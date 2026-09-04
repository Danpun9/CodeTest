import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = [False] * len(operations)
    
    for i, op in enumerate(operations):
        cmd, num_str = op.split()
        num = int(num_str)
        
        if cmd == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
            
        elif cmd == 'D':
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                    
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
                    
            elif num == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if not min_heap or not max_heap:
        return [0, 0]
        
    return [-max_heap[0][0], min_heap[0][0]]