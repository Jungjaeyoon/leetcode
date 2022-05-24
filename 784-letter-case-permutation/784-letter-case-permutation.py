class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letterposition =[x for x in range(len(s)) if not s[x].isdigit()]
        solution=[]

        def backtrack(ans,remain):
            if remain ==0:
                if ans not in solution:
                    solution.append(ans)
            else:
                if remain-1 not in letterposition:
                    backtrack(ans+s[len(s)-remain],remain-1)

                backtrack(ans+s[len(s)-remain].upper(),remain-1)
                backtrack(ans+s[len(s)-remain].lower(),remain-1)



        backtrack("",len(s))
        return solution
