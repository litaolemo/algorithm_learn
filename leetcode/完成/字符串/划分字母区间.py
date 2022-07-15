# -*- coding:UTF-8 -*-
# @Time  : 2020/10/22 17:54
# @File  : 划分字母区间.py

# @email : litao@igengmei.com
# @author : litao
from typing import List

"字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。" \
"返回一个表示每个字符串片段的长度的列表。"
# class Solution:
#     def partitionLabels(self, S: str) -> List[int]:
#         last = [0] * 26
#         for i, ch in enumerate(S):
#             last[ord(ch) - ord("a")] = i
#
#         partition = list()
#         start = end = 0
#         for i, ch in enumerate(S):
#             end = max(end, last[ord(ch) - ord("a")])
#             if i == end:
#                 partition.append(end - start + 1)
#                 start = end + 1
#
#         return partition


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        str_dic = {
            "a":[0,0],
            "b":[0,0],
            "c":[0,0],
            "d":[0,0],
            "e":[0,0],
            "f":[0,0],
            "g":[0,0],
            "h":[0,0],
            "i":[0,0],
            "j":[0,0],
            "k":[0,0],
            "l":[0,0],
            "m":[0,0],
            "n":[0,0],
            "o":[0,0],
            "p":[0,0],
            "q":[0,0],
            "r":[0,0],
            "s":[0,0],
            "t":[0,0],
            "u":[0,0],
            "v":[0,0],
            "w":[0,0],
            "x":[0,0],
            "y":[0,0],
            "z":[0,0],
        }
        for pos, s in enumerate(S):
            str_pos_start = str_dic[s][0]
            if str_pos_start == 0:
                str_dic[s][0] = pos + 1
            else:
                str_dic[s][1] = pos + 1
        print(str_dic)
#


if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    test = Solution()
    print(test.partitionLabels(S))