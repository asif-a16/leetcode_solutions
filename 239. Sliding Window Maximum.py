class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return [max(nums)]
        
        left = 1
        max_num = 0
        result = []

        for right, num in enumerate(nums):
            if right < k - 1:
                max_num = max(max_num, num)
                continue
            elif right == k - 1:
                result.append(max(max_num, num))
                continue

            max_num = float("-inf")
            for i in range(left, right + 1):
                max_num = max(max_num, nums[i])
                
            result.append(max_num)
            left += 1

        return result
