class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permute(path: list, candidates: set):
            if not candidates:
                result.append(path[:])

            for num in candidates:
                path.append(num)
                candidates.remove(num)
                permute(path, candidates.copy())
                candidates.add(num)
                path.pop()

        permute([], set(nums))
        return result
