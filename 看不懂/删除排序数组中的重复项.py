class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_num = len(nums)
        if len_num == 0:
            return 0
        left = 0
        right = 1
        while right < len_num:
            if nums[left] !=nums[right]:
                nums[left+1] = nums[right]
                left += 1
            right += 1
        return left +1