class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        coins = sorted(coins, reverse=True)
        memo = {}

        for coin in coins:
            memo[coin] = 1

        def dp(s_amount: int):
            if s_amount in memo:
                return memo[s_amount]
            
            for coin in coins:
                if coin > s_amount:
                    continue

                change = dp(s_amount - coin)

                if change == 0:
                    continue
                if (s_amount in memo and memo[s_amount] > change + 1 or 
                    s_amount not in memo):
                    memo[s_amount] = change + 1
            
            if s_amount in memo:
                return memo[s_amount]
            
            memo[s_amount] = 0
            return 0
        
        dp(amount)
        return memo[amount] if memo[amount] else -1
