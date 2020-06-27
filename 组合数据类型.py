# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 08:43:15 2020

@author: Jahn
"""


"""
组合数据类型
    -集合
        *集合类型定义
            集合是多个数据的无序组合
            集合中的元素是唯一的，不能有相同的元素
            集合中的元素是不可更改的，集合中的元素可以是各种数据类型
        *集合结构
            集合使用"{}"表示，其内的元素使用","分隔
            建立一个集合可以使用{}或set()函数，建立一个空集合必须使用set()函数，因为使用空的
            大括号，即"{}"是用来建立字典类型的变量的
            set()函数会将其内的参数按个赋给一个集合
        *集合操作符
            集合运算：
            | ：二元操作符，或运算            & ：二元操作符，并运算
            - ：二元操作符，差运算            ^ : 二元操作符，补运算
            关系运算符：
            <=,< : 二元运算符，用来判断两个集合的子集关系
            >=,> : 二元运算符，用来判断两个集合的包含关系
            增强集合运算符：
            |=: S|=T  将集合T中含有而集合S中不含有的元素补充集合S
            -=: S-=T  剔除集合S中的T集合含有的元素
            &=: S&=T  求出集合S和集合T共有的元素，并使用它们覆盖掉集合S
            ^=: S^=T  求出集合S和集合T中不共有的元素，并使用它们覆盖掉集合S
        *集合处理方法
            S.add(x): 将元素x添加到集合S中，如果集合中没有该元素的话
            S.discard(x): 移除集合S中的x元素，如果x不再集合中不报错
            S.remove(x): 移除集合S中的x元素，如果x不再集合中将会产生keyError 异常
            S.clear(): 移除集合S中的所有元素
            S.pop(): 随机返回S中的一个元素，同时更新集合S，删除该元素，若S为空则产生KeyError异常
            S.copy(): 返回集合S的一个副本
            len(s): 返回集合的元素个数
            x in S: 判断元素x是否在集合S中，返回值为True和False
            x not in S: 与 x in S 的真值相反
            set(x): 将其它类型的变量转换为集合类型
        *集合类型的特性可被用来进行数据去重，即通过set()函数转换为集合类型，再用list()等
         函数再转换为需要的数据类型
    -序列及其操作
        *序列是具有先后关系的一组元素，可以将其理解为一维元素向量，但各个元素的数据类型可以不同
         但各元素可以相同
        *序列可以通过下标进行访问，可以将字符串类型，元组类型，列表类型看作序列类型的衍生，这几类
         数据类型的操作是通用的，准确的说，序列类型和字符串类型操作通用，但元组类型和列表类型
         在此基础上有所引申
        *序列和字符串一样，存在正向递增，反向递减两种关系
        *序列处理函数和方法
            &6个操作符
                in: x in s 判断元素x是否在序列s中
                not in: x not in s 上一个的反操作
                + : s+t 连接两个序列s和t
                * : s*n或n*s 将序列s复制n次
                s[i]: 索引，返回序列s中的标号为i的元素
                s[i:j[:k]]: 切片操作
            &5个函数和方法
                len(s): 返回序列s的长度
                min(s): 返回序列s的最小元素，这时需要列表s中的元素可以比较
                max(s): 返回序列s的最大元素，这时需要列表s中的元素可以比较
                s.index(x): 返回元素x第一次在列表s中出现的位置(下标)
                s.index(x,i,j): 返回元素x第一次在列表s的i到j的位置中第一次出现的位置
                s.count(x): 返回元素x在序列s中出现的次数
    -元组类型
        *定义
            元组类型是序列的一个衍生，元组一经创建就不能修改，可以认为是一个常量，无法对其修改
            元组使用小括号()或tuple() 创建，元素间使用"," 分割
            元组的小括号可以省略
        *元组类型继承了所有序列类型的操作，但元组不可以被修改，所以可以将一组数据使用tuple()
         函数转换为元组类型，将其保护起来
    -列表类型及其操作
        *列表是一种序列类型，创建后可以任意修改，列表中不可能再有列表
        *一般结构
            列表可以使用"[]"和list()函数创建，元素之间使用","分割
            列表中的各个元素的类型可以不同，且没有长度限制
        *列表类型操作函数和方法
            ls[i]=x: 使用x替换列表ls的标号为i的元素
            ls[i:j:k]=lt: 使用列表lt替换ls切片后对应元素
            的子列表
            del ls[i]: 删除列表ls的标号为i的元素
            del ls[i:j:k]: 删除列表ls中从i到j以k为步长的元素
            ls += lt: 将列表lt中的元素加入到ls中
            ls *= n : 将列表重复n次并更新列表
            对列表的操作：
            ls.append(x): 在列表最后增加一个元素x
            ls.clear(): 删除列表ls中所有的元素
            ls.copy(): 生成列表ls的副本
            ls.insert(i, x): 在列表ls的标号为i的位置后增加元素x
            ls.pop(): 将列表ls的标号为i的元素取出，并在原列表中删除该元素
            ls.remove(x): 删去列表ls中出现的第一个为x的元素
            ls.reverse(): 将列表ls反转
    -字典类型
        *字典类型也是一种变量，一定程度上来说，字典和集合的表示形式有些像，都是"{}"，一般是
         { 原象:象, 原象:象, 原象:象 }
        *字典里面存储的是映射关系，映射关系使用":"表示， 冒号":"左端是原象，冒号右端是象
        *字典内的映射关系是无序的，字典的使用是通过"[]"实现的
        *字典的初始化有两种，一个是在定义时赋予初值，一个是以<字典变量名>[原象] = 象
         的形式逐个给予
        *字典的使用
            索引元素： <象> = <字典变量名>[原象]
            添加映射： <字典变量名>[原象] = 象
        *字典的一般结构
            字典使用大括号"{}"或dict()函数创建
        *字典操作函数和方法
            del d[k]: 删除字典k中的原象k对应的映射关系
            k in d: 判断字典d中是否存在以k为原象的映射关系，返回值是True或False
            d.keys(): 返回字典d中所有的原象(键)
            d.values(): 返回字典d中所有的象(值)
            d.items(): 返回字典d中所有的映射关系信息
          方法：
            d.get(k, default): 在字典中搜索原象为k的映射关系，如果存在，返回它的象，
                               否则，返回default的值
            d.pop(k, default): 取出字典中以k为原象的象，如果不存在，返回default的值
            d.popitem(): 随机从字典d中取出一个映射关系，以元组的形式返回
            d.clear(): 清空字典d
            len(d): 返回字典d的映射关系的个数=
"""


"""
基本统计值
    =总个数： len()
    =求和 ： for ... in ...
    =平均值： 求和/个数
    =方差 ： 各个数据与平均值的差的平方的和的平均数
    =中位数：排序，如果是有奇数个数据就在中间找一个，如果是偶数个数据就找中间两个取平均
    
    type(x):返回x的数据类型
"""

'''
jieba库
    -jieba库是一个优秀的中文分词第三方库
        &分词指的是将连续的中文语段分解为单个的词语
    -jieba库提供三种分词形式
    -jieba库的安装
        使用pip命令工具
        在命令行下键入 pip install jieba
    -jieba库说明
        jieba库分词具有三种模式
        &精确模式
            把文本精确的分开，不存在冗余的单词，常用
        &全模式
            挖掘出一个文本中的字的所有可能词语，会有很多的冗余
        &搜索引擎模式
            在精确模式的基础上，对长词语再次切分，切为短词语
    -jieba库提供的函数
        jieba.lcut(s): 对中文文本(字符串形式)s进行分词，分词结果以列表形式返回, 精确模式
        jieba.lcut(s, cut_all=True):对中文文本(字符串形式)s进行分词，分词结果以列表形式
                                    返回, 全模式
        jieba.lcut_for_search(s):对中文文本(字符串形式)s进行分词，分词结果以列表形式
                                 返回, 搜索引擎模式
        jieba.add_word(w): 向jieba库的词库添加新词的函数
'''

'''
A={"p", "y", 123}
try:
    while True:
        print(A.pop(), end=",")
except:
    pass
print(A)

for item in A:
    print(item, end=",")
'''    


'''
lt=[]
lt[1]=7
lt += [1,2,3,4,5]
lt.assert(2, 6)
del lt[1]
del lt[1:4]
0 in lt
lt.append(0)

lt.index(0)
len(lt)
max(lt)
lt.clear()
'''

'''
def getNum():               #得到用户输入
    nums=[]
    iNumStr=input("请输入数字(回车退出)")
    while iNumStr!="":
        nums.append(eval(iNumStr))
        iNumStr=input("请输入数字(回车退出)")
    return nums

def midNumber(numbers):     #返回列表numbers的平均值
    s=0
    for i in numbers:
        s+=i
    return s/len(numbers)

def dev(numbers, mid):      #返回方差
    s=0.0
    for num in numbers:
        s+=pow(num-mid, 2)
    return pow(s/(len(numbers)-1)), 0.5

sorted()
'''


#哈姆雷特文本词频分析
#获取文本，并将文本归一化(全使用小写，单词与单词间使用空格分隔)
def getText():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()
    for ch in '#|"$%&()*+,-/.:;”<=>?@[\\]^{|}~': #将特殊字符使用空格代替
        txt=txt.replace(ch, " ")
    return txt

#获取文本，以空格分隔开形成以单词为元素的列表
hamletTxt=getText()
words = hamletTxt.split()

#建立字典，原象为单词，象为出现的次数
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1       #建立映射关系，如果字典counts中存在这个值，次数加一，否则创建该映射关系，次数为1

#将字典类型转换为列表类型，并排序
items=list(counts.items())
items.sort( key=lambda x:x[1], reverse=True  )  #将sort方法设置为从大到小排，同时是按第二个元素排序

#输出频率最高的十个单词
for i in range(10):
    word, count=items[i]        
    print("{0:<10}{1:>5}".format(word, count))


'''
import jieba
import time

start=time.perf_counter()
txt=open("threekingdoms.txt","r",encoding="utf-8").read()

words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="玄德" or word=="玄德曰":
        rword="刘备"
    elif word=="孔明" or word=="孔明曰":
        rword="诸葛亮"
    elif word=="丞相" or word=="曹操":
        rword="曹操"
    elif word=="关公" or word=="云长":
        rword="关羽"
    else:
        rword=word
    counts[rword]=counts.get(rword, 0)+1
        
excludes={"将军","却说","二人","不可","荆州","不能","如此"}
for item in excludes:
    del counts[item]
        
items=list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)

for i in range(20):
    word, count=items[i]
    print("{0:<12}{1:>6}".format(word, count))

print( "程序耗时: {:.2f}s".format(time.perf_counter()-start) )
'''

'''
n=set(input())
s=0
for i in n:
    s+=eval(i)
print(s)
'''   

s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖 
       杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙 
       金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍 
       鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰 
       阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰 
       乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王 
       忽必烈 慕容复 张三丰 赵敏 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正 
       李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复 
       逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣 
       洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复 
       黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄 
       张三丰 令狐冲 赵敏 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫 
       洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈 
       完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱 
       郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲 
       谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉 
       双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏 
       逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄 赵敏'''

words=s.split(" ")
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
word, count = items[1]
print("{}".format(word))

















