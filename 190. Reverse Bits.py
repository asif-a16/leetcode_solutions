class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for left_shift_amount in range (32):
            result = (result << 1) | bool(n & (1 << left_shift_amount))

        return result
