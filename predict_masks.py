#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tensorflow.keras.models import load_model
from model_unet import dice_coef

def load_model1():
    return load_model('model-dsbowl2018-1.h5', custom_objects={'dice_coef': dice_coef})

def predict_masks(model, X_test):
    model = load_model1()
    return model.predict(X_test, verbose=1)

if __name__ == '__main__':
        
    IMG_HEIGHT = 128
    IMG_WIDTH = 128
    IMG_CHANNELS = 3   
    model = load_model1()
    X_train, Y_train, X_test = load_data(IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS)
    preds_test = model.predict_masks(X_test, verbose=1)
    
    def plot_sample(X_test, preds_test, ix=None):
        
        if ix is None:
            ix = random.randint(0, len(X_test))
        has_mask = preds_test[ix].max() > 0

        fig, ax = plt.subplots(1, 2, figsize=(20, 10))
        ax[0].imshow(X_test[ix, ..., 0], cmap='seismic')
        ax[0].set_title('Seismic')

        ax[1].imshow(preds_test[ix].squeeze(), vmin=0, vmax=1)
        ax[1].set_title('Salt Predicted');
        plot_sample(X_test, preds_test, ix=None)

