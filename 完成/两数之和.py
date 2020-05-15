from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for count,num in enumerate(nums):
        #     try:
        #         res = nums[count+1::].index(target - num)
        #         return [count,res+count+1]
        #     except:
        #         continue

        dic = {}
        for count,num in enumerate(nums):
            res = dic.get(target - num)
            if res is None:
                dic[num] = count
            else:
                return [count,res]

test = Solution()
# print(test.twoSum([2,7,11,15],9))
# print(test.twoSum([3,2,4],6))
print(test.twoSum([1,1,1,15],2))