#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import os
import random

import matplotlib.pyplot as plt
import numpy as np

from skimage.io import imshow

# Dataset consists of pictures (a large number of segmented nuclei images).
# Within this folder are two subfolders:
# -images contains the image file
# -masks contains the segmented masks of each nucleus. This folder is only included in the training set.
#  Each mask contains one nucleus. Masks are not allowed to overlap (no pixel belongs to two masks)
# Сonvert each image of the nucleus into one image so that each image of the nucleus is compared with one mask.


# # Load data

# In[ ]:


from preprocessing import load_data, plot_example
X_train, Y_train, X_test = load_data(IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS)


# #  Show example

# In[ ]:


plot_example(X_train, Y_train)


# 
