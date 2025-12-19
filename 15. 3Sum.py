class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n_len = len(nums)
        res = set()
        sett = {}

        for i in range(n_len):
            pivot = -nums[i]
            for j in range(i+1, n_len):
                if pivot - nums[j] in sett:
                    k = sett[pivot - nums[j]]
                    sorted_ans = tuple(sorted([nums[i], nums[k], nums[j]]))
                    if i != k and k != j and i != j:
                        res.add(tuple(sorted_ans))
                    continue
                sett[nums[j]] = j
    
        return list(res)
