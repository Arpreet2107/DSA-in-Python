 # Heaps / priority queue demo
import heapq

arr = [5,1,3,2]
heap = []
for x in arr:
    heapq.heappush(heap, x)
    print("Heap pop sequence:", [heapq.heappop(heap) for _ in range(len(arr))])