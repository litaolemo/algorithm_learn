class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.strip().split(" ")
        return len(s_list[-1])
test = Solution()
print(test.lengthOfLastWord(" a"))