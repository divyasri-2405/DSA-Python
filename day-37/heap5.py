'''#min heap
import heapq
heap=[]
heapq.heappush(heap,30)
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,5)
print(heap)
print("Minimum:",heap[0])
heapq.heappop(heap)
print(heap)

#max heap
import heapq
heap=[]
heapq.heappush(heap,-30)
heapq.heappush(heap,-10)
heapq.heappush(heap,-50)
heapq.heappush(heap,-20)
print([-x for x in heap])
print("Maximum: ",-heap[0])
heapq.heappop(heap)
print([-x for x in heap])'''

#priority heap
import heapq
pq=[]
heapq.heappush(pq,(2,'Followup'))
heapq.heappush(pq,(1,"Emergency"))
heapq.heappush(pq,(3,'consultation'))
while pq:
    priority,task=heapq.heappop(pq)
    print(priority,task)