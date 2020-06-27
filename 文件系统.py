# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:32:54 2020

@author: Jahn
"""

"""
文件和数据格式化
    -文件的使用
        文件的结尾是"", 空符号
        *文件的类型
            文件有两种展示形式，文本文件和二进制文件
            &文本文件
                由单一特定编码形式表达的文件，文本文件可以看作长字符串
            &二进制文件
                直接由0，1表示的文件，由特定形式组合而成，包括.avi .jpeg等
            如果需要对其进行理解，借用文本形式打开；如果仅需要使用其存储形态，就用二进制形式处理
    -文件的打开与关闭
        对文件的处理流程是：打开  处理  关闭
        *文件的打开
            <文件名>=open(<文件名>, <打开模式>)
            其中，文件名包括文件路径及名称，若与源文件同目录，则文件路径可缺省
                 文件模式包括文本模式和二级制模式，读模式和写模式
                 文件打开后以一个抽象的文件变量，即文件句柄表示
            &文件的路径可以是绝对路径，通常用‘/’代替‘\’表示绝对路径
                      也可以是相对路径，相对路径指打开的文件与当前的程序之间的路径
                      "./"表示当前判断盘符好像
            &文件打开模式
                "r": 只读模式，为缺省值，若文件不存在，返回错误FileNotFoundError
                "w": 覆盖写模式，文件不存在时将创建一个文件，若文件存在，则完全覆盖，然后写入
                "x": 创建写模式，文件不存在，创建一个文件，文件存在，返回错误FileExistsError
                "a": 追加写模式，文件不存在，创建一个文件，文件存在，则不改变原文件内容，在文件最后追加内容
                "b": 以二进制形式打开文件
                "t": 以文本文件形式打开文件，为缺省值
                "+": 可与r w x a组合使用，指在原功能的基础上增加 同时读写的功能
        *文件的关闭
            <变量名>.close()
            变量名指已打开的文件的句柄
    -文件内容的操作
        注意文件指针的位置
        &文件内容的读取
            操作方法 3
            <f>.read( [size=-1] ): 默认读入全部的文件内容，其中可选参数size用来指定读入
                                   的文件长度(字节数)，若size不保持缺省值，则将读入
                                   该文件前size个字符
            <f>.readline( [size=-1] ): 读取指针当前指向行的信息，如果给出size参数，则
                                       表示读取这一行前size个字符
            <f>.readlines( [hint=-1] ): 默认读入文件所有行，以每行为元素形成一个列表
                                        如果给出参数hint，则读入前hint行
        &文件的写入
            文件的写入要求文件以写模式打开
            操作方法
            <f>.write(s): 向文件写入一个字符串s
            <f>.writelines(lines): 将一个元素全为字符串的列表写入文件，其中参数lines
                                   是一个列表，其内元素全为字符串
                                   此时的写入是直接将列表中的元素直接拼接后写入，元素间没有分隔
            <f>.seek(offset): 改变当前文件操作指针的位置，参数offset定义如下
                              0-文件开头     1-当前位置     2-文件结尾
                
                
"""

'''
f=open('hamlet.txt', "r+")
f.seek(1000)
print(f.read())
f.close()
'''

#行进距离  转向判断  转向角度
import turtle

turtle.clear()
turtle.title("自动绘制轨迹")
turtle.setup(800,600,0,0)
turtle.pencolor("red")
turtle.pensize(5)

#加载文件
datals=[]
f=open("data.txt", "r",encoding="UTF-8")
for line in f:
    line = line.replace("\n", "")
    datals.append( list(map(eval,line.split("，"))) ) #将字符串数据变成数字
    
#解析文件,绘制图形
for i in range(len(datals)):
    turtle.pencolor(datals[i][3], datals[i][4], datals[i][5])
    turtle.fd(datals[i][0])
    if datals[i][1]:
        turtle.right(datals[i][2])
    else:
        turtle.left(datals[i][2])

turtle.hideturtle()
turtle.done()





































