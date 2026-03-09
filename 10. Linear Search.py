'''Linear Search
Linear search (or sequential search) is the simplest search algorithm. It checks each element one by one.

This algorithm is very simple and easy to understand and implement.

How it works:

Go through the array value by value from the start.
Compare each value to check if it is equal to the value we are looking for.
If the value is found, return the index of that value.
If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.
If the array is already sorted, it is better to use the much faster Binary Search algorithm that we will explore on the next page.'''

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]

if 4 in mylist:
  print("Found!")
else:
  print("Not found!")

#But if you need to find the index of a value, you will need to implement a linear search: 

def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4

result = linearSearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")