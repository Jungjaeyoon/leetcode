class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        ans = []

        while p1 <len(firstList) and p2 < len(secondList):
            p1_s = firstList[p1][0]
            p1_e = firstList[p1][1]
            p2_s = secondList[p2][0]
            p2_e = secondList[p2][1]

            if p1_s <= p2_e and p2_s <= p1_e:
                ans.append([max(p1_s,p2_s),min(p2_e,p1_e)])

            if p1_e >= p2_e:
                p2 +=1
            else:
                p1 +=1
        return ans
    
    
    
            