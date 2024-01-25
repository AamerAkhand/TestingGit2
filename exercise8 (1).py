#!/usr/bin/env python
# coding: utf-8

# # Exercise 8

# In[4]:

#hello
# Execute this code block to import the NumPy library
import numpy as np


# #### Problem 1
# 
# Create an `ndarray` object with data-type `float`, shape (2,3,4), and all values initialized to `5`.

# In[20]:


problem1 = np.ndarray(shape = (2,3,4),dtype = float)
problem1.fill(5)


# #### Problem 2
# 
# Develop a function `problem2(array1, array2)` with returns `True` if binary arithmetic operations (+, -, \*, etc) may be applied to the arrays `array1` and `array2`, `False` otherwise.

# In[14]:


def problem2(array1, array2):
    A = array1.ndim
    B = array2.ndim
    
    if array1.shape == array2.shape:
        return True
    if A > B:
        pass


# #### Problem 3
# 
# Develop a function `problem3(array1, array2)` that returns the shape of the result of applying binary arithmetic operations (+, -, \*, etc) to the arrays `array1` and `array2` or `None` if doing so would result in a semantic error.

# In[ ]:


def problem3(array1, array2):
    pass


# #### Problem 4
# 
# Given an array `p4arr`, create a new array whose values correspond to applying the natural logarithm to each of the values in `p4arr`.

# In[ ]:


problem4 = None


# #### Problem 5
# 
# Create an `ndarray` with values ranging from 5 to 50 in increments of 5.

# In[21]:


problem5 = np.arange(5,55,5)


# #### Problem 6
# 
# Create an `ndarray` with values ranging from 5 to 50 in increments of 5 in a way different from the previous problem.

# In[24]:


problem6 = np.linspace(5,50,10)


# #### Problem 7
# 
# Develop a function `problem7(array1)` which returns a tuple `(min, max, mean)` of the minimum, maximum, and mean values in the array.

# In[ ]:


def problem7(array1):
    return (array1.min(), array1.max(), array1.sum()/array1.size)


# #### Problem 8
# 
# Given an array of integers `p8arr`, determine the number of values in the array greater than 5 **without** using loops.

# In[ ]:


problem8 = None

