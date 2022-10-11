# -*- coding:UTF-8 -*-
# @Time  : 2021/4/6 20:43
# @File  : 测试.py
# @email : litao@chanct.com
# @author : litao

# name = "黎涛123456677889"
#
# print(name[-3:])
# age = 25
#
# # for n in name:
# #     print(n)
#
# lis = [1,2,3,4,5,6,7,8,9]
# dic ={
#     "a":1,
#     'b':2,
# }
#
# import re
# a = "姓名去去去的解放军住址手打免12312年龄3232"
# print(a.replace("姓名","\n").replace("住址","\n").replace("年龄","\n"))
# res = a.split("")
import json
import openpyxl
import pandas as pd

cv = open(r"D:\lemo下载\query-hive-7392.csv",encoding='utf-8')
lis = []
for c in cv:
    try:
        # print(c)
        if "郭涛" in c:
            continue
        lis.append(json.loads(c[1:-2].replace('""','"')))
    except:
        print(c[1:-2])
print("down")
Df = pd.DataFrame(lis)
Df.to_excel("res.xlsx")



