import tensorflow as tf
from keras_flops import get_flops


model = tf.keras.models.load_model(r'C:\Users\LiYanLin\Desktop\defect_product_backEnd\model\ResNet152_best.h5')
flops = get_flops(model, batch_size=1)
print(model.summary())
print(f"FLOPS: {flops / 10 ** 9:.03} G")
