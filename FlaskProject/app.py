import zipfile
import cv2
from flask import *
import tensorflow as tf
from flask_mail import Mail, Message
from pasta.base.annotate import expression
import numpy as np
import os
from flask_cors import CORS, cross_origin

# classes_name_list=['anomaly', 'good', 'one', 'neighbor_two', 'diagonal_two', 'three', 'four']
classes_name_list=['图片缺角（建议更换图片角度）', '合格', '不合格（缺一角螺丝）', '不合格（缺临边两螺丝）', '不合格（缺对角两螺丝）', '不合格（缺三角螺丝）', '不合格（缺四角螺丝）']
UPLOAD_PATH = r'./uploads'
model = tf.keras.models.load_model(r'C:\Users\LiYanLin\Desktop\defect_product_backEnd\model\VGG19_ft.h5')

# 1. 初始化 flask app
app = Flask(__name__)
app.config['MAIL_DEBUG'] = False            # 开启debug，便于调试看信息
app.config['MAIL_SUPPRESS_SEND'] = False    # 发送邮件，为True则不发送
app.config['MAIL_SERVER'] = 'smtp.qq.com'   # 邮箱服务器
app.config['MAIL_PORT'] = 465               # 端口
app.config['MAIL_USE_SSL'] = True           # 重要，qq邮箱需要使用SSL
app.config['MAIL_USE_TLS'] = False          # 不需要使用TLS
app.config['MAIL_USERNAME'] = '516680918@qq.com'  # 填邮箱
app.config['MAIL_PASSWORD'] = '**********'      # 填授权码，为了保密我把我的授权码删去了
app.config['MAIL_DEFAULT_SENDER'] = '516680918@qq.com'  # 填邮箱，默认发送者
mail = Mail(app)

# 2. 解决跨域
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    return response


# 3. 主页面
@app.route('/', methods=['GET', 'POST'])
def home():
    return redirect(url_for('static', filename='./index.html'))

# 4. 预测函数
def predict(path):
    import time
    img = cv2.imread(path)
    img = cv2.resize(img, (224, 224))
    img_tensor = tf.convert_to_tensor(img, dtype=tf.float16)
    img_tensor /= 255.0
    test_img = np.expand_dims(img_tensor, 0)
    begin_time = time.time()
    out = model.predict(test_img)
    end_time = time.time()
    t = end_time - begin_time
    time_result = str(round(t, 6)) + 's'
    con = str(round(out[0][out.argmax()], 5))
    if round(out[0][out.argmax()], 5) > 0.975:
        return classes_name_list[out.argmax()], time_result, con
    else:
        return '该图片中无零件', time_result, con

# 5. 上传待检测图片
@app.route('/upload', methods=['POST'])
def upload():
    ## 接收前端发送的待检测图片
    file = request.files['file']
    ## 获取图片名
    file_name = file.filename
    ## 图片保存路径
    file_path = UPLOAD_PATH + '/' + file_name
    ## 图片保存
    file.save(file_path)
    ## 调用预测
    result, time, con = predict(file_path)
    ## 返回分类结果和时间
    return jsonify({
        'result': result,
        'time': time,
        'con': con
    })

# 6. 接受邮箱并发送结果
@app.route('/email', methods=['POST'])
def email():
    address = request.form.get('address')
    msg = Message(
        subject="Predict Results",
        recipients=[address]
    )
    msg.body = "Please check the test results of the industrial products you submitted."
    with app.open_resource("results.txt") as fp:
        msg.attach("results.txt", "file/txt", fp.read())
    try:
        mail.send(msg)
        return "发送成功"
    except expression(BaseException) as e:
        print(e)
        return "发送失败"

# 7. 接受前端传来的zip压缩包
@app.route('/upload_zip', methods=['POST'])
def upload_zip():
    file = request.files['file']
    file_name = file.filename
    file_path = UPLOAD_PATH + '/' + file_name
    file.save(file_path)
    zip_files = zipfile.ZipFile(file_path)
    try:
        zip_files.extractall(UPLOAD_PATH)
        names = file_name.split('.')
        name = names[0]
        with open('results.txt', 'w', encoding='utf-8') as f:
            for root, dirs, files in os.walk(UPLOAD_PATH + '/' + name):
                for file in files:
                    path = os.path.join(root, file)
                    path = path.replace('\\', '/')
                    result, time, con = predict(path)
                    f.writelines(file + ' ' + result + ' ' + time + ' ' + con + '\n')


        return "上传并解压成功"
    except expression(BaseException) as e:
        print(e)
        return "解压失败"


if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
