from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        n = len(nums)

        pos = {arr[i]: i for i in range(n)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle += 1

            if cycle > 1:
                swaps += cycle - 1

        return swaps