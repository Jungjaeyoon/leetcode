class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = ['null' for x in nums]
        
        
        
        def dp(n):
            if n == 0:
                ans[0] = nums[0]
                return nums[0]
            if n == 1:
                ans[1] = nums[1]
                return nums[1]
            if n == 2:
                ans[2] = nums[0]+nums[2]
                return nums[0]+nums[2]
            
            if ans[n] == 'null':
                ans[n] = max(dp(n-2),dp(n-3)) + nums[n] 
            return ans[n]
        
        return max(dp(len(nums)-1),dp(len(nums)-2))