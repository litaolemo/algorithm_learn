class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        j = len(height) - 1
        while i < j:
            temp = (j - i) * min(height[i], height[j])
            if temp > res:
                res = temp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res


test = Solution()
print(test.maxArea([1,8,6,2,5,4,8,3,7]))


