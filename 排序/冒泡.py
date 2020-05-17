# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 15:36
# @Author  : litao


def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr