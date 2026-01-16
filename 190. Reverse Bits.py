class Solution:
    def reverseBits(self, n: int) -> int:
        count = 0
        bits = []
        for _ in range (32):
            if n & (1 << count):
                bits.append(1)
            else:
                bits.append(0)
            count += 1

        result = 0
        for bit in bits:
            result = (result << 1) | bit

        return result
