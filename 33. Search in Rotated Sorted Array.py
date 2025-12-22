class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot = left + int((right - left) / 2)
            if nums[pivot] == target:
                return pivot
            if nums[left] <= nums[pivot]:
                if target > nums[pivot] or target < nums[left]:
                    left  = pivot + 1
                else:
                    right = pivot - 1
            else:
                if target < nums[pivot] or target > nums[right]:
                    right = pivot - 1
                else:
                    left = pivot + 1

        return -1
