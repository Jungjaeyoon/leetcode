# 단순 풀이


## 리스트 1번째 값부터 해당 값이 나올때 까지 비교
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        score = 0
        for x in nums:
            if x == target:
                return score
            else:    score += 1
        return -1
​```


## binary search 

1. 중앙값과 타깃 비교
2. 중앙값 기준 좌 우로 나누어 중앙값> 타깃 일경우 좌측, 반대는 우측의 중앙값과 타깃 비교
반복하여 타깃 검출


'''
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
'''