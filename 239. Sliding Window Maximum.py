from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return [max(nums)]
        
        left = 0
        max_num = 0
        result = []
        window = SortedList()

        for right, num in enumerate(nums):
            if right < k - 1:
                window.add(num)
                continue
            elif right == k - 1:
                window.add(num)
                result.append(window[-1])
                continue
            
            window.remove(nums[left])
            window.add(num)
            left += 1

            max_num = window[-1]
                
            result.append(max_num)
            
        return result
