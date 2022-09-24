# -*- coding:utf-8 -*-
'''
@File    :   CodeStandard.py
@Time    :   2022/09/23 14:22:58
@Author  :   SheltonXiao
@Version :   1.0
@Contact :   pi620903@163.com
@Desc    :   None
@License :

    (c) Copyright 2022 SheltonXiao

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or(at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY;without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
    GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with this program.If not, see < https: //www.gnu.org/licenses/>.
'''

class Program(object):
    def __init__(self):
        try:
            A = input('请输入数字A：')
            B = input('请选择运算符号（+、-、*、/）：')
            C = input('请输入数字B：')
            if B == "+":
                D = str(float(A)+float(C))
            elif B == "-":
                D = str(float(A)-float(C))
            elif B == "*":
                D = str(float(A)*float(C))
            elif B == "/":
                if float(C) != 0:
                    D = str(float(A)/float(C))
                else:
                    raise Exception("除数不能为0")
            else:
                raise Exception("运算符错误")
            print("结果是："+D)
        except Exception as exp:
            print("您的输入有错：")
            print(exp)

if __name__ == '__main__':
    Program()