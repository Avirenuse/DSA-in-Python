# Insertion Sort Algorithm
# Builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
# Time Complexity: O(n^2) worst/average case, O(n) best case
# Space Complexity: O(1)

def insertion_sort(arr):
    # Traverse from 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1], that are greater than key, definition of insertion sort
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
    return arr

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    sorted_arr = insertion_sort(arr.copy())
    print("Sorted array:", sorted_arr)
