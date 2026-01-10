import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                prod = math.prod(nums[i:j+1])
                cur_max = max(cur_max, prod)

        return cur_max
