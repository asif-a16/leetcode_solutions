class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightt = {}
        leftt = {}

        left = 1
        right = 1
        nums_len = len(nums)

        for idx, num in enumerate(nums):
            leftt[idx] = left
            left *= num

            r_idx = nums_len - idx - 1
            rightt[r_idx] = right
            right *= nums[r_idx]

        return [leftt[i] * rightt[i] for i in range(nums_len)]
