class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        minval=0
        maxval=len(nums)-1

        sortedlist=[0]*len(nums)

        for x in range(len(nums)-1,-1,-1):
            if nums[minval]**2 < nums[maxval]**2:
                sortedlist[x] = nums[maxval]**2
                maxval -= 1
            else:
                sortedlist[x] = nums[minval] **2
                minval += 1
        return sortedlist