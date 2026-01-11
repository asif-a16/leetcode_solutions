class Solution:
    def maxProdSearch(self, nums: List[int]) -> int:
        max_found = nums[0]
        previous_negative_subarray = None
        current_subarray = 1

        for num in nums:
            if num == 0:
                max_found = max(max_found, 0)
                current_subarray = 1
                previous_negative_subarray = None
                continue

            if num < 0:
                if previous_negative_subarray:
                    current_subarray *= previous_negative_subarray * num
                    previous_negative_subarray = None
                    max_found = max(max_found, current_subarray)
                else:
                    previous_negative_subarray = current_subarray * num
                    current_subarray = 1
                continue

            current_subarray *= num
            max_found = max(max_found, current_subarray)
        
        return max_found

    def maxProduct(self, nums: List[int]) -> int:
        return max(self.maxProdSearch(nums), 
                   self.maxProdSearch(nums[::-1]))
