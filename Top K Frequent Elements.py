class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1

        sorted_freq = sorted(frequencies.items(),
                              key=lambda item: item[1], reverse=True)
        
        res = []
        for i in range(k):
            res.append(sorted_freq[i][0])

        return res
