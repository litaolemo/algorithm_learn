

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:return "1"

        def str_res(n):
            n_str = str(n)
            r_list = []
            for count,s in enumerate(n_str):
                if count > 0:
                    # print(n_str[count])
                    if s == n_str[count-1]:
                        # print(r_list[-1])
                        temp = str(int(r_list[-1][0]) + 1) + s
                        r_list.pop()
                        r_list.append(temp)
                    else:
                        r_list.append("1" + s)
                else:
                    r_list.append("1" + s)

            return "".join(r_list)
        res = 1
        for x in range(n-1):
            res = str_res(res)
        return res
test = Solution()
print(test.countAndSay(3))
