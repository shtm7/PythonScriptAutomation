#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


print('Hi, Welcome to test Jupyter notebook\n-----------------------------------------------------------------------------------------------------------')


# In[2]:


DataDictionary = pd.read_excel('./Preprocess Files/Dictionary Edited.xlsx')
DataDictionary.to_excel("DTset.xlsx")


# In[ ]:




