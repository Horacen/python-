# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:50:33 2020

@author: Jahn Ma
"""

"""
基本数据类型
    -数字类型
        整数类型：可正可负，没有取值范围限制
            pow(x, y): 计算x的y次方
            具有四种进制表示方式：
                十进制： 1010
                二进制：使用0b或0B开头， 0b10, -0B10
                八进制：使用0o或0O开头， 0o56, -0O56
                十六进制：使用0x或0X开头，0xfe, -0Xfe
                
        浮点数类型：带有小数点及小数的数字，取值范围和小数的精度都有限制(可忽略)
            需要注意的是，浮点数间存在不确定尾数，这个不是bug(由于计算机使用二进制表示小数的原因)
            round(x, d): 作用是对x四舍五入，d是小数被截取的位数，返回值是True和False
            浮点数的科学计数法表示：使用字母e或E作为幂的符号，以10为基数
                <a>e<b> 表示 a*10的b次方  4.3e-3
                
        复数类型：与数学中的复数类型相同, 关键词是j 4+5j
        
    -数字运算操作符
        + ：求和     - ：求差      * ：求乘积       / ：求商，产生的结果默认为浮点数   # 字符乘上一个数字n，相当于把该字符复制n次
        //：求商，整数除，将求得的结果取整
        % ：模运算，取余运算                       ** ：求幂运算，也可实现开方运算   
        
        python同样具有 += -= *=  /=  //=  %=  **= 二元操作运算符
        不同的数字类型可以混合运算，生成的类型是最宽的类型： 整数-->浮点数-->复数
        
    -数值运算函数
        abs(x):求x的绝对值，将其作为返回值
        divmod(x ,y):商余函数，同时计算x与y的商和余数，并将其作为返回值输出，返回值是(x//y, x%y),二元数
        pow(x, y[, z]):幂余函数，运算法则是 x**y%z, [..]表示该参数位置可不使用，当不使用时为求幂运算
        round(x[, d]):四舍五入函数，d是保留的小数的的位数，默认值是0
        max(x, y, z...):求若干个数中的最大值
        min(x, y, z...):求若干个数中的最小值
        
        数值类型转换函数
        int(x):将x变成整数的函数，x可以是浮点数，字符串等
        float(x):将x变成浮点数数的函数，x可以是整数，字符串等
        str(x):将x变成一个字符串
        list(x):将x变为一个列表型数据
"""
   

"""
字符串类型与操作
    -字符串的一般特征
        字符串是由0个或多个字符组成的有序字符序列，可以对其中的字符进行索引
        由一对单引号或一对双引号表示
        
    -字符串的表示(两类四种)
        由一对单引号或双引号表示，仅表示单行字符串
        由一对三单引号或三双引号表示，可以表示多行字符串
        需要注意的是，python中允许输出的字符串序列中存在单引号或者双引号，当要输出一对
                     当要在输出的字符串序列中输出单引号时，该字符串左右使用双引号标注
                     当要在输出的字符串序列中输出双引号时，该字符串左右使用单引号标注
                     当要在输出的字符串中输出单双两种引号时，使用三单引号标注
                     
    -字符串的序号
        正向递增序号：
            字符串由开始处向结尾处索引，序号从0向右递增
        反向递减序号：
            字符串由结尾处向开始处索引，序号从-1向左递减
            
    -字符串的使用
        使用[]获取字符串中的一个或多个字符
        索引：返回字符串中的单个字符
            <字符串>[M]
            通常上边界不包括在提取字符串内
            如果没有指定值，则分片的边界默认为0和序列的长度
            str[1:3]获取从偏移为1的字符一直到偏移为3的字符串，不包括偏移为3的字符串 
            str[1:] 获取从偏移为1的字符一直到字符串的最后一个字符（包括最后一个字符）
            str[:3] 获取从偏移为0的字符一直到偏移为3的字符串，不包括偏移为3的字符串 
            str[:-1] 获取从偏移为0的字符一直到最后一个字符（不包括最后一个字符串）
            str[:] 获取字符串从开始到结尾的所有元素 : "string"
            str[-3:-1] 获取偏移为 -3 到偏移为 -1 的字符，不包括偏移为 -1 的字符 
            str[-1:-3] 和 str[2:0] 获取的为空字符，系统不提示错误: ""
            分片的时候还可以增加一个步长，str[::2] 输出的结果为: 
        切片：返回字符串中一段字符字串
            <字符串>[M:N:K]:根据步长K对字串[M:N]切片 
                M表示起始的序号，可缺失，缺省值是0
                N表示结束的序号，可缺失，缺省值是-1
                K表示步长，可缺失，缺省值是1，表示不跳跃；K=-1时表示逆序索引切片(从右向左)
                
    -字符串的特殊字符
        转义符"\"：
            转义符表示字符的本义，不对其进行语法检查，而是作为一个字符出现
        回退符"\b":
        换行符"\n":将光标移动到下行的行首
        回车符"\r":新建一行，使光标移动到当前行的行首
        
    -字符串的操作符
        + ：x+y表示连接两个字符串x和y
        * ：n*x表示复制n次字符串
        in:x in s,判断x是不是s的字串，返回值是True或False
        
    -字符串处理函数
        len(x): 求得字符串x的长度，返回值为字符串的字符个数
        str(x): 在x两端加上双引号，将其变成字符串类型的数据，与eval()功能相反
        hex(x): 将整数x使用十六进制表示，并将该十六进制数作为字符串返回
        oct(x): 将整数x使用八进制表示，并将该八进制数作为字符串返回
        chr(u): 求得Unicode编码序号u对应的符号 
        ord(x): 求得符号x对应的Unicode编码序号
        
    -字符串的处理方法
        方法是面向对象编程的名词，值得是 <a>.<b> 中的b, a表示的是对象，b表示
            针对该对象的方法，或者说对对象a所进行的处理，提供的服务
        str.lower()或str.upper():
            将字符串str全部变为小写/全部变成大写，并返回
        str.split("sep"):(相当于切割)
            以字符串被指定的字符sep分割的各个部分为列表中的元素返回一个列表
        str.count("sub"):
            求得单元sub在字符串str中出现的次数，并将其以int型数据返回
        str.replace(old, new):
            将字符串str中为old的单元替换为new的单元
        str.center(width[ ,"fillchar"]):格式化输出
            将字符串str居中，然后使用总宽度为width的fillchar字符左右包围他，返回类型是字符串
        str.join("iter"):掺沙子
            在字符串str的各个元素的中间添加一个iter字符(除了最后一个)
            .join() 方法也可以用来处理其他类型的数据，形成字符串数组。
                    seq.join(ls)
                    将字符串、元组、列表ls中的元素以指定的字符seq(分隔符)连接生成一个新的字符
                    串并返回
            
            
    -字符串类型的格式化
        字符串的格式化使用.format()的方法再加上槽的辅助
        槽：{}
            python使用{}来表示槽，槽仅在字符串使用，槽使用.format()函数进行填充，
            默认情况下槽和.format()函数中的参数依次对应，若有多个参数，则可通过在槽中
            指定参数位置的方法来指定槽的填充关系(.format()函数中的参数由左向右按
            012次序排序)
        槽的相关控制：
            ":" : 引导符，相当于代替需要输出的内容，引导符前面的序号代表使用.format()
                    方法中填充的参数的序号，引导符后代表的是对填充的数据进行的各种处理
            ".x"：在槽中使用字符"."表示需要限制填充的数据(浮点数的精度)，保留x位小数 :.f
                    也可表示限制输出的字符串的长度为x位
            ",": 千位分隔符，仅用于输出一个数据便于人阅读时使用
            "type":输出的数据的类型
                如整数：b d o x c(Unicode编码)
                浮点数：e f %   
"""


"""
import time
time库：python中的处理时间的标准库
    -时间获取
        time()     time.time():返回值是一个浮点数，难以理解
        ctime()    time.ctime():返回值是一个字符串，内含星期 月份 日期 精确时间 年份
        gmtime()   time.gmtime():返回值是一个便于程序使用时间格式
    -时间格式化
        时间格式化借用模板来输出获取的各个时间参数
        strftime(tpl, ts)函数  time.strftime(tpl, ts)
        将获取到的时间使用tpl定义的输出模板输出
        其中 tql是一个字符串，用来定义输出的时间格式
             ts是计算机内部的时间类型变量，一般是time.gmtime()函数的返回值
        格式化字符
        %Y:年份，数字形式
        %m:月份，数字形式                 
        %B:月份，英文名称                %b:月份，英文名称缩写
        %d:日期，数字形式
        %A:星期，英文名称                %a:星期，英文名称缩写
        %H:小时，24小时制                %h:小时，12小时制              %p:AM/PM标志
        %M:分钟，数字形式
        %S:秒，数字形式
        strptime(timeStr, tps)  time.strptime(timeStr, tps)
        将timeStr表示的时间字符串以tps的模板转换成时间(timeStr和tps要对应)
        
    -程序计时
        测量起止动作所使用的时间
        perf_counter():返回一个浮点数，浮点数表示调用这个函数时的时刻，使用作差来求取时间差,差值是秒
        sleep(s):使程序停滞s秒后再继续运行，s可以是浮点数
        
        
    print("\r", end=" ")这个格式可以使输出一直停在本行且是最前面，而不是在到下一行(一个print会换一次行)
"""

#dayup = pow(1.001, 365)
#daydw = pow(0.999, 365)
#print("{:.2f} {:.2f}".format(dayup, daydw))


#dayup = 1.0
#dayfc = 0.001
#
#for i in range(365):
#    if (i%7) in [0,6]:
#        dayup = dayup*(1-dayfc)
#    else:
#        dayup = dayup*(1+dayfc)
#print("{:.2f}".format(dayup))


#def dayUP(factor):
#    dayup = 1.0
#    for i in range(365):
#        if i%7 in [0,6]:
#            dayup=dayup*(1-0.01)
#        else:
#            dayup=dayup*(1+factor)
#    return dayup
#dayfc = 0.01
#while dayUP(dayfc) < 37.78:
#    dayfc += 0.0001
#print("{:.4f}".format(dayfc))



#weekID=eval(input("请输入1-7\n"))
#week="一二三四五六日"
#print("星期"+week[weekID-1])


#def jduge_year():
#    year=eval(input( ))
#    if (year%100) in [0]:
#        if year%400 in [0]:
#            print("Y")
#        else:
#            print("N")
#    elif year%4 in [0]:
#        print("Y")
#    else:
#        print("N")
#        
#jduge_year()    


#def func(n):
#    if n == 0 or n == 1:
#        return 1
#    else:
#        return (n * func(n - 1))
#def cal():
#    s=0
#    n=int(input())
#    while n>0:
#        s+=func(n)
#        n-=1
#    print(s)
#cal()


'''
def sort():
   a=map(int, input().split(" "))
   a=sorted(a)
   print(a[0], a[1], a[2])
sort()
'''


#while y<168-x:
#    if (x/8+(3*y/4)) == 76:    
#        break
#    else:
#        x+=8
#        y-=8
#        
#print(x)
#print(y)

#import time
#
##t = time.strftime("%Y-%B-%d %A %H:%M:%S", time.gmtime())
##print(t)
#st = time.perf_counter()
#time.sleep(1)
#sp = time.perf_counter()
#print(sp-st)


#a=int(input())
#print("{:+>30.3f}".format(pow(a, 0.5)))

##文本进度条
#import time
#scale = 20
#print("{:=^25}".format("任务开始"))
#for i in range(scale+1):
#    a="*"*i
#    b="-"*(scale-i)
#    c=i*100/scale
#    print("{:^3.0f}%[{}->{}]".format(c, a, b))
#    time.sleep(0.1)
#print("{:=^25}".format("任务结束"))

#import time
#for i in range(101):
#    print("\r{:3}%".format(i), end=" ")
#    time.sleep(0.1)


import time
scale=40
print("任务开始".center(scale+4,"="))
t_st=time.perf_counter()
for i in range(scale+1):
    a="*"*i
    d=a+'\\'
    b="-"*(scale-i)
    c=i*100/scale
    dur=time.perf_counter()-t_st
    print("\r{:^3.0f}%[{}{}]{:.2f}s".format(c, d, b, dur), end=" ")
    time.sleep(0.1)
print("任务结束".center(scale+4,"="))

























