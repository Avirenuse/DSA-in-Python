# Merge Sort Algorithm
# A divide and conquer algorithm that divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.
# Time Complexity: O(n log n) in all cases
# Space Complexity: O(n)

def merge_sort(arr):
    if len(arr) > 1:
        # Find the mid of the array
        mid = len(arr) // 2
        
        # Dividing the array elements
        L = arr[:mid]
        R = arr[mid:]
        
        # Sorting the first half
        merge_sort(L)
        
        # Sorting the second half
        merge_sort(R)
        
        i = j = k = 0
        
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    
    # Note: merge_sort sorts in-place as it modifies the array passed
    arr_copy = arr.copy()
    merge_sort(arr_copy)
    
    print("Sorted array:", arr_copy)
