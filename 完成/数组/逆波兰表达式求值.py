# -*- coding:UTF-8 -*-
# @Time  : 2021/3/20 10:51
# @File  : 逆波兰表达式求值.py
# @email : litao@chanct.com
# @author : litao
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),  # 需要注意 python 中负数除法的表现与题目不一致
        }

        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)

        return stack[0]



if __name__ == "__main__":
    test = Solution()
    # tokens = ["2", "1", "+", "3", "*"]
    # tokens = ["4", "13", "5", "/", "+"]
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(test.evalRPN(tokens))
