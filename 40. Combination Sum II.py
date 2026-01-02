class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(i: int, current_sum: int, path: List[int]):
            if current_sum == target:
                result.append(path[:])
                return
            
            if current_sum > target or i >= len(candidates):
                return
            
            path.append(candidates[i])
            dfs(i + 1, current_sum + candidates[i], path)
            path.pop()

            while (i + 1 < len(candidates) and 
                   candidates[i] == candidates[i + 1]):
                i += 1

            if (i + 1 < len(candidates) and 
                current_sum + candidates[i + 1] > target):
                return
            
            dfs(i + 1, current_sum, path)

        dfs(0, 0, [])
        return result
