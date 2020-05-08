class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        has = False
        maxarea = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # print(dp)
        for i in range(len(matrix)):
            stack = [-1]

            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    high = dp[i][j] = dp[i - 1][j] + 1
                    has = True
                else:
                    high = 0
                # compute the maximum width and update dp with it


                # compute the maximum area rectangle with a lower right corner at [i, j]
                while len(stack) > 1 and high <= dp[i][stack[-1]]:
                    long = min(dp[i][stack.pop()],j - stack[-1]-1)
                    maxarea = max(maxarea, long*long)
                stack.append(j)
            for j in range(len(stack) - 1):
                long = min(dp[i][stack.pop()] , (len(dp[i]) - 1 - stack[-1]))
                maxarea = max(maxarea, long * long)
            #print(dp[i],maxarea)
        # return max_res
        if maxarea >=1:
            return maxarea
        elif has:
            return 1
        else:
            return 0



test = Solution()
# print(test.maximalRectangle(
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# ))
print(test.maximalRectangle(
[
  ["1","0"],
  ["1","0"],
]
))