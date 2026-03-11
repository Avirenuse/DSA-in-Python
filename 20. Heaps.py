# Min Heap Implementation
# A Min-Heap is a complete binary tree in which the value in each internal node 
# is smaller than or equal to the values in the children of that node.
# Time Complexity: Insertion - O(log n), Deletion - O(log n), Get Min - O(1)
# Space Complexity: O(n)

class MinHeap:
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        return (i - 1) // 2
        
    def left_child(self, i):
        return 2 * i + 1
        
    def right_child(self, i):
        return 2 * i + 2
        
    def insert(self, key):
        # Insert the new key at the end
        self.heap.append(key)
        
        # Keep swapping with parent until heap property is restored
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
            
    def min_heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        smallest = i
        
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
            
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
            
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)
            
    def extract_min(self):
        if len(self.heap) <= 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
            
        # Store the minimum value, and remove it from heap
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.min_heapify(0)
        
        return root
        
    def get_min(self):
        return self.heap[0] if self.heap else None

if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(3)
    heap.insert(2)
    heap.insert(15)
    heap.insert(5)
    heap.insert(4)
    heap.insert(45)
    
    print("Min Heap array representation:", heap.heap)
    print("Extracted Min:", heap.extract_min())
    print("Heap after extraction:", heap.heap)
    print("New Min:", heap.get_min())
