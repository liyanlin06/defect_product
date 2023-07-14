import tensorflow as tf
from make_dataset import get_dataset




train_data, train_label, test_data, test_label = get_dataset()


model = tf.keras.models.load_model('train_process/model/VGG19_ft.h5')
out = model.predict(train_data, verbose=0)
with open('train_process/code/result.txt', 'w') as f:
    f.write(str(train_label)+'\n')    
    for i in out:
        f.write(str(i.argmax())+' ')