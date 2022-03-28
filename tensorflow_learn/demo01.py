# -*- coding:utf-8 -*-
# @author :litao
# @Time :2022/3/28 13:43


import tensorflow as tf
import numpy as np

print(tf.__version__)
print('GPU:',tf.config.list_physical_devices('GPU'))

x = [[1.]]
m = tf.matmul(x, x)
print(m)

x = tf.constant([[1,9],[3,6]])
print(x)

x = tf.add(x,1)
print(x)

print(x.numpy())

x = tf.cast(x, tf.float32)
print(x)

x1 = np.ones([2,2])
x2 = tf.multiply(x1,2)
print(x2)