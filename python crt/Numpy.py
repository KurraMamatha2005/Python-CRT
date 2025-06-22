import numpy as np
print(np.__version__)
# creating an array object
Arr1=np.array([1,2,3,4,5,6,7])
print(Arr1)
print(type(Arr1))
#dimensions of array: one level of array depth
#one level array dimension
array1=np.array([10,20,30,40])
print(array1)
print(type(array1))
print(array1.ndim)
# two dimensional array
array2=np.array([[10,20],[30,40],[50,60]])
print(array2)
print(type(array2))
print(array2.ndim)
# three dimesionalarray
array3=np.array([[[10,20,30],[40,50,60],[70,80,90]]])
print(array3)
print(type(array3))
print(array3.ndim)
#acessing elements from arrray
array=np.array([[1,2,3],[10,20,30],[40,50,60]])
print(array[0][0])
print(array[0][1])
print(array[0][2])
print(array[1][0])
print(array[1][1])
print(array[1][2])
print(array[2][0])
print(array[2][1])
print(array[2][2])

"""write a python programm to create  matrix with 4 rows and 4 columns using numpy library and give only multiples of 5"""

import numpy as np

# Generate the first 16 multiples of 5 (5 to 80)
multiples_of_5 = np.arange(5, 5 * 16 + 1, 5)

# Reshape into a 4x4 matrix
matrix = multiples_of_5.reshape(4, 4)

# Display the matrix
print("4x4 Matrix with multiples of 5:")
print(matrix)

#acessing 3d array
import numpy as np
ar = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(ar[0,1,2])
print(ar[1,1,2])

#array slicing
#array [start:end:stepsize]
import numpy as np
a=np.array([1,2,3,4,5,6,7])
           #0 1 2 3 4 5 6  
print(a[1:5])
print(a[2:4])
#negative slicing
import numpy as np
r= np.array([1,2,3,4,5,6,7])
print(r[-3:-1])
#2d slicing
import numpy as np
rt=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(rt[1,1:4])#in[6,7,8,9,10] line slice 1:4

#view
import numpy as np
arrr=np.array([1,2,3,4,5])
x=arrr.view()
arrr[0]=42
print(arrr)
print(x)

import numpy as np
arrr=np.array([1,2,3,4,5])
x=arrr.copy()
arrr[0]=42
print(arrr)
print(x)

#copy jst copies the ellement but view modifies the original element

#array shape and reshape
#array shape
import numpy as np
s=np.array([[1,2,3,4],[5,6,7,8]])
print(s.shape)
#array reshape
import numpy as np
sh=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newsh=sh.reshape(4,3)
print(newsh)

#conversion from 1d to 3d
import numpy as np
t=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newt=t.reshape(2,3,2)#2rows 3 columns and 2 elements in each
print(newt)

"""write pp to create a 1d array with 15 elements and reshape it into 2d array with 3rows and 5 columns 
ii) 5 rows and 3 colums print the dimension of it
reshape the same array into a three dimensional array with 5 rows and 3 colums with one element in each coloumn"""

import numpy as np
f= np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
newf=f.reshape(3,5)
newwf=f.reshape(5,3)
print("3 rows 5 colums")
print(newf)
print("5 rows 3 columns")
print(newwf)
nww=f.reshape(5,3,1)#5 rows and 3 colums with one element in each
print(nww)

# array iteration in 1d
import numpy as np
arr=np.array([1,2,3])
for x in arr:
    print(x)
# array iteration in 2d
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)

#array iteration 3d
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    print(x)
#slicing
#array iteration 3d
import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1:])

#concatination
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)

#joining 2 strings
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
arr=np.concatenate((arr1,arr2),axis=1)#horizontal concatenztion
print(arr)

#joining two array 2d
import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
arr=np.concatenate((arr1,arr2),axis=0)#verticall conctenation
print(arr)

#splitting arrays
import numpy as np
arr= np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print("original array:",arr)
print("splitted array:",newarr)
print("....................................")
#splitiing 2d array
import numpy as np
g=np.array([[1,2],[3,4],[5,6],[7,8],[9,1]])
newg=np.array_split(g,3)
print("original array:",g)
print("splitted array:",newg)

#searching array:where method used
import numpy as np
arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr==4)
print(x)

#finding indexes are even
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
x=np.where(arr%2==0)
print(x)








