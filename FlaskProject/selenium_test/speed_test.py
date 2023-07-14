import cProfile
import tensorflow as tf
import cv2
import numpy as np

classes_name_list=['图片缺角（建议更换图片角度）', '合格', '不合格（缺一角螺丝）', '不合格（缺临边两螺丝）', '不合格（缺对角两螺丝）', '不合格（缺三角螺丝）', '不合格（缺四角螺丝）']
model = tf.keras.models.load_model(r'C:\Users\LiYanLin\Desktop\defect_product_backEnd\model\VGG19_ft.h5')
def predict(path):
    import time
    img = cv2.imread(path)
    img = cv2.resize(img, (224, 224))
    img_tensor = tf.convert_to_tensor(img, dtype=tf.float16)
    img_tensor /= 255.0
    test_img = np.expand_dims(img_tensor, 0)
    # begin_time = time.time()
    out = model.predict(test_img)
    # end_time = time.time()
    # t = end_time - begin_time
    # time_result = str(round(t, 6)) + 's'
    # con = str(round(out[0][out.argmax()], 5))
    # if round(out[0][out.argmax()], 5) > 0.975:
    #     return classes_name_list[out.argmax()], time_result, con
    # else:
    #     return '该图片中无零件', time_result, con

# 运行性能分析器
profiler = cProfile.Profile()
profiler.enable()

# 执行要测试的函数
predict(r"C:\Users\LiYanLin\Desktop\defect_product_backEnd\dataset\anomaly\009.JPG")

profiler.disable()
profiler.print_stats()
