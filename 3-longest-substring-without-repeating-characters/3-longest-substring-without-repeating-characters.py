class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        ptrn=[]
        for x in s:
            if x not in ptrn:
                ptrn.append(x)
                maxlen = max(maxlen,len(ptrn))
            elif x in ptrn:
                maxlen = max(maxlen,len(ptrn))

                dupos=0
                for s in ptrn:
                    if x != s:
                        dupos +=1
                    else:
                        break
                ptrn=ptrn[dupos+1:]
                ptrn.append(x)
        return maxlen