class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
    
        c = len(isConnected)
        cn = len(isConnected[0])
        cnt = 0 
        passlist = []
            
        def checker(x):
            connectedCity = [ z for z,y in enumerate(isConnected[x]) if y != 0]
            for pos in connectedCity:
                isConnected[x][pos] = 0 
                passlist.append(pos)
                checker(pos)



        for x in range(c):
            if x not in passlist:
                if sum(isConnected[x]) > 0:
                    cnt+=1
                checker(x)
            
        return cnt