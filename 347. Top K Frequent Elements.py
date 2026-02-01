class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequencies = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, frequency in counts.items():
            frequencies[frequency].append(num)

        result = []

        for i in range(len(nums), -1, -1):
            for num in frequencies[i]:
                result.append(num)
                if len(result) == k:
                    return result
