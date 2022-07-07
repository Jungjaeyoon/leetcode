class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slist= [x for x in s]
        p = sorted(p)
        output=[]
        
        for x in range(len(s)-len(p)+1):
            if slist[x] in p:
                if p == sorted(slist[x:x+len(p)]):
                    output.append(x)
                else:
                    pass
            else:
                pass
        return output
            