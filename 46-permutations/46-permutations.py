class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution=[]

        def permutation(num,ans,remain):
            if remain ==0:
                solution.append(ans)
            else:

                for x in num:
                    newans=ans+[x]
                    newnum=[ n for n in num if n is not x]
                    permutation(newnum,newans,remain-1)


        permutation(nums,[],len(nums))
        return solution