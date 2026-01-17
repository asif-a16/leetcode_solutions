class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        complete_sum_to_n = 0.5 * n * (n+1)
        return int(complete_sum_to_n - sum(nums))
