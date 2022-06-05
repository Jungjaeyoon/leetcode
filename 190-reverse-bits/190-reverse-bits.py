class Solution:
    def reverseBits(self, n: int) -> int:
        a = '0'*(32-len(bin(n)[2:])) + bin(n)[2:]

        return int(a[::-1],2)