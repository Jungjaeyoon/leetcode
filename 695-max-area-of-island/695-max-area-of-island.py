class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sizelist=[0]
        checked = []
        checklist=[]
        row = len(grid)
        col = len(grid[0])
     
        maxsize = 0
        
        
        def area(r,c,size):
            
            if grid[r][c] == 1 and [r,c] not in checked:
                if [r,c] not in checklist:
                    checklist.append([r,c])
                
                if size not in sizelist:
                    sizelist.append(size)
                checked.append([r,c])
                if r-1 >=0:
                    area(r-1,c,size)
                if c-1 >=0:
                    area(r,c-1,size)
                if r <= row-2:      
                    area(r+1,c,size)
                if c <= col-2:
                    area(r,c+1,size)
            else:
                if 0 not in sizelist:
                    sizelist.append(0)
                
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
               
                area(i,j,0)
                
                maxsize = max(maxsize,len(checklist))
                checklist=[]
             
                   
        
      
   
        return maxsize