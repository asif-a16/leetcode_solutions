class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n_len = len(nums)
        res = set()

        for i in range(n_len):
            pivot = -nums[i]
            left = 0
            right = n_len - 1
            while left < right:
                if nums[left] + nums[right] < pivot or left == i:
                    left += 1
                elif nums[left] + nums[right] > pivot or right == i:
                    right -= 1
                elif nums[left] + nums[right] == pivot:
                    res.add(tuple(sorted([nums[i], nums[left], nums[right]])))
                    left += 1
                    right -= 1
    
        return list(res)
