class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        ans = ['null' for x in cost]
        
        def minStep(s):
            if s == 0:
                return cost[0]
            if s == 1:
                return cost[1]    
            
            if ans[s] == 'null':
                ans[s] = min(minStep(s-1), minStep(s-2)) + cost[s]
            return ans[s]
        
        return minStep(len(cost)-1)