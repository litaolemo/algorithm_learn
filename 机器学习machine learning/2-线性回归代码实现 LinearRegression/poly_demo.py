# -*- coding:utf-8 -*-
# @author :litao
# @Time :2022/11/5 22:27
# _*_encoding=utf-8_*_
# pytorch 里面最基本的操作对象是Tensor,pytorch 的tensor可以和numpy的ndarray相互转化。
# 实现一个线性回归
# 所有的层结构和损失函数都来自于 torch.nn
# torch.optim 是一个实现各种优化算法的包，调用的时候必须是需要优化的参数传入，这些参数都必须是Variable


# 实现 y = b + w1 *x + w2 *x**2 +w3*x**3
import os

os.environ['CUDA_DEVICE_ORDER'] = "PCI_BUS_ID"
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import torch
import numpy as np
from torch.autograd import Variable
import matplotlib.pyplot as plt
from torch import nn


# pre_processing
def make_feature(x):
    x = x.unsqueeze(1)  # unsquenze 是为了添加维度1的，0表示第一维度，1表示第二维度，将tensor大小由3变为（3,1）
    return torch.cat([x ** i for i in range(1, 4)], 1)


# 定义好真实的数据


def f(x):
    W_output = torch.Tensor([0.5, 3, 2.4]).unsqueeze(1)
    b_output = torch.Tensor([0.9])
    return x.mm(W_output) + b_output[0]  # 外积，矩阵乘法


# 批量处理数据
def get_batch(batch_size=32):
    random = torch.randn(batch_size)
    x = make_feature(random)
    y = f(x)
    if torch.cuda.is_available():
        return Variable(x).cuda(), Variable(y).cuda()
    else:
        return Variable(x), Variable(y)


# def model
class poly_model(nn.Module):
    def __init__(self):
        super(poly_model, self).__init__()
        self.poly = nn.Linear(3, 1)

    def forward(self, input):
        output = self.poly(input)
        return output


if torch.cuda.is_available():
    print("sdf")
    model = poly_model().cuda()
else:
    model = poly_model()

# 定义损失函数和优化器
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

epoch = 0
while True:
    batch_x, batch_y = get_batch()
    # print(batch_x)
    output = model(batch_x)
    loss = criterion(output, batch_y)
    print_loss = loss.data
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    epoch = epoch + 1
    if print_loss < 1e-3:
        print(print_loss)
    break

model.eval()
print("Epoch = {}".format(epoch))

batch_x, batch_y = get_batch()
predict = model(batch_x)
a = predict - batch_y
y = torch.sum(a)
print('y = ', y)
predict = predict.data.cpu().numpy()
plt.plot(batch_x.cpu().numpy(), batch_y.cpu().numpy(), 'ro', label='Original data')
plt.plot(batch_x.cpu().numpy(), predict, 'b', ls='--', label='Fitting line')
plt.show()
