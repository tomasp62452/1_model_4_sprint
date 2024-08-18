#!/usr/bin/env python
# coding: utf-8

# ### Importing libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# ## Loading data from Kaggle

# In[2]:


# An alternative way to download datasets from kaggle
# For this you have to install: pip install kaggle 
# Create API token ~\.kaggle\kaggle.json

import kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files('siddharthm1698/coursera-course-dataset', path= '.', unzip=True)


# In[3]:


df1 = pd.read_csv('coursea_data.csv', index_col=0).sort_index()
df1


# 

# In[4]:


df1.info()


# In[ ]:




