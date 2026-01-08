class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        prev = max(nums[0], nums[1])
        prev_prev = nums[0]

        for i in range(2, len(nums)):
            if nums[i] + prev_prev > prev:
                prev_prev, prev = prev, nums[i] + prev_prev
            else:
                prev_prev = prev
        
        return prev
