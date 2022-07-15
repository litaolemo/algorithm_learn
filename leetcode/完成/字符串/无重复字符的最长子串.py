# -*- coding: utf-8 -*-
# Time: 2021-07-03




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        target_str = ""
        res_list = []
        for single in s:
            if not target_str:
                target_str = single
            elif single in target_str:
                if res_list:
                    if len(res_list[0]) < len(target_str):
                        res_list.pop()
                        res_list.append(target_str)
                else:
                    res_list.append(target_str)

                target_str = target_str.split(single)[1]+single
            else:
                target_str += single

        res_list.append(target_str)
        if len(res_list[0]) < len(target_str):
            res_list.insert(0,target_str)
        return res_list[0]




if __name__ == "__main__":
    test = Solution()
    print(test.lengthOfLongestSubstring("dvdf"))
    print(test.lengthOfLongestSubstring("abcabcbb"))