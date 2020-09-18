# Test_Task_Semantic_Segmentation_with_UNET
# Data
Data loaded from [2018 Data Science Bowl](https://www.kaggle.com/c/data-science-bowl-2018/data). In my case, I used stage1_train.zip which contains training set images(images and annotated masks) and stage1_test.zip  which contains test set images, preprocessing.py will create X_train, Y_train, X_test that used to train model. One example:
![example1](https://user-images.githubusercontent.com/71394662/93486818-4b36e000-f90d-11ea-9a88-ff27724b0c17.png)

# UNET
[UNET](https://arxiv.org/abs/1505.04597) - Convolutional Networks for Biomedical Image Segmentation. The goal of semantic image segmentation is to label each pixel of an image with a corresponding class of what is being represented. 

![image](https://gabe.smedresman.zone/content/images/2019/06/u-net-architecture.png) 

# Train
The model is trained for 36 epochs. After 36 epochs, calculated loss funcition is ~0.066 and dice_coef is ~0.764%. For dice_coef set smooth factor = 1e-6.

![image2](https://user-images.githubusercontent.com/71394662/93488261-d5337880-f90e-11ea-92e4-849d1df691b7.png)

# Test

The result of the model work on test data (X_test)


![Image3](https://user-images.githubusercontent.com/71394662/93516214-636d2600-f932-11ea-8700-0a5e9ee201cd.png)

# Implementation
 1. Create Python 3.6 + environment and install all requirements from requirements.txt
 2. Download data (download stage1_train.zip, stage1_test.zip and unpack in the data folder)
 3. Run preprocessing.py -> model_unet.py -> train.py -> predict_masks.py. 
 4. Run data_analysis.py.
