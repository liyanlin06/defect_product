import torch
from torchvision.transforms import transforms
import tensorflow as tf


class GetLoader(torch.utils.data.Dataset):
# 初始化函数，得到数据
    def __init__(self, data_root, data_label):
        # 在这里调用自己的数据
        self.data = data_root
        self.label = data_label
# index是根据batch size划分数据后得到的索引，最后将data和对应的labels进行一起返回
    def __getitem__(self, index):
        im_trans = transforms.Compose([
            transforms.ToPILImage(),
            transforms.CenterCrop(size=224),
            transforms.ToTensor(),
            transforms.Normalize([0.5520, 0.5336, 0.5050],
                                 [0.2353, 0.2345, 0.2372]),
        ])
        return tf.transpose((self.data[index]), perm=[2, 0, 1]), torch.tensor(self.label[index], dtype=torch.float)
# 该函数返回数据大小长度，目的是DataLoader方便划分，如果不知道大小，DataLoader会一脸懵逼
    def __len__(self):
        return len(self.data)
