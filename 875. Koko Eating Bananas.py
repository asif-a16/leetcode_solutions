class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        left = math.ceil(sum(piles) / h)
        right = max(piles)

        while left < right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k

            if hours > h:
                left = k + 1
            else:
                right = k

        return left
