import os
import random
import imgaug.augmenters as iaa
import imageio.v2 as imageio



def get_dataset():
    
    print("------------开始制作数据集------------")

    # 之前的扩充方法是，每张图像只使用了一种扩充方法，但实际上完全可以先旋转各种角度然后再加噪声
    # 测试集里最好不加噪声，只是旋转
    
    
    ## 原图系列
    #### 原图水平翻转180
    seq1 = iaa.Sequential([ 
        iaa.Fliplr(1), 
    ])

    #### 原图垂直翻转180
    seq2 = iaa.Sequential([
        iaa.Flipud(1),
    ])

    #### 原图旋转90
    seq3 = iaa.Sequential([
        iaa.Affine(rotate=90)
    ])
    
    #### 原图旋转270
    seq4 = iaa.Sequential([
        iaa.Affine(rotate=270)
    ])
    
    #### 原图-180到180之间旋转随机角度
    seq5 = iaa.Sequential([
        iaa.Affine(rotate=(-180, 180))
    ])
    
    #### 原图高斯噪声
    seq6 = iaa.Sequential([
        iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255))
    ])
    
    #### 原图散粒噪声
    seq7 = iaa.Sequential([
        iaa.imgcorruptlike.ShotNoise(severity=2)
    ])
    
    #### 原图斑点噪声
    seq8 = iaa.Sequential([
        iaa.imgcorruptlike.SpeckleNoise(severity=2)
    ])
    
    #### 原图像变暗
    seq9 = iaa.Sequential([
        iaa.Multiply(mul=(0.75), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    #### 原图像变亮
    seq10 = iaa.Sequential([
        iaa.Multiply(mul=(1.25), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    #### 原图锐化
    seq11 = iaa.Sequential([
        iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5))
    ])
    

    
    ## 水平翻转180系列
    #### 水平180 + 高斯噪声
    seq12 = iaa.Sequential([
        iaa.Fliplr(1), 
        iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255))
    ])
    
    #### 水平180 + 散粒噪声
    seq13 = iaa.Sequential([
        iaa.Fliplr(1), 
        iaa.imgcorruptlike.ShotNoise(severity=2)
    ])
    
    #### 水平180 + 斑点噪声
    seq14 = iaa.Sequential([
        iaa.Fliplr(1), 
        iaa.imgcorruptlike.SpeckleNoise(severity=2)
    ])
    
    #### 水平180 + 图像变暗
    seq15 = iaa.Sequential([
        iaa.Fliplr(1), 
        iaa.Multiply(mul=(0.75), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    #### 水平180 + 图像变亮
    seq16 = iaa.Sequential([
        iaa.Fliplr(1), 
        iaa.Multiply(mul=(1.25), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    
    #### 水平180 + 图像锐化
    seq17 = iaa.Sequential([
        iaa.Fliplr(1), 
        iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5))
    ])
    
    
    ## 垂直翻转180系列
    #### 垂直180 + 高斯噪声
    seq18 = iaa.Sequential([
        iaa.Flipud(1),
        iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255))
    ])
    
    #### 垂直180 + 散粒噪声
    seq19 = iaa.Sequential([
        iaa.Flipud(1),
        iaa.imgcorruptlike.ShotNoise(severity=2)
    ])
    
    #### 垂直180 + 斑点噪声
    seq20 = iaa.Sequential([
        iaa.Flipud(1),
        iaa.imgcorruptlike.SpeckleNoise(severity=2)
    ])
    
    #### 垂直180 + 图像变暗
    seq21 = iaa.Sequential([
        iaa.Flipud(1),
        iaa.Multiply(mul=(0.75), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    #### 垂直180 + 图像变亮
    seq22 = iaa.Sequential([
        iaa.Flipud(1),
        iaa.Multiply(mul=(1.25), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    
    #### 垂直180 + 图像锐化
    seq23 = iaa.Sequential([
        iaa.Flipud(1),
        iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5))
    ])
    
    
    ## 旋转90系列
    #### 90 + 高斯噪声
    seq24 = iaa.Sequential([
        iaa.Affine(rotate=90),
        iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255))
    ])
    
    #### 90 + 散粒噪声
    seq36 = iaa.Sequential([
        iaa.Affine(rotate=90),
        iaa.imgcorruptlike.ShotNoise(severity=2)
    ])
    
    #### 90 + 斑点噪声
    seq25 = iaa.Sequential([
        iaa.Affine(rotate=90),
        iaa.imgcorruptlike.SpeckleNoise(severity=2)
    ])
    
    
    #### 90 + 图像变暗
    seq26 = iaa.Sequential([
        iaa.Affine(rotate=90),
        iaa.Multiply(mul=(0.5), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    #### 90 + 图像变亮
    seq27 = iaa.Sequential([
        iaa.Affine(rotate=90),
        iaa.Multiply(mul=(1.5), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    
    #### 90 + 图像锐化
    seq28 = iaa.Sequential([
        iaa.Affine(rotate=90),
        iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5))
    ])
    
    
    ## 旋转270系列
    #### 270 + 高斯噪声
    seq29 = iaa.Sequential([
        iaa.Affine(rotate=270),
        iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255))
    ])
    
    #### 270 + 散粒噪声
    seq30 = iaa.Sequential([
        iaa.Affine(rotate=270),
        iaa.imgcorruptlike.ShotNoise(severity=2)
    ])
    
    #### 270 + 斑点噪声
    seq31 = iaa.Sequential([
        iaa.Affine(rotate=270),
        iaa.imgcorruptlike.SpeckleNoise(severity=2)
    ])
    
    #### 270 + 图像变暗
    seq32 = iaa.Sequential([
        iaa.Affine(rotate=270),
        iaa.Multiply(mul=(0.75), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    #### 270 + 图像变亮
    seq33 = iaa.Sequential([
        iaa.Affine(rotate=270),
        iaa.Multiply(mul=(1.25), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    #### 270 + 图像锐化
    seq34 = iaa.Sequential([
        iaa.Affine(rotate=270),
        iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5))
    ])
    
    
    ## 旋转180到180随机角度系列
    #### 随机 + 高斯噪声
    seq35 = iaa.Sequential([
        iaa.Affine(rotate=(180, 180)),
        iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255))
    ])
    
    #### 随机 + 散粒噪声
    seq36 = iaa.Sequential([
        iaa.Affine(rotate=(180, 180)),
        iaa.imgcorruptlike.ShotNoise(severity=2)
    ])
    
    #### 随机 + 斑点噪声
    seq37 = iaa.Sequential([
        iaa.Affine(rotate=(180, 180)),
        iaa.imgcorruptlike.SpeckleNoise(severity=2)
    ])
    
    #### 随机 + 图像变暗
    seq38 = iaa.Sequential([
        iaa.Affine(rotate=(180, 180)),
        iaa.Multiply(mul=(0.75), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    #### 随机 + 图像变亮
    seq39 = iaa.Sequential([
        iaa.Affine(rotate=(180, 180)),
        iaa.Multiply(mul=(1.25), per_channel=False, name=None,  deterministic="deprecated", random_state=None)
    ])
    
    #### 随机 + 图像锐化
    seq40 = iaa.Sequential([
        iaa.Affine(rotate=(180, 180)),
        iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5))
    ])

    
    
    
    
    
    
    ## dataset路径
    dir = '/home/sduu2/userspace/lyl/product_detect/defect_product_dataset/multi_classification/'
    ## aug之后的数据集路径
    aug_train_dir = '/home/sduu2/userspace/lyl/product_detect/dataset_aug/train/'
    aug_test_dir = '/home/sduu2/userspace/lyl/product_detect/dataset_aug/test/'
    
    ## 在train和test下面创建每个类别的文件夹
    os.makedirs(aug_train_dir + 'anomaly')
    os.makedirs(aug_test_dir + 'anomaly')
    os.makedirs(aug_train_dir + 'good')
    os.makedirs(aug_test_dir + 'good')
    os.makedirs(aug_train_dir + 'one')
    os.makedirs(aug_test_dir + 'one')
    os.makedirs(aug_train_dir + 'neighbor_two')
    os.makedirs(aug_test_dir + 'neighbor_two')
    os.makedirs(aug_train_dir + 'diagonal_two')
    os.makedirs(aug_test_dir + 'diagonal_two')
    os.makedirs(aug_train_dir + 'three')
    os.makedirs(aug_test_dir + 'three')
    os.makedirs(aug_train_dir + 'four')
    os.makedirs(aug_test_dir + 'four')


    ## 遍历每个类别文件夹
    folderNames = os.listdir(dir)

    for folderName in folderNames:
    
        print(folderName)

        folderPath = dir + folderName + '/'
        files = os.listdir(folderPath)
        files.sort()
    
    
        #### 该类别下的数据数量
        size = len(files)
    
        #### 确定测试集数据数量，剩余即为训练集
        test_size= size//10
        test_size *= 2


        #### 确定测试集的index
        test_index = random.sample(range(0, size), test_size)


        #### 根据index，划分训练和测试
        for i in range(size):
            fileName = files[i]
            filePath = folderPath + fileName
            img = imageio.imread(filePath)
            names = str.split(fileName, '.')
            name = names[0]
            
            if i in test_index:
                ## 原图
                imageio.imwrite(aug_test_dir + folderName + '/' + name + "_0.JPG", img)
                [img_seq1,]=seq1(images=[img])
                imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_1.JPG", img_seq1)
                [img_seq2,]=seq2(images=[img])
                imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_2.JPG", img_seq2)
                [img_seq3,]=seq3(images=[img])
                imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_3.JPG", img_seq3)
                [img_seq4,]=seq4(images=[img])
                imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_4.JPG", img_seq4)
                [img_seq5,]=seq5(images=[img])
                imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_5.JPG", img_seq5)
                # [img_seq6,]=seq6(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_6.JPG", img_seq6)
                [img_seq7,]=seq7(images=[img])
                imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_7.JPG", img_seq7)
                [img_seq8,]=seq8(images=[img])
                imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_8.JPG", img_seq8)
                
                [img_seq9,]=seq9(images=[img])
                imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_9.JPG", img_seq9)
                [img_seq10,]=seq10(images=[img])
                imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_10.JPG", img_seq10)
                
                # [img_seq11,]=seq11(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_11.JPG", img_seq11)
                # [img_seq12,]=seq12(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_12.JPG", img_seq12)
                # [img_seq13,]=seq13(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_13.JPG", img_seq13)
                # [img_seq14,]=seq14(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_14.JPG", img_seq14)
                # [img_seq15,]=seq15(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_15.JPG", img_seq15)
                # [img_seq16,]=seq16(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_16.JPG", img_seq16)
                # [img_seq17,]=seq17(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_17.JPG", img_seq17)
                # [img_seq18,]=seq18(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_18.JPG", img_seq18)
                # [img_seq19,]=seq19(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_19.JPG", img_seq19)
                # [img_seq20,]=seq20(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_20.JPG", img_seq20)
                # [img_seq21,]=seq21(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_21.JPG", img_seq21)
                # [img_seq22,]=seq22(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_22.JPG", img_seq22)
                # [img_seq23,]=seq23(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_23.JPG", img_seq23)
                # [img_seq24,]=seq24(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_24.JPG", img_seq24)
                # [img_seq25,]=seq25(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_25.JPG", img_seq25)
                # [img_seq26,]=seq26(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_26.JPG", img_seq26)
                # [img_seq27,]=seq27(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_27.JPG", img_seq27)
                # [img_seq28,]=seq28(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_28.JPG", img_seq28)
                # [img_seq29,]=seq29(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_29.JPG", img_seq29)
                # [img_seq30,]=seq30(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_30.JPG", img_seq30)
                # [img_seq31,]=seq31(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_31.JPG", img_seq31)
                # [img_seq32,]=seq32(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_32.JPG", img_seq32)
                # [img_seq33,]=seq33(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_33.JPG", img_seq33)
                # [img_seq34,]=seq34(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_34.JPG", img_seq34)
                # [img_seq35,]=seq35(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_35.JPG", img_seq35)
                # [img_seq36,]=seq36(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_36.JPG", img_seq36)
                # [img_seq37,]=seq37(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_37.JPG", img_seq37)
                # [img_seq38,]=seq38(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_38.JPG", img_seq38)
                # [img_seq39,]=seq39(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_39.JPG", img_seq39)
                # [img_seq40,]=seq40(images=[img])
                # imageio.imwrite(aug_test_dir  + folderName + '/' + name + "_40.JPG", img_seq40)


                
            else:
                ## 扩充训练集 
                imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_0.JPG", img)
                [img_seq1,]=seq1(images=[img])
                imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_1.JPG", img_seq1)
                [img_seq2,]=seq2(images=[img])
                imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_2.JPG", img_seq2)
                [img_seq3,]=seq3(images=[img])
                imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_3.JPG", img_seq3)
                [img_seq4,]=seq4(images=[img])
                imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_4.JPG", img_seq4)
                [img_seq5,]=seq5(images=[img])
                imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_5.JPG", img_seq5)
                # [img_seq6,]=seq6(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_6.JPG", img_seq6)
                [img_seq7,]=seq7(images=[img])
                imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_7.JPG", img_seq7)
                [img_seq8,]=seq8(images=[img])
                imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_8.JPG", img_seq8)
                [img_seq9,]=seq9(images=[img])
                imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_9.JPG", img_seq9)
                [img_seq10,]=seq10(images=[img])
                imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_10.JPG", img_seq10)
                
                # [img_seq11,]=seq11(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_11.JPG", img_seq11)
                # [img_seq12,]=seq12(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_12.JPG", img_seq12)
                # [img_seq13,]=seq13(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_13.JPG", img_seq13)
                # [img_seq14,]=seq14(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_14.JPG", img_seq14)
                # [img_seq15,]=seq15(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_15.JPG", img_seq15)
                # [img_seq16,]=seq16(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_16.JPG", img_seq16)
                # [img_seq17,]=seq17(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_17.JPG", img_seq17)
                # [img_seq18,]=seq18(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_18.JPG", img_seq18)
                # [img_seq19,]=seq19(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_19.JPG", img_seq19)
                # [img_seq20,]=seq20(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_20.JPG", img_seq20)
                # [img_seq21,]=seq21(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_21.JPG", img_seq21)
                # [img_seq22,]=seq22(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_22.JPG", img_seq22)
                # [img_seq23,]=seq23(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_23.JPG", img_seq23)
                # [img_seq24,]=seq24(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_24.JPG", img_seq24)
                # [img_seq25,]=seq25(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_25.JPG", img_seq25)
                # [img_seq26,]=seq26(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_26.JPG", img_seq26)
                # [img_seq27,]=seq27(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_27.JPG", img_seq27)
                # [img_seq28,]=seq28(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_28.JPG", img_seq28)
                # [img_seq29,]=seq29(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_29.JPG", img_seq29)
                # [img_seq30,]=seq30(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_30.JPG", img_seq30)
                # [img_seq31,]=seq31(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_31.JPG", img_seq31)
                # [img_seq32,]=seq32(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_32.JPG", img_seq32)
                # [img_seq33,]=seq33(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_33.JPG", img_seq33)
                # [img_seq34,]=seq34(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_34.JPG", img_seq34)
                # [img_seq35,]=seq35(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_35.JPG", img_seq35)
                # [img_seq36,]=seq36(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_36.JPG", img_seq36)
                # [img_seq37,]=seq37(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_37.JPG", img_seq37)
                # [img_seq38,]=seq38(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_38.JPG", img_seq38)
                # [img_seq39,]=seq39(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_39.JPG", img_seq39)
                # [img_seq40,]=seq40(images=[img])
                # imageio.imwrite(aug_train_dir  + folderName + '/' + name + "_40.JPG", img_seq40)
                
                

    
    print("------------数据集制作完成------------")
        
    

if __name__ == '__main__':
    get_dataset()