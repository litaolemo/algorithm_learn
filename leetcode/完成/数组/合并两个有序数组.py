# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/19 14:19
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        last = m + n - 1
        while n:
            if m == 0 or nums1[m - 1] <= nums2[n - 1]:
                nums1[last] = nums2[n - 1]
                last -= 1
                n -= 1
            else:
                nums1[last] = nums1[m-1]
                m -= 1
                last -= 1
        return nums1


if __name__ == "__main__":
    test = Solution()
    print(test.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
