# Selection Sort Algorithm
# Sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning.
# Time Complexity: O(n^2) for all cases
# Space Complexity: O(1)

def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element of unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    sorted_arr = selection_sort(arr.copy())
    print("Sorted array:", sorted_arr)
