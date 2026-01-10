class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        reachable_bits = 1 << amount
        coins_used = 0

        while (reachable_bits & 1) == 0:
            next_reachable_bits = 0

            for coin in coins:
                next_reachable_bits |= reachable_bits >> coin

            if next_reachable_bits == reachable_bits:
                return -1
            
            coins_used += 1
            reachable_bits = next_reachable_bits

        return coins_used
