class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for factor, price in items)
        max_factor = max(factor for factor, price in items)

        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        gain = freq[:]

        for i in range(1, max_factor + 1):
            for j in range(2 * i, max_factor + 1, i):
                gain[i] += freq[j]

        candidates = []

        for factor, price in items:
            count = gain[factor] - 1

            if count > 0 and price < 2 * min_price:
                candidates.append((price, count))

        candidates.sort()

        ans = 0

        for price, count in candidates:
            take = min(count, budget // price)
            ans += 2 * take
            budget -= take * price

        ans += budget // min_price

        return ans