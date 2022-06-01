class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l = len(triangle[-1])
        val = triangle[0][0]

        for i in range(1, l):
            for j in range(len(triangle[i])):
                print(triangle[i][j], "t")
                if j == 0:
                    val = triangle[i][j] + triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    val = triangle[i][j] + triangle[i-1][j-1]
                else:
                    val = triangle[i][j] + min(triangle[i-1][j-1],triangle[i-1][j])

                triangle[i][j] = val
        return min(triangle[-1])