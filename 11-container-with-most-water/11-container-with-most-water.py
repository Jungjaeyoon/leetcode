class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        n = len(height)-1
        left = 0
        right = len(height)-1
        area = min(height[left],height[right])*n
            
        while left < right:             
            if height[left] < height[right]:
                area = max(area, height[left]*n)
                left +=1
                n -=1
                
            else:
                area = max(area, height[right]*n)
                right -=1
                n -=1
        
        return area
                
            