# -*- coding: utf-8 -*-
"""
Spyder Editor Jahn

This is a temporary script file.
"""



"""
注释：
-单行注释 # 
-多行注释  
-快捷键 ctrl+1
"""


"""
赋值符号    = 
    -赋值符号用来给变量赋予新的数据值
    -赋值语句右侧的数据类型同时作用于变量
    
命名规则：
    使用字母大小写，数字，下划线，汉字及其组合作为变量名
    注意：大小写敏感，首字符不能是数字，变量名不能与保留字相同

关键字：
    and or not as assert  break  class  continue  def  except  finally  for  while
    from if else elif import in is lambda pass raise return try with yield del
    global nonlocal True False None

字符串的序号定义：
    -正向递增序号：最左端为序号 0，向右依次递增
    -反向递减序号：最右端为序号-1，向左依次递减
    
字符串的使用
    -索引：返回字符串的单个字符： 字符串变量名[M]
    -切片：返回字符串中的一段字符串：字符串变量名[M: N](取出第M, M+1, ...直到第N个字符前的字符)
           [1: 3]：取出标号1，2的元素

列表类型的数据：
    -列表使用 [] 表示，采用逗号 , 分隔各元素(元素可以是多种类型)                                  
    -可以使用关键字 in 判断一个元素是否在列表中，返回值是True 和 False
            s[-1] in ["Y", 'C']
            
分支语句：
    -由判断条件决定程序运行方向的语句
    -使用关键字if elif else 构成
            if s[-1] in ["C", 'c']:
            如果条件为真，则运行冒号后带有缩进的语句，如果条件不成立，则跳过冒号及其以后的程序
            
函数：
    -根据输入参数产生不同的输出结果
    -由一个名字和一个括号组成：<函数名>( 参数 )
            input(  )
            
input()函数  输入函数
    -从控制台得到用户输入
    -一般使用方式：<变量> = input( <提示信息字符串> ) 返回值类型是字符串
    -用户输入的信息以字符串类型保存在 <变量> 中
    
print()函数  输出函数
    -一般使用方式：print( <想输出的字符串或字符串变量> )
    -格式化操作方法：在print函数的输出字符串中加入槽 {}(后续变量会填充到槽中) 
                    也常用到  :.2f  来将小数取到小数点后两位        

eval()函数  评估函数
    -去掉参数最外侧引号并执行余下语句
    -可用于字符串向变量的变化
    -eval("1") ==> 1    eval("1+2") ==> 3    eval('"1+2"') ==> "1+2"   eval("print("Hello")") ==> Hello
    

    
"""

a = input()
b = a.replace(" "," ")
c = eval(b)
print("{:.2f}".format(c))



