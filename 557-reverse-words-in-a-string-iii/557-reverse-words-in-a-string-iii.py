class Solution:
    def reverseWords(self, s: str) -> str:
        splitwords = s.split(' ')
        ans = ''
        for x in range(len(splitwords)):
            ans += splitwords[x][::-1]
            ans += " "       
        return ans[:-1]