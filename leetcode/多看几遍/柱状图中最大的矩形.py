class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        max_res = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                # tmep  =heights[stack.pop()]
                # print(i,heights[i],tmep,i - stack[-1] - 1,tmep * (i - stack[-1] - 1))
                # max_res = max(max_res, tmep * (i - stack[-1] - 1))
                max_res = max(max_res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        for i in range(len(stack) - 1):
            max_res = max(max_res, heights[stack.pop()] * (len(heights) - 1 - stack[-1]))
        return max_res


test = Solution()
print(test.largestRectangleArea([15,18,18,3,7,11,2,13,18,15,18,6,6,1,17,15,2,15,0,0]))
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/ji-jian-python-shen-du-jie-xi-dan-diao-dui-zhan-zu/