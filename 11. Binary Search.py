# Binary Search Algorithm
# Used to search a sorted array by repeatedly dividing the search interval in half.
# Time Complexity: O(log n)
# Space Complexity: O(1) for iterative, O(log n) for recursive

def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1
            
    return -1

def binary_search_recursive(arr, target, left, right):
    if left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, right)
        else:
            return binary_search_recursive(arr, target, left, mid - 1)
            
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    
    # Iterative
    result_idx = binary_search_iterative(arr, target)
    print(f"Iterative: Element found at index {result_idx}" if result_idx != -1 else "Element not found")
    
    # Recursive
    result_idx_rec = binary_search_recursive(arr, target, 0, len(arr) - 1)
    print(f"Recursive: Element found at index {result_idx_rec}" if result_idx_rec != -1 else "Element not found")
