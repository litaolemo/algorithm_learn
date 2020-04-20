class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        diff = abs(nums[0] + nums[1] + nums[2] - target)
        temp = diff
        res = nums[0] + nums[1] + nums[2]
        for i in range(n):
            L = i + 1
            R = n - 1
            while (L < R):
                res_tmep = nums[i] + nums[L] + nums[R]
                temp = abs(res_tmep - target)
                if temp < diff:
                    diff = temp
                    res = res_tmep
                    #print(diff, res)
                if res_tmep > target:
                    R = R -1
                elif res_tmep < target:
                    L = L+1
                else:
                    return res
        return res



test = Solution()
print(test.threeSumClosest([1,2,4,8,16,32,64,128],82))