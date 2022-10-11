# -*- coding:utf-8 -*-
# @author :litao
# @Time :2021/9/30 16:38


import numpy as np

# 打印当前numpy版本
# print("打印当前numpy版本 " + str(np.__version__))


# 构造一个全0的矩阵并打印其占用内存大小
# z = np.zeros((5,5))
# print("内存大小" + str(z.size))


# 打印函数的帮助文档
# print(help(np.info(np.add)))


# 创建10-49的数据,并将其倒序排列
# tang_array = np.arange(10,50,1)
# tang_array = tang_array[::-1]
# print(tang_array)


# 找到数组当中不为0的索引
# print(np.nonzero([1,2,3,4,50,0,0,4,3,2]))


# 随机构造一个3*3矩阵,并打印其最大与最小值
# tang_array = np.random.random((3,3))
# print(tang_array.max())
# print(tang_array.min())


# 构造一个5*5的矩阵,令其都为1,最外圈加上0
# tang_array = np.ones((5, 5))
# tang_array = np.pad(tang_array, pad_width=1, constant_values=0, mode='constant')
# print(tang_array)
# print(help(np.pad))


# 构建一个shape(6,7,8)的矩阵,并找到第100个元素的索引值
# print(np.unravel_index(100, (6, 7, 8)))
# print(np.unravel_index(20, (5, 5)))


# 对一个5*5的矩阵做归一化操作
# tang_array = np.random.random((5, 5))
# tang_max = tang_array.max()
# tang_min = tang_array.min()
# tang_array = (tang_array - -tang_min)/(tang_max - tang_min)


# 找到两个数组中相同的值
# z1 = np.random.randint(0, 10, 10)
# z2 = np.random.randint(0, 10, 10)
# print(np.intersect1d(z1, z2))


# 得到今天 明天 昨天的日期
# yesterday = np.datetime64('today','D') - np.timedelta64('1','D')
# today = np.datetime64('today','D')


# 得到一个月中的所有天
# print(np.arange('2017-10','2017-11',dtype='datetime64[D]'))


# 得到一个数的整数部分
# z = np.random.uniform(0, 10, 10)
# print(np.floor(z))


# 创造一个数组,并且不能改变值
# z = np.zeros(5)
# z.flags.writeable = False


# 打印大数据的部分值,全部值
# np.set_printoptions(threshold=5)
# z = np.zeros((15,15))
# print(z)


# 找到在一个数组中,最接近一个数的索引
# z = np.arange(100)
# v = np.random.uniform(0, 100)
# index = (np.abs(z-v)).argmin()
# print(z[index])


# 32位float类型和32位int类型转换
# z = np.arange(10, dtype=np.int32)
# z = z.astype(np.float32)


# 打印数组元素位置坐标与数值
# z = np.arange(9).reshape(3, 3)
# for index,value in np.ndenumerate(z):
#     print(index, value)


# 数组按照某一列进行排序
# z = np.random.randint(0, 10, (3, 3))
# print(z)
# print(z[:,1].argsort())
# print(z[z[:,1].argsort()])


# 统计数组中每个数值出现的次数
# z = np.array([1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 8])
# print(np.bincount(z))


# 对四维数组最后两维求和
# z = np.random.randint(0,10,(4,4,4,4))
# print(z)
# res = z.sum(axis=(-2,-1))

# 交换矩阵中的两行
# z = np.arange(25).reshape(5,5)
# z[[0,1]] = z[[1,0]]
# print(z)

# 找到数组中最长出现的一个数
# z = np.random.randint(0,10,50)
# print(z.bincount(z).argmax())

# 快速查找top k
# z = np.arange(10000)
# np.random.shuffle(z)
# n=5
# print(z[np.argpartition(-z,n)[:n]])

# 去掉数组中,所有元素都相同的数据
# z = np.random.randint(0,3, (10,3))
# print(z)
# # 一行中元素相同
# e = np.all(z[:,1:] == z[:,:-1],axis=1)
# print(e)
#
#
# a = np.array([1, 2, 3, 4])
# b = np.array([1, 2, 3, 5])
# np.all(a==b)
# np.any(a==b)