import os
import cv2
import numpy as np
import tensorflow as tf


def get_dataset():
    print("------------开始制作数据集------------")

    
    ## dataset路径
    train_dir = 'train_process/dataset_aug/train'
    test_dir = 'train_process/dataset_aug/test'

    ## 按照类别读取数据，添加标签

    train_data = []
    train_label = []
    test_data = []
    test_label = []

    ## 制作训练集
    folderNames = os.listdir(train_dir)
        
    for folderName in folderNames:
        print(folderName)
        if folderName == 'anomaly':
            label = 0
        elif folderName == 'good':
            label = 1
        elif folderName == 'one':
            label = 2
        elif folderName == 'neighbor_two':
            label = 3
        elif folderName == 'diagonal_two':
            label = 4
        elif folderName == 'three':
            label = 5
        else:
            label = 6
    
        folderPath = train_dir + folderName + '/'
        files = os.listdir(folderPath)
        
        for file in files:
            img = cv2.imread(folderPath + file)
            img = cv2.resize(img, (224, 224))
            img_tensor = tf.convert_to_tensor(img, dtype=tf.float16)
            img_tensor /= 255.0
            train_data.append(img_tensor)
            train_label.append(label)

    
    
    
    ## 制作测试集
    folderNames = os.listdir(test_dir)
        
    for folderName in folderNames:
        print(folderName)
        if folderName == 'anomaly':
            label = 0
        elif folderName == 'good':
            label = 1
        elif folderName == 'one':
            label = 2
        elif folderName == 'neighbor_two':
            label = 3
        elif folderName == 'diagonal_two':
            label = 4
        elif folderName == 'three':
            label = 5
        else:
            label = 6
    
        folderPath = test_dir + folderName + '/'
        files = os.listdir(folderPath)
        
        for file in files:
            img = cv2.imread(folderPath + file)
            img = cv2.resize(img, (224, 224))
            img_tensor = tf.convert_to_tensor(img, dtype=tf.float16)
            img_tensor /= 255.0
            test_data.append(img_tensor)
            test_label.append(label)

    

    train_data = tf.convert_to_tensor(train_data, dtype=tf.float16)
    test_data = tf.convert_to_tensor(test_data, dtype=tf.float16)
        
    print("train data length   : "+str(len(train_data)))
    print("train label length  : "+str(len(train_label)))
    print("test data length    : "+str(len(test_data)))
    print("test label length   : "+str(len(test_label)))
    
    print("------------数据集制作完成------------")

    
        
    return np.array(train_data), np.array(train_label), np.array(test_data), np.array(test_label)
    


