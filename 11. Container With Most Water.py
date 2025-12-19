class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        n = len(height)

        left = 0
        right = n-1
        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            best = max(best, area)

            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return best
