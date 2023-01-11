class Solution:
    tribo_list = []
    
    def tribonacci(self, n: int) -> int:
        if len(self.tribo_list) == 0:
            self.tribo_list = [ 'null' for x in range(n+1)]
            self.tribo_list[0] = 0 
            if n >=1:
                self.tribo_list[1] = 1
            elif n >=2:
                self.tribo_list[2] = 1
            
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        if self.tribo_list[n] == 'null':     
            self.tribo_list[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
            return self.tribo_list[n]
        else:
            return self.tribo_list[n]