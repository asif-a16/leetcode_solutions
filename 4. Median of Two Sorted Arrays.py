class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        half_total = total_len // 2
        a = nums1
        b = nums2

        if len(b) < len(a):
            a, b = b, a

        left = 0
        right = len(a) - 1

        while True:
            a_pivot = (left + right) // 2
            b_pivot = half_total - a_pivot - 2

            a_left = a[a_pivot] if a_pivot >= 0 else float("-infinity")
            a_right = a[a_pivot + 1] if (a_pivot + 1) < len(a) else float("infinity")

            b_left = b[b_pivot] if b_pivot >= 0 else float("-infinity")
            b_right = b[b_pivot + 1] if (b_pivot + 1) < len(b) else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                if total_len % 2:
                    return min(a_right, b_right)
                return (min(a_right, b_right) + max(a_left, b_left)) / 2
            elif a_left > b_right:
                right = a_pivot - 1
            else:
                left = a_pivot + 1
