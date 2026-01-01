class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()

        combinations_for_sum = [[] for _ in range(target + 1)]
        combinations_for_sum[0] = [[]]

        for candidate in candidates:
            for current_sum in range(candidate, target + 1):
                remaining_sum = current_sum - candidate

                for previous_combination in combinations_for_sum[remaining_sum]:
                    new_combination = previous_combination + [candidate]
                    combinations_for_sum[current_sum].append(new_combination)

        return combinations_for_sum[target]
