
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        last = {}
        ans = 0

        def apply(node, l, r, val):
            length = r - l + 1
            tree[node] = (tree[node] + 2 * val * lazy_sum[node] + val * val * length) % MOD
            lazy[node] += val
            lazy[node] %= MOD
            lazy_sum[node] = (lazy_sum[node] + val * length) % MOD

        lazy_sum = [0] * (4 * n)

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return
            mid = (l + r) // 2
            apply(node * 2, l, mid, lazy[node])
            apply(node * 2 + 1, mid + 1, r, lazy[node])
            lazy[node] = 0

        def update(node, l, r, ql, qr, val):
            if ql <= l and r <= qr:
                apply(node, l, r, val)
                return
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr, val)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, val)
            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD
            lazy_sum[node] = (lazy_sum[node * 2] + lazy_sum[node * 2 + 1]) % MOD

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i, 1)
            ans = (ans + tree[1]) % MOD
            last[x] = i

        return ans
