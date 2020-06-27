# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 19:46:42 2020

@author: Jahn
"""

"""
程序的控制结构
    -程序的分支结构
        *单分支结构
            根据判断条件结果选择不同向前结构
            if <条件>:
                <语句块>
        *二分支结构
            根据判断条件结果选择不同向前路径
            if <条件>:
                <语句块1>
            else:
                <语句块2>
                
            二分支的紧凑形式(相当于C语言的 表达式 ? 语句1 : 语句2)
            <表达式1> if <条件> else <表达式2>     (该语句必须在同一行)
            如果条件满足就执行表达式1，否则执行表达式2 ，表达式指的是没有赋值语句的语句
        *多分支结构
            根据多个条件判断不同运行结果的结构
            if <条件>：
                <语句块1>
            elif:
                <语句块2>
            ...
            else:
                <语句块>
        *关系、逻辑运算符
            关系运算符：
            < :小于                      <= :小于等于
            > :大于                      >= :大于等于
            ==:等于                      != :不等于
            逻辑运算符：
            and : 逻辑与    二元  x and y
            or  : 逻辑或    二元  x or  y
            not : 逻辑非    一元  not x
            
        *程序的异常处理(错误处理)
        try:                                  try:
            <语句块1>                              <语句块1>
        except:                               except <错误类型>：
            <语句块2>                              <语句块2>
        如果语句块1运行过程中                     如果运行语句块1过程中发生错误，且错误类型与
        发生错误，就运行语句                      except后的相同，就运行语句块2，否则
        块2，否则语句块不被运行                   程序产生错误
        
        还有一种结构 try: 
                   except:
                   else:
        这种结构中的esle用于奖励，当try中的语句块正常执行完时，else后的语句块可以执行，否则不执行
    -程序的循环结构
        *遍历循环结构
            for <循环变量> in <遍历结构>:
                <语句块>
            该循环由关键字for和in组成，完整遍历所有元素后结束；
            每次循环，由遍历结构所获得的元素放入循环变量，并执行一次语句块
            常用的搭配方式
            for i in range(N):
                <语句块>
            由range()函数提供计数，循环N次
            for i in range(M,N,K)
                <语句块>
            循环由M到N-1并以K为步长的次数
            for c in s:
                <语句块>
            遍历字符串循环，将字符串s中的元素依次取出给c，并进行循环
            for item in ls:
                <语句块>
            列表循环，从列表ls中依次取出元素进行循环
            for line in fi:
                <语句块>
            文件循环，fi是一个文件标识符，遍历其每行，产生循环
        *无限循环结构
            由条件控制的循环，条件满足时，执行语句块
            while <条件>:
                <语句块>
        *循环控制保留字
            break和continue   均可与for while配套使用
          -break是跳出并结束当前整个循环，执行循环后的语句
          -continue结束当次，继续执行后续次数的循环
        *循环的高级用法 与else搭配
            for <循环变量> in <遍历结构>:        while  <条件>:
                <语句块>                              <语句块> 
            else:                             else:
                <语句块>                              <语句块>
            当循环结构正常循环完毕，没有被break打断时，else后的语句块可以被执行，否则不执行
"""




"""
random库
    -random库是python中用来生成伪随机数的函数
    -random库是python自带的标准库，不需要安装即可使用可直接用 import 使用
    
    -基本随机数函数seed(), random()
        seed(a):种子初始化函数，使用种子a初始化随机数产生算法，默认为当前系统时间, 给了种子后
                为随机过程可以重现，因为在相同的随机数种子的情况下，特定次数获得伪随机数是相同的
        random():产生一个[0.0, 1.0)的一个随机小数
    -扩展随机数函数
        randint(a,b):产生一个[a, b]之间的随机整数
        randrange(m, n[, k]):产生一个在[m, n)之间以k为步长的随机整数
        uniform(a, b):生成一个[a, b]之间的随机小数
        choice(seq):从序列seq中随机选出一个元素
        shuffle(seq):将序列seq中的元素随机排列，并返回随机排列后的序列3
    
"""



##计算BMI值并判断体型
#height, weight=eval(input("请依次输入身高(米)，体重(公斤)[中间使用逗号隔开]： \n"))
#bmi = weight/pow(height, 2)
#print("BMI 数值为{:.2f}".format(bmi))
#who = " "
#if bmi < 18.5:
#    who = "偏瘦"
#elif bmi <25:
#    who = "正常"
#elif bmi < 30:
#    who = "偏胖"
#else:
#    who = "肥胖"
#print("BMI 指标为：国际'{}'".format(who))
#if bmi < 18.5:
#    who = "偏瘦"
#elif bmi <24:
#    who = "正常"
#elif bmi < 28:
#    who = "偏胖"
#else:
#    who = "肥胖"
#print("BMI 指标为：国内1.'{}'".format(who))



#pi=0
#N=10000
#for k in range(N):
#    pi += (1/pow(16,k))*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
#print("圆周率是{:.10f}".format(pi))

##蒙特卡洛法求解圆周率
#from time import perf_counter
#from random import random
#start = perf_counter()
#hits = 0
#darts = 1000*1000
#for i in range(darts):
#    x, y=random(), random()
#    if pow(x**2+y**2, 0.5) <= 1.0:
#        hits+=1
#pi=4*(hits/darts)
#print("圆周率是：{:.7f}".format(pi))
#print("程序运行时间为：{:.2f}s".format(perf_counter()-start))
                                     








































