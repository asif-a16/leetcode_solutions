class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for shift_amount in range(32):
            bit = (n >> shift_amount) & 1
            res |= bit << (31 - shift_amount)

        return res
