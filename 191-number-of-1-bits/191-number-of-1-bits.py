class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n)
        return sum([int(x) for x in bin(n)[2:]])
    
    
    
    