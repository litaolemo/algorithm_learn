class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_str = ""
        count = 0
        while True:
            try:
                tmep_str = strs[0][count]
                for s in strs:
                    if tmep_str == s[count]:
                        pass
                    else:
                        return common_str
                common_str += tmep_str
                count += 1
            except:
                return common_str

test = Solution()
print(test.longestCommonPrefix(["dog","racecar","car"]))