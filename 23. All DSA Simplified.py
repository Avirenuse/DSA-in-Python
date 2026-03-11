# 1. Binary Search
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: l = mid + 1
        else: r = mid - 1
    return -1

# 2. Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 3. Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]: min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 4. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        k, j = arr[i], i - 1
        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k
    return arr

# 5. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    L, R = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    i = j = 0
    res = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]: 
            res.append(L[i]); i += 1
        else: 
            res.append(R[j]); j += 1
    return res + L[i:] + R[j:]

# 6. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1: return arr
    p = arr[len(arr) // 2]
    return quick_sort([x for x in arr if x < p]) + [x for x in arr if x == p] + quick_sort([x for x in arr if x > p])

# 7. Breadth First Search (BFS)
from collections import deque
def bfs(graph, start):
    visited, q, res = {start}, deque([start]), []
    while q:
        v = q.popleft()
        res.append(v)
        for n in graph.get(v, []):
            if n not in visited: 
                visited.add(n)
                q.append(n)
    return res

# 8. Depth First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None: visited = set()
    visited.add(start)
    res = [start]
    for n in graph.get(start, []):
        if n not in visited:
            res.extend(dfs(graph, n, visited))
    return res

# 9. Dijkstra's Algorithm
import heapq
def dijkstra(graph, start):
    dist, q = {n: float('inf') for n in graph}, [(0, start)]
    dist[start] = 0
    while q:
        d, u = heapq.heappop(q)
        if d > dist[u]: continue
        for w, v in graph.get(u, []):
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(q, (d + w, v))
    return dist

# 10. Min Heap (Using Python's built-in heapq for simplicity)
def min_heap_example(arr):
    heapq.heapify(arr)               # O(N) to build heap
    heapq.heappush(arr, 5)           # O(log N) to push
    min_element = heapq.heappop(arr) # O(log N) to pop minimum
    return min_element

# 11. Trie (Prefix Tree)
class Trie:
    def __init__(self): 
        self.root = {}
        
    def insert(self, w):
        n = self.root
        for c in w: n = n.setdefault(c, {})
        n['#'] = True    # Mark end of word
        
    def search(self, w):
        n = self.root
        for c in w:
            if c not in n: return False
            n = n[c]
        return '#' in n

# 12. Dynamic Programming (Fibonacci example - Space Optimized)
def fib_dp(n):
    a, b = 0, 1
    for _ in range(n): 
        a, b = b, a + b
    return a
