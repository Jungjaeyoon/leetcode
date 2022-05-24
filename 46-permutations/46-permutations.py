class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solution=[]

        def permutation(num,ans,remain):
            if remain ==0:
                solution.append(ans)
            else:

                for x in range(len(num)):
                    newans=ans+[num[x]]
                    newnum=num[:x]+num[x+1:]
                    permutation(newnum,newans,remain-1)


        permutation(nums,[],len(nums))
        return solution