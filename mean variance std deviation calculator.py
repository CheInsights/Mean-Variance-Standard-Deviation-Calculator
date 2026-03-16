#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def calculate(list):
    # 1. Validation: Ensure the list has exactly 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # 2. Reshape the list into a 3x3 Numpy array
    # We convert to float to ensure consistent math, though int works too
    matrix = np.array(list).reshape(3, 3)

    # 3. Perform calculations
    # axis=0 refers to columns (vertical)
    # axis=1 refers to rows (horizontal)
    # None (default) refers to the flattened matrix
    
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), 
            matrix.mean(axis=1).tolist(), 
            matrix.mean().tolist()
        ],
        'variance': [
            matrix.var(axis=0).tolist(), 
            matrix.var(axis=1).tolist(), 
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(), 
            matrix.std(axis=1).tolist(), 
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(), 
            matrix.max(axis=1).tolist(), 
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(), 
            matrix.min(axis=1).tolist(), 
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(), 
            matrix.sum(axis=1).tolist(), 
            matrix.sum().tolist()
        ]
    }

    return calculations


# In[3]:


print(calculate([0,1,2,3,4,5,6,7,8]))


# In[7]:


print(calculate([0,10,20,30,40,50,60,70,80]))


# In[8]:


print(calculate([5,10,15,20,25,30,35,40,45]))


# In[ ]:




