class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # lis = list(s)
        # for k in t:
        #     try:
        #         lis.remove(k)
        #     except:
        #         return False
        # if len(lis) == 0:
        #     return True
        # else:
        #     return False

        if len(s) != len(t):
            return False
        if sorted(s) != sorted(t):
            return False
        return True

