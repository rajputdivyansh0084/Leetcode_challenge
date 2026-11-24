from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            p = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]
                p *= x
                g = gcd(g, x)
                l = lcm(l, x)

                if p == g * l:
                    ans = max(ans, j - i + 1)

        return ans