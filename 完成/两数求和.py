def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for count,num in enumerate(nums):
        ssecend_num = target - num
        if ssecend_num in nums:
            try:
                secend_count = nums.index(ssecend_num,count+1)
                if secend_count:
                    return [count, secend_count]
            except:
                continue


import win32gui

hwnd_title = dict()

#
# def get_all_hwnd(hwnd, mouse):
#     if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
#         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
#
#
# win32gui.EnumWindows(get_all_hwnd, 0)
#
# for h, t in hwnd_title.items():
#     if t is not "":
#         print(h, t)
#
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtGui import *
# import win32gui
# import sys
#
# hwnd = win32gui.FindWindow()
# app = QApplication(sys.argv)
# screen = QApplication.primaryScreen()
# img = screen.grabWindow(hwnd).toImage()
# img.save("screenshot.jpg")
from PIL import ImageGrab

# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标  
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
bbox = (0, 0, 1000, 1000)
im = ImageGrab.grab(bbox)

# 参数 保存截图文件的路径
im.save('as.png')