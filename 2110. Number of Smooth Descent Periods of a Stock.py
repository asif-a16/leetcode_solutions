class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        smooth_descent_periods = len(prices)
        
        current_window_size = 2
        
        def isSmooth(l, r):
            while l != r:
                if prices[l] - prices[l + 1] != 1:
                    return False
                l += 1
            return True

        left = 0

        if len(prices) != 1:
            while current_window_size != len(prices):
                for right in range(current_window_size - 1, len(prices)):
                    if isSmooth(left, right):
                        smooth_descent_periods += 1
                    left += 1
                current_window_size += 1
                left = 0

        print(smooth_descent_periods)
        return smooth_descent_periods
    
if __name__ == "__main__":
    Solution.getDescentPeriods(None, [12,11,10,9,8,7,6,5,4,2,1,0])