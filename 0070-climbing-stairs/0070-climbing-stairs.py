class Solution:
    record = []
    
    def climbStairs(self, n: int) -> int:
        if len(self.record) == 0 :
            self.record = ['n' for x in range(n+1)]
            self.record[0] = 0
            
            
        if n == 1:
            self.record[1] = 1
            return 1
        elif n == 2:
            self.record[2] = 2
            return 2
        
        if self.record[n] == 'n':
            self.record[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.record[n]
        
        else:
            return self.record[n]