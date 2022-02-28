#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

my_list = [1,2,3,4,5]
np.array(my_list)


# #### Example 1. Create a Numpy array of zeros with a desired shape

# In[ ]:


# We create a 3 x 4 ndarray full of zeros. 
X = np.zeros((3,4), dtype=int)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)


# #### Example 2. Create a Numpy array of ones

# In[ ]:


# We create a 3 x 2 ndarray full of ones. 
X = np.ones((3,2))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype) 


# #### Example 3. Create a Numpy array of constants

# In[ ]:


# We create a 2 x 3 ndarray full of fives. 
X = np.full((2,3), 5) 

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)


# #### Example 4. Create a Numpy array of Identity matrix

# In[ ]:


# We create a 5 x 5 Identity matrix. 
X = np.eye(5)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)  


# #### Example 5. Create a Numpy array of constants

# In[ ]:


# Create a 4 x 4 diagonal matrix that contains the numbers 10,20,30, and 50
# on its main diagonal
X = np.diag([10,20,30,50])

# We print X
print()
print('X = \n', X)
print()


# #### Example 5. Create a Numpy array of evenly spaced values in a given range, using `arange(stop_val)`
# See the complete syntax of `NumPy.arange()` [here](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)

# In[ ]:


# We create a rank 1 ndarray that has sequential integers from 0 to 9
x = np.arange(10)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 


# #### Example 6. Create a Numpy array using `arange(start_val, stop_val)`

# In[ ]:


# We create a rank 1 ndarray that has sequential integers from 4 to 9. 
x = np.arange(4,10)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 


# #### Example 7. Create a Numpy array using `arange(start_val, stop_val, step_size)`

# In[ ]:


# We create a rank 1 ndarray that has evenly spaced integers from 1 to 13 in steps of 3.
x = np.arange(1,14,3)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 


# #### Example 8. Create a Numpy array using `linspace(start, stop, n)`, with `stop` inclusive.
# See the all possible arguments in the syntax [here](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) 

# In[ ]:


# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25.
x = np.linspace(0,25,10)

# We print the ndarray
print()
print('x = \n', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 


# #### Example 9. Create a Numpy array using `linspace(start, stop, n)`, with `stop` excluded.

# In[ ]:


# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25,
# with 25 excluded.
x = np.linspace(0,25,10, endpoint = False)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 


# #### Example 10. Create a Numpy array by feeding the output of `arange()` function to the  `reshape()` function.
# Here, `arange()` function will give you a 1-D array, whereas the `reshape()` function will convert that 1-D array into a  desired shape. **Remember, that the  `size` of the final output must be as same as the `size` of the initial  1-D array.

# In[ ]:


# We create a rank 1 ndarray with sequential integers from 0 to 19
x = np.arange(20)

# We print x
print()
print('Original x = ', x)
print()

# We reshape x into a 4 x 5 ndarray 
x = np.reshape(x, (4,5))

# We print the reshaped x
print()
print('Reshaped x = \n', x)
print()

# We print information about the reshaped x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 


# #### Example 11. Create a Numpy array by calling the `reshape()` function from the output of `arange()` function.
# Notice the change in the arguments of `reshape()`

# In[ ]:


# We create a a rank 1 ndarray with sequential integers from 0 to 19 and
# reshape it to a 4 x 5 array 
Y = np.arange(20).reshape(4, 5)

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype) 


# #### Example 12. Create a rank 2 Numpy array by using the `reshape()` function.

# In[ ]:


# We create a rank 1 ndarray with 10 integers evenly spaced between 0 and 50,
# with 50 excluded. We then reshape it to a 5 x 2 ndarray
X = np.linspace(0,50,10, endpoint=False).reshape(5,2)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)


# #### Example 13. Create a Numpy array using the `numpy.random.random()` function. 

# In[ ]:


# We create a 3 x 3 ndarray with random floats in the half-open interval [0.0, 1.0).
X = np.random.random((3,3))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in x are of type:', X.dtype)


# #### Example 14. Create a Numpy array  using the `numpy.random.randint()` function. 

# In[ ]:


# We create a 3 x 2 ndarray with random integers in the half-open interval [4, 15).
X = np.random.randint(4,15,size=(3,2))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)


# #### Example 15. Create a Numpy array of "Normal" distributed random numbers, using the `numpy.random.normal()` function. 

# In[ ]:


# We create a 1000 x 1000 ndarray of random floats drawn from normal (Gaussian) distribution
# with a mean of zero and a standard deviation of 0.1.
X = np.random.normal(0, 0.1, size=(1000,1000))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
print('The elements in X have a mean of:', X.mean())
print('The maximum value in X is:', X.max())
print('The minimum value in X is:', X.min())
print('X has', (X < 0).sum(), 'negative numbers')
print('X has', (X > 0).sum(), 'positive numbers')


# In[ ]:




