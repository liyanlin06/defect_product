import tensorflow as tf
import numpy as np
import cv2
import imgaug.augmenters as iaa
from make_dataset import get_dataset
from keras.utils.np_utils import to_categorical

# 加载预训练模型
inputs = tf.keras.layers.Input(shape=[224, 224, 3])
base_model = tf.keras.applications.resnet.ResNet152(layers=tf.keras.layers, include_top=False, weights='imagenet', input_tensor=inputs)
## 冻结参数
for l in base_model.layers:
    l.trainable = False  # 第一步锁定前层，不进行训练

# 添加输出层 (batch_size, 1000)->(batch_size, 7)
x = tf.keras.layers.GlobalAveragePooling2D(name='average_pool')(base_model.output)
fla = tf.keras.layers.Flatten()(base_model.output)
fc1 = tf.keras.layers.Dense(1024, activation='relu')(fla)
drop1 = tf.keras.layers.Dropout(rate=0.2)(fc1)
fc2 = tf.keras.layers.Dense(512, activation='relu')(drop1)
drop2 = tf.keras.layers.Dropout(rate=0.2)(fc2)
predictions = tf.keras.layers.Dense(7, activation='softmax')(drop2)
model = tf.keras.models.Model(inputs=inputs, outputs=predictions)

## 不使用预训练
# inputs = tf.keras.layers.Input(shape=[512, 512, 3])
# base_model = tf.keras.applications.resnet.ResNet152(include_top=False, input_tensor=inputs)
# x = tf.keras.layers.GlobalAveragePooling2D(name='average_pool')(base_model.output)
# fla = tf.keras.layers.Flatten()(base_model.output)
# fc1 = tf.keras.layers.Dense(1024, activation='relu')(fla)
# drop1 = tf.keras.layers.Dropout(rate=0.2)(fc1)
# fc2 = tf.keras.layers.Dense(512, activation='relu')(drop1)
# drop2 = tf.keras.layers.Dropout(rate=0.2)(fc2)
# predictions = tf.keras.layers.Dense(7, activation='softmax')(drop2)
# model = tf.keras.models.Model(inputs=inputs, outputs=predictions)


## 加载训练集和测试集
train_data, train_label, test_data, test_label = get_dataset()
train_label = to_categorical(train_label, num_classes=7)
test_label = to_categorical(test_label, num_classes=7)

## 定义超参数
learning_rate = 0.001
batch_size = 64
epochs = 1000

## 定义优化器和损失函数
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
loss = tf.keras.losses.categorical_crossentropy

## 编译模型

checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath='train_process/model/ResNet152_ft.h5',
                                                monitor='val_categorical_accuracy', verbose=1, save_best_only=True,
                                                mode='max')
callback_list = [checkpoint]
model.compile(optimizer=optimizer, loss=loss, metrics=['categorical_accuracy'])

print("-----------开始训练----------")
model.fit(train_data, train_label, epochs=epochs, batch_size=batch_size, validation_data=(test_data, test_label),
          callbacks=callback_list)

loss, accuracy = model.evaluate(train_data, train_label, verbose=0)
print(f" Train Loss: {loss:.4f} Train Accuracy: {accuracy:.4f}")
loss, accuracy = model.evaluate(test_data, test_label, verbose=0)
print(f"Test Loss: {loss:.4f} Test Accuracy: {accuracy:.4f}")