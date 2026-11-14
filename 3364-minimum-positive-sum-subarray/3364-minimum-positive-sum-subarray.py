class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')

        for i in range(n):
            total = 0

            for j in range(i, min(i + r, n)):
                total += nums[j]

                length = j - i + 1

                if length >= l and total > 0:
                    ans = min(ans, total)

        return ans if ans != float('inf') else -1