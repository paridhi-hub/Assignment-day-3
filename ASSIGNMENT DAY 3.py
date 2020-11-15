#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1

import numpy as np
arr = np.array(range(2,50,3))
print(arr)


# In[2]:


# Question 2
import numpy as np

arr1 = np.array([int(input())for i in range(5)])
arr2 = np.array([int(input())for i in range(5)])
arr_sum = np.concatenate((arr1,arr2))
print(arr_sum)
print(np.sort(arr_sum))


# In[3]:


#Question 3

arr = np.array([1,2,3,4,5])
print(arr.ndim)
print(arr.size)


# In[4]:


#Question 4

arr = np.array([int(input())for i in range(10)])
# Convert 1D array to a 2D numpy array of 2 rows and 3 columns
arr_2d = np.reshape(arr, (2, 5))
print(arr_2d)


# In[5]:


#Question 5

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.vstack(a))
print(np.hstack(a))


# In[9]:


# Question 6

arr = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18])


# Get a tuple of unique values & their frequency in numpy array

uniqueValues, occurCount = np.unique(arr, return_counts=True)
print("Unique Values : " , uniqueValues)
print("Occurrence Count : ", occurCount)


# In[ ]:




