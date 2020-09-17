# Semantic_Segmentation_with_UNET
# Data
Data loaded from [2018 Data Science Bowl](https://www.kaggle.com/c/data-science-bowl-2018/data). In my case, I used stage1_train.zip which contains training set images(images and annotated masks) and stage1_test.zip  which contains test set images. preprocessing.py will create X_train, Y_train, X_test tht used to train model. One example:
![example1](https://user-images.githubusercontent.com/71394662/93486818-4b36e000-f90d-11ea-9a88-ff27724b0c17.png)

# UNET
[UNET](https://arxiv.org/abs/1505.04597) - Convolutional Networks for Biomedical Image Segmentation. The goal of semantic image segmentation is to label each pixel of an image with a corresponding class of what is being represented. 

![image](https://gabe.smedresman.zone/content/images/2019/06/u-net-architecture.png) 

# Train
The model is trained for 36 epochs. After 36 epochs, calculated loss funcition is ~0.0708 and dece_coef is ~0.748%. For Dice set smooth factor = 1e-6.

![image2](https://user-images.githubusercontent.com/71394662/93488261-d5337880-f90e-11ea-92e4-849d1df691b7.png)

