"""
有一个密钥字符串 S ，只包含字母，数字以及 '-'（破折号）。其中， N 个 '-' 将字符串分成了 N+1 组。

给你一个数字 K，请你重新格式化字符串，除了第一个分组以外，每个分组要包含 K 个字符；而第一个分组中，至少要包含 1 个字符。两个分组之间需要用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。

给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/license-key-formatting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper().split("-")
        full_Str = "".join(S)
        str_num = len(full_Str)
        s_str = ""
        extra_str_mun = str_num % K
        if extra_str_mun != 0:
            s_str += full_Str[0:extra_str_mun] + "-"
        for count,s in enumerate(full_Str[extra_str_mun::]):
            if (count+1) % K ==0:
                s_str += s + "-"
            else:
                s_str += s
        return s_str.strip("-")

test = Solution()
# print(test.licenseKeyFormatting(S = "5F3Z-2e-9-w", K = 4))
print(test.licenseKeyFormatting(S = "2-5g-3-J", K = 2))
# print(test.licenseKeyFormatting(S = "2-4A0r7-4k", K = 4))
