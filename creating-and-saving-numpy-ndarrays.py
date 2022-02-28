#!/usr/bin/env python
# coding: utf-8

# ### Example 1.a - Using a 1-D Array of Integers (Rank #1 Array)
# 

# In[ ]:


import numpy as np

# We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

# Let's print the ndarray we just created using the print() command
print('x = ', x)


# In[ ]:


# We print information about x
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)
print('x has dimensions:', x.shape)
print('x has size:', x.size)


# ### Example 1.b  - Using 1-D Array of Strings (Rank #1 Array)

# In[ ]:


# We create a rank 1 ndarray that only contains strings
x = np.array(['Hello', 'World'])

# We print information about x
print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)


# ### Example 1.c - Using a 1-D Array of Int and String (Rank #1 Array)
# ***NumPy will assign each element a same datatype because NumPy arrays must contains elements of same type.***

# In[ ]:


# We create a rank 1 ndarray from a Python list that contains integers and strings
x = np.array([1, 2, 'World'])

# We print information about x
print('x = ', x)
print('x has dimensions:', x.shape) 
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)


# ### Example 1.d - Using a 1-D Array of Int and Float
# ***Upcasting demo*** - All integers will be converted (upgraded) to Float datatype. It is called upcasting, not downcasting, because a Float has a precision value (digits after the decimal). 

# In[ ]:


# We create a rank 1 ndarray that contains integers
x = np.array([1,2,3])

# We create a rank 1 ndarray that contains floats
y = np.array([1.0,2.0,3.0])

# We create a rank 1 ndarray that contains integers and floats
z = np.array([1, 2.5, 4])

# We print the dtype of each ndarray
print('The elements in x are of type:', x.dtype)
print('The elements in y are of type:', y.dtype)
print('The elements in z are of type:', z.dtype)


# ### Example 1.e - Using a 1-D Array of Float, and specifying the datatype of each element as int64
# ***NOTE*** - Precision will be lost in this example

# In[ ]:


# We create a rank 1 ndarray of floats but set the dtype to int64
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)

# We print the dtype x
print('x = ', x)
print('The elements in x are of type:', x.dtype)


# ### Example 2 - Using a 2-D Array (Rank #2 Array)

# In[ ]:


# We create a rank 2 ndarray that only contains integers
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])

# We print information about Y
print('Y = \n', Y)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)
print('Y has dimensions:', Y.shape)
print('Y has a total of', Y.size, 'elements')


# ### Example 3 - Save the NumPy array to a File

# In[ ]:


# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])

# We save x into the current directory as 
np.save('my_array', x)


# In[ ]:


# We load the saved array from our current directory into variable y
y = np.load('my_array.npy')

# We print information about the ndarray we loaded
print('Y = \n', y)
print('y is an object of type:', type(y))
print('The elements in y are of type:', y.dtype)

