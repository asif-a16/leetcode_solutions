class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for num in range(1, n + 1):
            result[num] = 1 + result[num & (num - 1)]

        return result
