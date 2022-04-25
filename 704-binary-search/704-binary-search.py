class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = 0 
        
        while high >= low:    
            mid = ( high + low ) // 2
            if target == nums[mid]:
                return mid
    
            elif target < nums[mid]:
                high = mid-1
            elif target > nums[mid]:
                low = mid+1
        return -1
      