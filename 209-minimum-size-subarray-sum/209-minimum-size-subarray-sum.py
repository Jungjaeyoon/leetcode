class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        ans = 0
        maxright = len(nums)
        subsum = 0 
        while left <=right:
            

            if subsum < target and right == maxright:
                break
            elif subsum < target:
                subsum += nums[right]
                right +=1
            elif subsum >= target:
                if ans == 0:
                    ans = len(nums[left:right])
                else:
                    ans = min(ans,len(nums[left:right]))
                subsum -= nums[left]
                left +=1
        return ans
