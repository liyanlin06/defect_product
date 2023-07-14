import os
import cv2


def get_dataset():

    print("------------开始制作数据集------------")

    ## dataset路径
    dir = r'C:\Users\LiYanLin\Desktop\defect_product_backEnd\dataset'

    data = []
    labels = []

    ## 遍历每个类别文件夹
    folderNames = os.listdir(dir)

    for folderName in folderNames:
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
        print(folderName)

        folderPath = dir + "\\" + folderName + '\\'
        files = os.listdir(folderPath)
        files.sort()

        #### 该类别下的数据数量
        size = len(files)

        for i in range(size):
            fileName = files[i]
            filePath = folderPath + fileName
            img = cv2.imread(filePath)
            data.append(img)
            labels.append(label)


    # print(len(data))
    # print(len(labels))
    # print(labels)
    print("------------数据集制作完成------------")
    return data, labels


if __name__ == '__main__':
    get_dataset()