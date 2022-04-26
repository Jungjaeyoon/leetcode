class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while right - left > 1 :
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        
        if nums[right] < target:
            return right+1
        elif target <= nums[right] and target > nums[left]:
            return right
        else:
            return left