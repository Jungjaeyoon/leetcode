class Solution:
    fibolist = []
    def fib(self, n: int) -> int:
        if len(self.fibolist) == 0:
            self.fibolist =[0,1]+[0 for x in range(n+1)]
        if n==0: 
            self.fibolist[0] = 0
            return 0
        if n==1: 
            self.fibolist[1] = 1
            return 1
        
        if self.fibolist[n] == 0:
            self.fibolist[n] = self.fib(n-1) + self.fib(n-2)
            return self.fibolist[n]            
        else:
            return self.fibolist[n]