class Solution(object):
    def rob(self, nums):
        prev, prev_prev = 0, 0

        for num in nums:
            prev_prev, prev = prev, max(num + prev_prev, prev)
        
        return prev
