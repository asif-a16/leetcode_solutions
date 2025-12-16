class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        uncontiguous_idxs = [0]
        prices_length = len(prices)
        smooth_descent_periods = 0

        if prices_length != 1:
            for i in range(1, prices_length):
                if prices[i-1] - prices[i] != 1:
                    uncontiguous_idxs.append(i)

        uncontiguous_idxs.append(prices_length)

        for i in range(1, len(uncontiguous_idxs)):
            smooth_range = uncontiguous_idxs[i] - uncontiguous_idxs[i-1]
            smooth_descent_periods += 0.5 * smooth_range * (smooth_range + 1)

        return int(smooth_descent_periods)
