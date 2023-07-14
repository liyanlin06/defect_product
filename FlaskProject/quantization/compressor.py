import tensorflow as tf
from neural_compressor import PostTrainingQuantConfig
from neural_compressor import quantization
from dataset import GetLoader


from torch.utils.data import DataLoader
from make_dataset import get_dataset

data, label = get_dataset()
dataset = GetLoader(data, label)
dataloader = DataLoader(dataset, batch_size=64, shuffle=True, drop_last=True)


model = tf.keras.models.load_model(r'C:\Users\LiYanLin\Desktop\defect_product_backEnd\model\VGG19.h5')
conf = PostTrainingQuantConfig()
q_model = quantization.fit(model=model,
                           conf=conf,
                           calib_dataloader=dataloader)
# q_model.save(r'after_compressor/')