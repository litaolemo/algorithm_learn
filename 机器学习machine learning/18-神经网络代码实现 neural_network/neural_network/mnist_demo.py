# -*- coding:utf-8 -*-
# @author :litao
# @Time :2022/11/12 14:24
from multilayer_perceptron import MultilayerPerceptron
import pandas as pd
import numpy as np
pd.set_option("display.precision", 16)
 #显示两位
f = open("./cloud.dat",encoding="utf-8")
res_list = []
for s in f:

    d1,d2 = s.split("	")
    res_list.append([d1,d2])
# print(res_list)
import matplotlib.pyplot as plt
res_df = pd.DataFrame(res_list)
res_df =  res_df.astype("float")
# res_df
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.scatter(res_df.loc[:,0],res_df.loc[:,1],color='r', label='real')

train_data = res_df.sample(frac = 0.8)
test_data = res_df.drop(train_data.index)

train_data = train_data.values
test_data = test_data.values

num_training_examples = 5000

x_train = train_data[:num_training_examples,1:]
y_train = train_data[:num_training_examples,[0]]

x_test = test_data[:,1:]
y_test = test_data[:,[0]]


layers=[1,25,1]

normalize_data = False
max_iterations = 500
alpha = 0.1


multilayer_perceptron = MultilayerPerceptron(x_train,y_train,layers,normalize_data)
(thetas,costs) = multilayer_perceptron.train(max_iterations,alpha)
plt.plot(range(len(costs)),costs)
plt.xlabel('Grident steps')
plt.xlabel('costs')
plt.show()
