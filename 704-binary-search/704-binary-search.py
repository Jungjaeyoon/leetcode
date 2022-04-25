class Solution:
    def search(self, nums: List[int], target: int) -> int:
        score = 0
        for x in nums:
            if x == target:
                return score
            else:    score += 1
        return -1