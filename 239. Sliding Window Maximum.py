from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return [max(nums)]
        
        left = 0
        window = deque()
        result = []

        for right, num in enumerate(nums):
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(right)
            if left > window[0]:
                window.popleft()
            if right + 1 >= k:
                result.append(nums[window[0]])
                left += 1
        
        return result
