import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model(r'C:\Users\LiYanLin\Desktop\defect_product_backEnd\train_process\model\VGG19_ft.h5')
img = cv2.imread(r"C:\Users\LiYanLin\Desktop\defect_product_backEnd\train_process\defect_product_dataset\multi_classification\anomaly\009.JPG")
img = cv2.resize(img, (224, 224))
img_tensor = tf.convert_to_tensor(img, dtype=tf.float16)
img_tensor /= 255.0
test_img = np.expand_dims(img_tensor, 0)
out = model.predict(test_img)
print(out.argmax())