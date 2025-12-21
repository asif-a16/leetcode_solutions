class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        res = 10**18

        while left <= right:
            pivot = left + int((right - left) / 2)
            res = min(nums[left], res)

            if nums[right] < nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1

        return res
