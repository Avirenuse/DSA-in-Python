# Quick Sort Algorithm
# A divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
# Time Complexity: O(n log n) average case, O(n^2) worst case
# Space Complexity: O(log n)

def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)
        
        # Separately sort elements before partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def quick_sort_pythonic(arr):
    """A more pythonic way to write quicksort (uses more space O(n))"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_pythonic(left) + middle + quick_sort_pythonic(right)

if __name__ == "__main__":
    # Standard Quick Sort (In-place)
    arr1 = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr1)
    quick_sort(arr1, 0, len(arr1) - 1)
    print("Sorted array (In-place):", arr1)
    
    # Pythonic Quick Sort
    arr2 = [10, 7, 8, 9, 1, 5]
    sorted_arr2 = quick_sort_pythonic(arr2)
    print("Sorted array (Pythonic):", sorted_arr2)
