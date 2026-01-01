class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            for elem in result[:]:
                copy = elem[:]
                elem.append(num)
                result.append(copy) 

        return result
