class Solution:
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row=len(image)
        col=len(image[0])
        color=image[sr][sc]
        newcolor=newColor
        
        def filler(r,c,color,newcolor):
            print(image)
            if color == newcolor: return image
            if image[r][c] == color:
                image[r][c]=newcolor
                if r-1 >=0:
                    filler(r-1,c,color,newcolor)
                if c-1 >=0:
                    filler(r,c-1,color,newcolor)
                if r+1 < row:      
                    filler(r+1,c,color,newcolor)
                if c+1 < col:
                    filler(r,c+1,color,newcolor)
        
        filler(sr,sc,color,newcolor)
        
        return image
        