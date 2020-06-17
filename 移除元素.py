from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

test = Solution()
print(test.removeElement([0,1,2,2,3,0,4,2],2))

