import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        request_count = [0] * k
        available = SortedList(range(k))
        busy = []
        
        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
                
            if not available:
                continue
                
            target = i % k
            idx = available.bisect_left(target)
            
            if idx == len(available):
                idx = 0
                
            chosen_server = available.pop(idx)
            request_count[chosen_server] += 1
            heapq.heappush(busy, (start + duration, chosen_server))
            
        max_requests = max(request_count)
        return [server_id for server_id, count in enumerate(request_count) if count == max_requests]
