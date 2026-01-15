class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        res = 0
        while 1 << count <= n:
            if n & (1 << count):
                res += 1

            count += 1

        return res
