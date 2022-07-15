# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/7/19 10:43


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res_list = []
        max_num = max(len(a),len(b))
        count = 1
        sign = False
        while count <= max_num + 1:
            try:
                a_temp = int(a[-count])
            except:
                a_temp = 0

            try:
                b_temp = int(b[-count])
            except:
                b_temp = 0
            if sign:
                if a_temp + b_temp == 2:
                    res_list.insert(0,"1")
                    sign =True
                elif a_temp + b_temp == 1:
                    res_list.insert(0,"0")
                    sign = True
                else:
                    res_list.insert(0,"1")
                    sign = False
            else:
                if a_temp + b_temp == 2:
                    res_list.insert(0,"0")
                    sign =True
                elif a_temp + b_temp == 1:
                    res_list.insert(0,"1")
                    sign = False
                else:
                    res_list.insert(0,"0")
                    sign = False
            count += 1
        if res_list[0] == "0":
            return "".join(res_list[1::])
        return "".join(res_list)







if __name__ == "__main__":
    test = Solution()
    print(test.addBinary("0","0"))