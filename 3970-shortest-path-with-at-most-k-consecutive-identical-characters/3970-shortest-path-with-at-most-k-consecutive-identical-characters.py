
import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        
        pq = [(0, 0, labels[0], 1)]

        
        dist = {}

        while pq:
            cost, node, last_char, count = heapq.heappop(pq)

            state = (node, last_char, count)

            if state in dist and dist[state] <= cost:
                continue

            dist[state] = cost

            if node == n - 1:
                return cost

            for nei, weight in graph[node]:
                ch = labels[nei]

                if ch == last_char:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_state = (nei, ch, new_count)
                new_cost = cost + weight

                if new_state not in dist or new_cost < dist[new_state]:
                    heapq.heappush(
                        pq,
                        (new_cost, nei, ch, new_count)
                    )

        return -1
