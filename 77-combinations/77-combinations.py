class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combinelist=[]

        def backtrack(remain,ans,i):
            if remain ==0:
                if ans not in combinelist:
                    combinelist.append([int(x) for x in ans[:-1].split(",")])


            else:
                for x in range(i,n+1):
                    backtrack(remain-1,ans+str(x)+",",x+1)

        backtrack(k,"",1)
        return combinelist