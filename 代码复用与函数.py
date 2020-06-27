# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:59:05 2020

@author: Jahn
"""

"""
-函数- 完成某一特定功能的可重复使用的代码块

    *定义结构 使用def定义函数
        def <函数名>(<参数名>):   (参数可为0或多个)
            <函数体>
            return <返回值>
    *函数的参数    
       &可选参数
        python中定义函数时支持参数数量可变，即在定义函数时有某参数，但在使用函数时不使用该参数位置
        要求可变参数必须在不可选参数的后面
        def <函数名>(<非可选参数>, <可选参数>)：
            <函数体>
            return <返回值>
        需要将可选参数给默认值，函数体运行时若调用函数时未使用该参数位置，则可选参数
        以默认值参与运算
       &不定参数
        python中也支持定义函数时函数的参数数量不定，具体数量由用户调用函数时确定，这种情况用户
        输入的所有参数是以组合数据，一般为列表，被函数使用的
        def <函数名>(n, *c)
            <函数体>
            return <返回值>
       &函数参数的传递
        有两种方法，一种是根据函数参数的位置对应给参数，一种是按照函数定义时参数的名字指定各个参数值
    *函数的返回值
        一个函数可以有返回值，也可以没有返回值
        一般使用return返回函数值，return支持返回多个值，多个值之间使用“,”隔开，也支持将多个
        返回值组合，使用元组返回函数值，此时函数的返回值类型是元组
    *局部变量和全局变量
        局部变量指在函数内部使用的参数，全局变量指在函数体外定义的变量，该变量全局有效，如果一个
        函数内没有创建一个组合数据类型，但在函数中使用了这个变量，那么这个被使用的组合数据类型
        就是函数体外被定义的全局变量，因为组合数据其实是指针
        局部变量可是说是函数内部的占位符，与全局变量不同，即使重名也不是一个东西
        局部变量会在函数运算结束后被释放，即不再存在
        可以使用global关键字在函数体内使用已定义全局变量，global关键字用来在函数体内声明其后使用
        的变量是一个全局变量，而不是一个函数内部的局部变量
    *lanbda函数
        类似于使用宏定义定义简单的运算函数
        lanbda函数使用关键字lanbda来定义, 定义结构为
        函数名=lanbda <函数参数>:<运算表达式>
        使用时与普通函数相同 函数名(函数参数)  
"""


'''
模块化设计与函数递归
    *模块化设计
        &函数与函数之间通过参数和返回值相关联，要求函数的参数和返回值尽可能简单
        &函数内要尽量紧密，实现功能，函数与函数之间的关系要尽量简单
        &定义的子函数称为模块，主函数体现模块与模块间的关系
    *递归
        递归要求计算过程中存在递归链条，每一次的计算之间存在关联
        递归要求存在一个或多个不需要再次递归的基例，作为递归结束的判断标志
    *递归的一般形式
        递归是一个函数，需要使用函数定义的方式实现
        在递归函数内部，使用分支语句对输入参数进行判断
        在递归函数中，一般使用分支语句判断基例和递归链条，分别编写对应代码
    *递归包括两个过程，首先是顺序执行程序，直到执行到基例，无法再向下执行下去，在这个过程中
     递归的各个函数的返回值被得到；第二个过程是逆序索引返回值，程序由基例向上运行，根据顺序
     执行得到的各次递归的返回值来计算最终结果


'''


'''
PyInstaller库的使用
    PyInstaller库的功能是将python文件转换成无需源代码的可执行文件
    
    -pyInstaller库安装后可以使用一个命令pyinstaller, 使用该命令可以将.py文件变成可执行程序
    -用法：
        在源代码所在目录下，使用命令行，键入 pyinstaller -F <文件名.py>
        在生成的dist文件夹中会有生成的可执行文件，其他生成的文件夹可以删除
    -其他命令
        pyinstaller -h       查看帮助文档
        pyinstaller --clean   清理生成的临时文件
        pyinstaller -i <图标文件名.ico>   指定生成的打包程序的图标
    
    
    
第三方库的安装可以使用python提供的pip工具，一般语句为 pip install <库名称
>

'''










'''
import turtle
import time
#绘制间隔
def drawGap():
    turtle.penup()
    turtle.fd(5)

#绘制某一根数码管
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
    return
    
#绘制某个数字
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.right(180)
    turtle.penup()
    turtle.fd(20)
    return

#绘制日期
#def drawDate(date):
#    for i in date:
#        drawDigit(eval(i))
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i=="-":
            turtle.write("-", font=("Arial",18,"normal"))
            turtle.fd(40)
        elif i=="+":
            turtle.pencolor("blue")
            turtle.write(" ",font=("Arial",18,"normal"))
            turtle.fd(40)
        elif i==":":
            turtle.write(":", font=("Arial",18,"normal"))
            turtle.fd(40)
        else:
            drawDigit(eval(i))
              
def main():
    turtle.setup(1250, 450, 0, 50)
    turtle.penup()
    turtle.fd(-600)
    turtle.pensize(4)
    turtle.speed(1000)
    while True:
        sysTime=time.strftime("%Y-%m-%d+%H:%M:%S",time.localtime())
        drawDate(sysTime)
        turtle.clear()
        turtle.fd(-1180)
        
if __name__ == "__main__"
    main()
'''


'''
#递归示例
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

def rvs(s):
    if s=="":
        return s
    else:
        return rvs(s[1:])+s[0] #每一次递归都取出当前字符串最左边的字符放到最后面
print(rvs("1234567"))

def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(7))
'''


'''
count=0
def hanoi(n, src, dst, mid):    #n代表汉诺塔的圆盘数量
    global count
    if n==1:
        print("{}:{}->{}".format(1, src, dst))
        count+=1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n,src,dst))
        count+=1
        hanoi(n-1,mid,dst,src)
hanoi(3,"A","C","B")
'''


#绘制科赫雪花曲线
#绘制雪花的一支
import turtle
def koch(size, n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)
    
KOCH_LEVEL = 4       #指定科赫曲线的阶数
def main():
    turtle.setup(1000, 800, 0, 0)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(1)
    turtle.pencolor("blue")
    turtle.speed(100)
    koch(200,KOCH_LEVEL)
    turtle.right(60)
    koch(200,KOCH_LEVEL)
    turtle.right(60)
    koch(200,KOCH_LEVEL)
    turtle.right(60)
    koch(200,KOCH_LEVEL)
    turtle.right(60)
    koch(200,KOCH_LEVEL)
    turtle.right(60)
    koch(200,KOCH_LEVEL)
    turtle.right(60)
    turtle.done()

main()


'''
import random

def genpwd(length):
    i=10**(length-1)
    j=10**length-1
    s=random.randint(i, j)
    return s

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
'''
'''
def prime(m):
    li=[]
    count=0
    while count<5:
        for i in range(2, m//2):
            if m%i==0:
                break
        else:
            count += 1
            li.append(m)
        m += 1
    return li

n = eval(input())
l = prime(int(n))
print("{},{},{},{},{}".format(l[0],l[1],l[2],l[3],l[4]))
'''
'''
def prime(m):
    for i in range(2,m):
        if m % i == 0:
            return False
    return True

n = eval(input())
n_ = int(n)
n_ = n_+1 if n_ < n else n_
count = 5

while count > 0:
    if prime(n_):
        if count > 1:
            print(n_, end=",")
        else:
            print(n_, end="")
        count -= 1 
    n_ += 1
'''


















