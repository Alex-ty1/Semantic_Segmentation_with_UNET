#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from keras.callbacks import EarlyStopping, ModelCheckpoint

def train(model, X_train, Y_train, validation_split=0.1, batch_size=16, epochs=50):
    earlystopper = EarlyStopping(patience=5, verbose=1)
    checkpointer = ModelCheckpoint('model-dsbowl2018-1.h5', verbose=1, save_best_only=True)
    return  model.fit(X_train, Y_train, validation_split=0.1, batch_size=16, epochs=50, 
                      callbacks=[earlystopper, checkpointer])
    

if __name__ == '__main__':
    
    from model_unet import model_unet, dice_coef
    from preprocessing import load_data, plot_example
    
    IMG_HEIGHT = 128
    IMG_WIDTH = 128
    IMG_CHANNELS = 3
    TRAIN_PATH ='train_images' 
    TEST_PATH ='test_images' # image path
    train_ids = next(os.walk(TRAIN_PATH))[1]
    test_ids = next(os.walk(TEST_PATH))[1]
    X_train, Y_train, X_test = load_data(IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS)
    model = model_unet(IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS)
    train(model, X_train, Y_train)

