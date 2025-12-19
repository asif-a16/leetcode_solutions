class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n_len = len(nums)
        res = []
        for i in range(n_len):
            for j in range(i + 1, n_len):
                for k in range(j+1, n_len):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sort_res = sorted([nums[i], nums[j], nums[k]])
                        if not(sort_res in res):
                            res.append(sort_res)

        return res
