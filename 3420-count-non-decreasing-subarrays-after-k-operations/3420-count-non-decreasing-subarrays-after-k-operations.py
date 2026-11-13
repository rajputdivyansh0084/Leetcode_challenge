class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        LOG = n.bit_length()

        nxt = [n] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                nxt[stack.pop()] = i
            stack.append(i)

        up = [nxt]
        sm = [[nums[i] * (nxt[i] - i) for i in range(n)]]

        for j in range(1, LOG):
            p = up[-1]
            s = sm[-1]

            nu = [n] * n
            ns = [0] * n

            for i in range(n):
                mid = p[i]
                if mid < n:
                    nu[i] = p[mid]
                    ns[i] = s[i] + s[mid]

            up.append(nu)
            sm.append(ns)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def get_cost(l, r):
            cur = l
            total = 0

            for j in range(LOG - 1, -1, -1):
                nxt_pos = up[j][cur]

                if nxt_pos <= r:
                    total += sm[j][cur]
                    cur = nxt_pos

            total += nums[cur] * (r - cur + 1)

            return total - (prefix[r + 1] - prefix[l])

        ans = 0
        left = 0

        for right in range(n):
            while left <= right and get_cost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans