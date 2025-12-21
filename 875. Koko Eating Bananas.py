class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        lower_k = math.ceil(sum(piles) / h)
        upper_k = max(piles)
        best_k = -1
        best_distance_to_h = 10**18

        while lower_k <= upper_k:
            k = lower_k + int((upper_k - lower_k) / 2)
            new_h = 0
            for num in piles:
                new_h += math.ceil(num / k)
            
            distance_to_h = abs(h - new_h)
            if distance_to_h <= best_distance_to_h and new_h <= h:
                best_k = k
                best_distance_to_h = distance_to_h

            if new_h > h:
                lower_k = k + 1
            else:
                upper_k = k - 1

        return best_k
