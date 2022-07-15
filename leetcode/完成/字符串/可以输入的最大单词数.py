# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/20 10:40

"""
1935. 可以输入的最大单词数 显示英文描述
通过的用户数3292
尝试过的用户数3372
用户总通过次数3331
用户总提交次数4381
题目难度Easy
键盘出现了一些故障，有些字母键无法正常工作。而键盘上所有其他键都能够正常工作。

给你一个由若干单词组成的字符串 text ，单词间由单个空格组成（不含前导和尾随空格）；另有一个字符串 brokenLetters ，由所有已损坏的不同字母键组成，返回你可以使用此键盘完全输入的 text 中单词的数目

"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # if not text:
        #     return 0
        # str_list = text.split(" ")
        # count = len(str_list)
        # for s in str_list:
        #     for b in brokenLetters:
        #         if b in s:
        #             count -= 1
        #             break
        # return count

        count = 1
        sign = False
        for s in text:
            if s == " ":
                sign = False
                count += 1
            if not sign:
                for b in brokenLetters:
                    if b == s:
                        count -= 1
                        sign = True
        return count

if __name__ == "__main__":
    test = Solution()
    print(test.canBeTypedWords("leet code","e"))
