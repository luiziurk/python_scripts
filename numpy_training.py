#%%
import time
from matplotlib.pyplot import spring
import numpy as np
import pandas as pd

#%%

x = np.random.random(100000000)

# Case 1
start = time.time()
sum(x) / len(x)
print(time.time() - start)

# Case 2
start = time.time()
np.mean(x)
print(time.time() - start)

#%%

x = np.array([1,2,3,4,5])

print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a rank 1 ndarray from a Python list that contains integers and strings
y = np.array([1, 2, 'World'])

# We print information about x
print('y = ', y)
print('y has dimensions:', y.shape)
print('y is an object of type:', type(y))
print('The elements in y are of type:', y.dtype)


# %%

# Exercise 1

""" Create a numpy array of strings containing letters 'a' through 'j' (inclusive) of the alphabet. Then, use numpy array attributes to print the following information about this array:

dtype of array
shape of array
size of array """

import string as st

alphabet  = st.ascii_lowercase.split()[0][:10]

letters_list = [char for char in alphabet]

letter_array = np.array(letters_list)

print("Letter Array", letter_array )

print("Array Data Type  = ", letter_array.dtype)
print("Array Data Shape  = ",letter_array.shape)
print("Array Data Size  = ",letter_array.size)


# %%
x = np.zeros((4,3), dtype = int64)
y = np.eye(5)
z = np.arange(10)
k = np.linspace(0 ,25, 10, endpoint= False).reshape(5,2)


t = np.random.random((3,3))
u = np.random.randint(4, 15, (3, 2))

f = np.random.normal(0, 0.1, size = (1000,1000) )
print(f.mean())


# %%
# We create a rank 1 ndarray 
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print x
print()
print('Original x = ', x)

# We delete the first and last element of x
x = np.delete(x, [0,4])

# We print x with the first and last element deleted
print()
print('Modified x = ', x)
#%%

x = np.arange(1, 26).reshape(5,5)
x[x%2 != 0]

#%%

# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc.. 

X = np.ones(shape=(4,4))
y = np.array([1,2,3,4])
z = np.arange(1,5)

