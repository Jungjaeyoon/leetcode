class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def backspacecal(s):
            ans = ""
            size = len(s)
            p = 0
            while p <= size-1:
                if s[p] != "#":
                    ans += s[p]
                    p +=1

                elif s[p] == "#":
                    bs = p
                    if bs == p-1:
                        p +=1
                    else:
                        ans = ans[:-1]
                        p +=1
            return ans
        return backspacecal(s) == backspacecal(t)