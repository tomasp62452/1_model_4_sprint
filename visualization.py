#!/usr/bin/env python
# coding: utf-8

# # Exploratory data analysis and visualization of Coursera Course data set
# 
# ### Tasks:
# - Download the data from Kaggle.
# - Load the data using Pandas.
# - Perform data cleaning by:
#   - Handling missing values.
#   - Removing duplicate samples and features.
#   - Treating the outliers.
# - Perform exploratory data analysis. Your analysis should provide answers to these questions:
#   - How many observations are there in this dataset?
#   - How many features this dataset has?
#   - Which of the features are categorical?
#   - Which of the features are numeric?
#   - Are there any artists that have more than 1 popular track? If yes, which and how many?
#   - Who was the most popular artist?
#   - How many artists in total have their songs in the top 50?
#   - Are there any albums that have more than 1 popular track? If yes, which and how many?
#   - How many albums in total have their songs in the top 50?
#   - Which tracks have a danceability score above 0.7?
#   - Which tracks have a danceability score below 0.4?
#   - Which tracks have their loudness above -5?
#   - Which tracks have their loudness below -8?
#   - Which track is the longest?
#   - Which track is the shortest?
#   - Which genre is the most popular?
#   - Which genres have just one song on the top 50?
#   - How many genres in total are represented in the top 50?
#   - Which features are strongly positively correlated?
#   - Which features are strongly negatively correlated?
#   - Which features are not correlated?
#   - How does the danceability score compare between Pop, Hip-Hop/Rap, Dance/Electronic, and Alternative/Indie genres?
#   - How does the loudness score compare between Pop, Hip-Hop/Rap, Dance/Electronic, and Alternative/Indie genres?
#   - How does the acousticness score compare between Pop, Hip-Hop/Rap, Dance/Electronic, and Alternative/Indie genres?
# - Provide clear explanations in your notebook. Your explanations should inform the reader what you are trying to achieve, the results you got, and what these results mean.
# - Provide suggestions for how your analysis could be improved.
# 

# ### Installing necessary packages

# In[1]:


#!pip install pipreqs
#!pip install -r requirements.txt
#!pip install pandas


# ### Importing libraries

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



#import os; print(os.getcwd())
#!pipreqs c:\Users\blockchain\Documents\turing_college
get_ipython().system('jupyter nbconvert --to script *.ipynb')
#!pipreqs .


# ### Loading data from Kaggle

# In[3]:


# An alternative way to download datasets from kaggle
# For this you have to install: pip install kaggle 
# Create API token ~\.kaggle\kaggle.json

import kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files('siddharthm1698/coursera-course-dataset', path= '.', unzip=True)


# In[ ]:


df = pd.read_csv('coursea_data.csv', index_col=0).sort_index()
df


# ### Data cleaning

# In[ ]:


df['course_students_enrolled'] = (
    df['course_students_enrolled']
    .str.replace('k', '*1_000')
    .str.replace('m', '*1_000_000')
    .map(eval)
)


# In[ ]:


df.info()


# No NaNs were found, so no actions were required.

# In[ ]:


df.describe().map(
    lambda x: '{:,.2f}'.format(x).rstrip('0').rstrip('.')
)


# ### Removing duplicated samples and features

# In[ ]:


duplicate_rows = df[df.duplicated()]
duplicate_rows


# 
# No duplicated rows were found, so no actions were required.

# In[ ]:


del duplicate_rows


# In[ ]:


duplicate_columns = df.columns[df.columns.duplicated()]
duplicate_columns


# 
# No duplicated columns were found, so no actions were required.

# In[ ]:


del duplicate_columns


# ### Treating outliers

# In[ ]:


numerical_features


# In[ ]:


# Visualize the distribution of numerical features to identify outliers
numerical_features = df.select_dtypes(include=[np.number]).columns

# Plot boxplots for numerical features in a grid view
plt.figure(figsize=(15, 10))
for i, feature in enumerate(numerical_features):
    plt.subplot(4, 3, i + 1)
    sns.boxplot(x=df[feature])
    plt.title(f'Boxplot of {feature}')
plt.tight_layout()
plt.show()


# In[ ]:




