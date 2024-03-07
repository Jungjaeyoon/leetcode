class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximumwealth = 0
        for customer in accounts:
            if maximumwealth <= sum(customer):
                maximumwealth = sum(customer)
        
        return maximumwealth