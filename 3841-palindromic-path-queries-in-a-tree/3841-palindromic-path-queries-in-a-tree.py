
from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        chars = list(s)
        tin = [0] * n
        tout = [0] * n
        parent = [0] * n
        depth = [0] * n
        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()
            if state == 0:
                parent[u] = p if p != -1 else u
                tin[u] = timer
                timer += 1
                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        LOG = n.bit_length()
        up = [parent[:]]
        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        class Fenwick:
            def __init__(self, size):
                self.size = size
                self.bit = [0] * (size + 1)

            def add(self, i, value):
                while i <= self.size:
                    self.bit[i] ^= value
                    i += i & -i

            def update(self, left, right, value):
                self.add(left + 1, value)
                self.add(right + 2, value)

            def query(self, i):
                i += 1
                result = 0
                while i > 0:
                    result ^= self.bit[i]
                    i -= i & -i
                return result

        bit = Fenwick(n + 1)

        for u in range(n):
            mask = 1 << (ord(chars[u]) - 97)
            bit.update(tin[u], tout[u] - 1, mask)

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                if chars[u] != c:
                    delta = (1 << (ord(chars[u]) - 97)) ^ (1 << (ord(c) - 97))
                    chars[u] = c
                    bit.update(tin[u], tout[u] - 1, delta)
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                mask = bit.query(tin[u]) ^ bit.query(tin[v]) ^ (1 << (ord(chars[w]) - 97))
                ans.append((mask & (mask - 1)) == 0)

        return ans
