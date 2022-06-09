class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums)-1

        while left <= right :
            mid = (left+right)//2
            if nums[left] == nums[right] == target:
                return [left, right]

            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                if nums[left] != target:
                    left += 1
                if nums[right] != target:
                    right -= 1
        return [-1,-1]