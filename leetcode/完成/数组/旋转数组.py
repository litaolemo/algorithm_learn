#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #nums = nums[-k::] + nums[0:k+1]
        nums[:] = nums[-k % len(nums):] + nums[: -k % len(nums)]
        print(nums)

test = Solution()
test.rotate([1,2,3,4,5,6,7],3)