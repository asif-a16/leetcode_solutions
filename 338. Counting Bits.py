class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        current_highest_power_of_two = None

        for num in range(1, n + 1):
            if not num & (num - 1):
                current_highest_power_of_two = num
                result[num] = 1
            else:
                result[num] = 1 + result[num - current_highest_power_of_two]

        return result
