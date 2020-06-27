# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:59:25 2019

@author: Jahn Ma
"""

"""
turtle库：turtle绘图体系
    -turtle可以调出一个其专用的绘图窗体，起始绘图点在窗体视野中央
    -绘图的最小单位是像素，绘图的坐标原点在绘图窗体的左上角
    
turtle.setup()函数：不必须
    -用来设置窗体的大小和位置
    -turtle.setup(width, height, <startx>, <starty>)
"""   

"""    
库 licrary    包 package     模块 module  统称模块   
     
import: 引用库，一般使用 <a>.<b>() 的编码风格
    -import <库名>
    -使用函数时，采用<库名>.<函数名>( <函数参数> )的方式
    -可以避免函数重名的可能，建议用于较长程序
    
使用from和import引入库
    -from <库名> import <函数名>
    -from <库名> import *
    -使用这两种方式引入的库，使用函数时，语法为 <函数名>( <函数参数> )
    -可以会出现函数重名的问题，建议用于简短程序
    
使用import和as来更改库名
    -可以使用该语法给库重新起一个名字
    -import <库名> as <库别名>
    -之后使用该库中的函数时，调用方法为 <库别名>.<函数名>( <函数参数> )
    -可以给调用的的外部库关联一个更短, 更适合自己的名字  

循环语句
    -for <变量> in range( <参数> ):
        <被循环执行的语句>
    -循环次数由range()函数内参数决定
    -其中<变量>表示每次循环的计数器, 其值范围为 0到参数减1

print 输出函数可以一次输出多个单元，每个单元间使用","分割，输出时各个单元间会被加上一个空格符号

range( )函数
    -range(N): 产生 0~N-1 的整数序列, 共N个
    -range(M, N):产生 M~N-1 的整数序列, 共N-M个

"""

'''
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.down()
'''

#import turtle as t
#t.pensize(2)
#for i in range(8):
#    t.fd(100)
#    t.left(45)







