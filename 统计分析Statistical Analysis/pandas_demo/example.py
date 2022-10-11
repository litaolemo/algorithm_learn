# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/10/8 15:33
import numpy as np
import pandas as pd

# df =  pd.read_csv('///')


# data = {
#     'country': ['a', 'b', 'c'],
#     'population': [10, 12, 14]
# }
# data_df = pd.DataFrame(data)
# print(data_df)
# print(data_df.info)
# print(data_df['country'])

# NaN not a number

# 排序
# data = pd.DataFrame({'group': ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'], 'data': [1, 2, 3, 4, 5, 6, 7, 8, 9]})
# print(data)
# data.sort_values(by=['group', 'data'], ascending=[False, True], inplace=True)
# print(data)


# 去重
# data = pd.DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
#                      'k2': [3, 2, 1, 3, 3, 4, 4]})
# data.drop_duplicates(inplace=True)
# print(data)
# print(data.drop_duplicates(subset='k1'))

# 自定义方法
# data = pd.DataFrame({'food': ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2'], 'data': [1, 2, 3, 4, 5, 6, 7]})
# def food_map(series):
#     if series['food'] == 'A1':
#         return 'A'
#     elif series['food'] == 'A2':
#         return 'A'
#     elif series['food'] == 'B1':
#         return 'B'
#     elif series['food'] == 'B2':
#         return 'B'
#     elif series['food'] == 'C1':
#         return 'C'
#     elif series['food'] == 'C2':
#         return 'C'
# data['food_map'] = data.apply(food_map, axis='columns')
# print(data)
#
# food2Upper={
#     'A1':'A',
#     'A2':'A',
#     'B1':'B',
#     'B2':'B',
#     'C1':'C',
#     'C2':'C',
# }
# data['upper'] = data['food'].map(food2Upper)
# print(data)


# 对象的增删改查
# data = [10, 11, 12]
# index = ["a","b","c"]
# s = pd.Series(data=data,index=index)
# print(s)
# mask = [True, False, True]
# print(s[mask])
# s1 = s.copy()


# dataFrame 的增删改查
# data = [[1, 2, 3], [4, 5, 6]]
# index = ['a', 'b']
# columns = ['A', 'B', 'C']
# df = pd.DataFrame(data=data, index=index, columns=columns)
# print(df)
# print(df.loc['a'])
# print(df.iloc[0])
#
# df.loc['a']['A'] = 150
# print(df)
# df.loc['c'] = [7,8,9]
# print(df)

# 赋值
# df = pd.DataFrame({'data1': np.random.randn(5),
#                    'data2': np.random.randn(5)})
#
# df1 = df.assign(ration=df['data1'] / df['data2'])
# # print(df1)
# df1.drop('data1', axis='columns', inplace=True)
# print(df1)

# 替换
# data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])
# data.replace(9, np.nan, inplace=True)
# print(data)


# cut 分组
# ages = [15, 18, 20, 21, 35, 51, 21, 25, 54, 89]
# bins = [10, 40, 60, 80, 100]
# data = pd.cut(ages, bins)
# print(data)
# print(pd.value_counts(data))
# group_names = ['yong', 'middle', 'old']
# res2 = pd.cut(ages, [10, 20, 50, 80], labels=group_names)
# print(res2)

# 处理空值
# df = pd.DataFrame([range(3), [0, np.nan, 0], [0, 0, np.nan], range(3)])
# print(df)
# print(df.isnull())
# print(df.isnull().any())
# print(df.isnull().any(axis=1))
# print(df.fillna(5))  # 填充缺失值
# print(df[df.isnull().any(axis=1)])

# group by
# df = pd.DataFrame(
#     {'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
#      'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
#      'C': np.random.randn(8),
#      'D': np.random.randn(8),
#      }
# )
# grouped = df.groupby("A")
#
# def get_letter_type(letter):
#     if letter.lower() in 'aeiou':
#         return 'a'
#     else:
#         return 'b'
# grouped = df.groupby(get_letter_type,axis=1)
# print(grouped.count())
#
# s = pd.Series([1, 2, 3, 1, 2, 3], [8, 7, 5, 8, 7, 5])
# print(s)
#
# grouped = s.groupby(level=0)
# print(grouped.first())
# print(grouped.sum())

# df2 = pd.DataFrame({'X': ['a', 'b', 'a', 'b'], 'Y': [1, 2, 3, 4]})
# print(df2)
# print(df2.groupby(['X']).get_group('a'))

# arrays = [
#       ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
#       ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three']
# ]
# index = pd.MultiIndex.from_arrays(arrays, names=['first','second'])
# print(index)
# s = pd.Series(np.random.randn(8),index= index)
# grouped = s.groupby(level=1)
# print(grouped.sum())

# grouped = s.groupby

# grouped = df.groupby(['A', 'B'])
# print(grouped.aggregate(np.sum))
#
# grouped = df.groupby(['A', 'B'], as_index=False)
# print(grouped.aggregate(np.sum))
#
# grouped = df.groupby(['A', 'B']).sum().reindex()
# print(grouped)

# print(grouped.size)
# print(grouped.describe())

# agg
# grouped = df.groupby('A')
# print(grouped['C'].agg([np.sum, np.mean, np.std]))

### 字符串
# s = pd.Series(['A','b','B','gaer','AGER',np.nan])
# print(s.str.lower())
# print(s.str.len())
#
# index = pd.Index(['   tang','sdd   ','  nodd '])
# print(index.str.strip())
# print(index.str.lstrip())
# print(index.str.rstrip())


# df = pd.DataFrame(np.random.randn(3,2),columns=['A a','B b'],index=range(3))
# df.columns = df.columns.str.replace(' ','_')
# print(df)

# s = pd.Series(['a_b_C', 'c_d_e', 'f_g_h'])
# print(s.str.split('_', expand=True))
# print(s.str.split('_', expand=True, n=1))
# s = pd.Series(['A','Asd','sd','dsds','Aafsd'])
# print(s.str.contains('Aa'))
# s = pd.Series(['a','a|b','a|c'])
# print(s.str.get_dummies(sep='|'))

### 索引
# s = pd.Series(np.arange(5), index=np.arange(5)[::-1])
# print(s[s.isin([1, 3, 4])])

# s2 = pd.Series(np.arange(6), index=pd.MultiIndex.from_product([[0, 1],['a', 'b', 'c']]))
# print(s2)
# print(s2.iloc[s2.index.isin([(1, 'a'), (0, 'b')])])
# dates = pd.date_range('20210101', periods=8)
# df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
# print(df)
# print(df.select(lambda x: x == 'A', axis='columns'))
# print(df['A'])
# print(df.where(df < 0, -df))
## query
# df = pd.DataFrame(np.random.randn(10, 3), columns=list('abc'))
# print(df.query('(a<b)'))
# print(df.query('(a<b) & (b<c)'))

