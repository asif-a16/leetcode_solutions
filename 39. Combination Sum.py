class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, builder):
            if i > len(candidates):
                if sum(builder)  == target:
                    result.append(builder[:])
                return
            
            builder_sum = sum(builder)
            if builder_sum == target:
                result.append(builder[:])
                return
            
            if builder_sum > target:
                return
            
            if builder_sum + candidates[i] < target:
                dfs(i, builder.append(candidates[i]))

            dfs(i + 1, builder.append(candidates[i]))
            dfs(i + 1, builder)

        dfs(0, [])

        return result
