"""
5.  NUMPY:
a.	Create a Numpy array filled with all zeros[1d and 2d]
b.	Create a Numpy array filled with all ones[1d and 2d]
c.	Slice elements from index 4 to the end of the array
d.	Slice from the index 3 from the end to index 1 from the end
e.	Write the necessary function to get below output: 
i.	input- arr1 = np.array([[1, 2], [3, 4]]) arr2 = np.array([[10, 20], [30, 40]])
f.	Create a numpy array and find the Sum of All the Elements in the Array
g.	Aggregations: Min, Max, and Everything In Between – 
i.	Write the Python code to print the maximum of 4,12,43.3,19,100
ii.	Check whether your able to find the minimum from the given set of values :: 4,12,43.3,19, "HelloProgramming"
iii.	Write the python code to print the word occurring 1st among these in dict:: "GoodMorning", "Evening", "algorithm", "programming"
h.	SORTING: 
i.	Create a list [[4,3,2],[2,1,4]], convert it to a numpy array and sort it along axis 1.
ii.	Implement a program to take fruits names from array of fruits. To sort the array in alphabetical manner and display their index position.
"""

import numpy as np

# Part a: Create Numpy arrays filled with all zeros
zeros_1d = np.zeros(5)
zeros_2d = np.zeros((3, 4))
print("1D array filled with zeros:", zeros_1d)
print("2D array filled with zeros:\n", zeros_2d)

# Part b: Create Numpy arrays filled with all ones
ones_1d = np.ones(5)
ones_2d = np.ones((3, 4))
print("1D array filled with ones:", ones_1d)
print("2D array filled with ones:\n", ones_2d)

# Part c: Slice elements from index 4 to the end of the array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
sliced_arr = arr[4:]
print("Sliced elements from index 4 to the end:", sliced_arr)

# Part d: Slice from the index 3 from the end to index 1 from the end
sliced_arr_reverse = arr[-3:-1]
print(
    "Sliced elements from index 3 from the end to index 1 from the end:",
    sliced_arr_reverse,
)

# Part e: Element-wise addition of two arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[10, 20], [30, 40]])
result = np.add(arr1, arr2)
print("Element-wise addition of arr1 and arr2:\n", result)

# Part f: Create a numpy array and find the sum of all elements
arr = np.array([1, 2, 3, 4, 5])
sum_of_elements = np.sum(arr)
print("Sum of all elements in the array:", sum_of_elements)

# Part g: Aggregations
# i. Maximum value
max_value = max(4, 12, 43.3, 19, 100)
print("Maximum value:", max_value)

# ii. Minimum value with error handling
values = [4, 12, 43.3, 19, "HelloProgramming"]
try:
    min_value = min(values)
    print("Minimum value:", min_value)
except TypeError as e:
    print("Error:", e)

# iii. First word in dict order
words = ["GoodMorning", "Evening", "algorithm", "programming"]
first_word = min(words)
print("Word occurring 1st in dict order:", first_word)

# Part h: Sorting
# i. Sort along axis 1
lst = [[4, 3, 2], [2, 1, 4]]
np_arr = np.array(lst)
sorted_arr = np.sort(np_arr, axis=0)
print("Sorted array along axis 1:\n", sorted_arr)

# ii. Sort fruits array alphabetically and display index positions
fruits = np.array(["banana", "apple", "cherry", "date"])
sorted_fruits = np.sort(fruits)
sorted_indices = np.argsort(fruits)
print("Sorted fruits:", sorted_fruits)
print("Indices of sorted fruits:", sorted_indices)
