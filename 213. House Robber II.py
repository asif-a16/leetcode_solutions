class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        prev, prev_prev = 0, 0

        for num in nums:
            prev_prev, prev = prev, max(prev_prev + num, prev)

        result1 = prev_prev

        prev, prev_prev = 0, 0

        for i in range(1, len(nums)):
            prev_prev, prev = prev, max(prev_prev + nums[i], prev)

        return max(result1, prev)
