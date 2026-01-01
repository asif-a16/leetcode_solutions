class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def dfs(start, current_sum, path):
            if current_sum == target:
                result.append(path[:])
                return
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, current_sum + candidates[i], path)
                path.pop()

        dfs(0, 0, [])
        return result
