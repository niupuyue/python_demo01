# coding=utf-8
# 变量类型

'''
变量就二十存储在内存中的值，这意味着创建变量就要在内存中开辟一个空间
基于变量的数据类型，解析器会分配指定的内存，并决定是什么数据可以存储在该内存中
因此变量可以指定不同的数据类型，可以是整数，小数，字符等
'''

# 变量赋值

'''
Python中变量赋值不需要类型声明
每个变量在内存中创建，都包括变量的标识，名称和数据这些信息
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
等号(=)用来变量赋值
'''
counter = 100  # 赋值整型变量
mails = 10.01  # 赋值浮点类型
values = 'hello world'  # 赋值字符类型

print(counter)
print(mails)
print(values)

# 多个变量赋值
a, b, c = 1, 10.2, 'paulniu'

print(a, b, c)

# 标准数据类型

'''
在内存中存储的数据可以有多种类型，例如，一个人的年龄可以用数字表示，姓名用字符表示
为了方便，在Python中定义了一些标准类型，用于存储各种类型的数据
1. Numbers(数字)
2. String(字符串)
3. List(列表)
4. Tuple(元组)
5. Dictionary(字典)
'''

# 数字
'''
数字数据类型用于存储数值
他们是不可改变的数据类型，意味着改变数字数据类型会分配一个新的对象
'''
var1 = 1
var2 = 10
# 同时我们可以使用del语句删除一些对象的引用
del var1
'''
Python支持4中不同的数字类型
int
long
float
complex(复数)
'''

# 字符串
print("-----------------------------------------------------------------")
ss = "hello world!"
print(ss)  # 输出完整字符串
print(ss[0])  # 输出字符串中第一个字符
print(ss[2:5])  # 数组字符串中第三个和第六个之间的字符串
print(ss[2:])  # 输出字符串中第三个开始后面的字符串
print(ss * 2)  # 输出字符串两次
print(ss + "test")  # 输出拼接字符串
print(ss[-4:])
print(ss[-4:4])

# 设置步长
print("-" * 100)
ss1 = "abcdefghijklmnopqrstuvwxyz"
print(ss1[0:20:2])

# 列表拼接

ss2 = ["hello", "world", "!"]
ss3 = [100, "python", "!"]
ss4 = "paulniu"
print("-" * 100)
print(ss2 + ss3)

# 元组

'''
元组相当于list列表，但是只能赋值一次，不能再次修改
'''
print("-" * 100)
ss5 = ("hello", "world", "!", 100);
print(ss5)

# 字典
print("-" * 100)
ss6 = {"key1": "value1", "name": "paulniu", "age": 27, 100: "classname", 101: 10001}
print(ss6)

# Python基本数据类型的转化

'''
int(x) 将数据转成int类型
long(x) 将数据转成long类型
float(x) 将数据类型转成float类型
complex(x) 创建一个复数
str(x) 将数据类型转成String类型
repr(x) 将对象转化为供解释器读取的形式
eval() 用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s) 将序列 s 转换为一个元组
list(s) 将序列 s 转换为一个列表
set(s) 转换为可变集合
dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s) 转换成不可变
chr(x) 将一个整数转换为一个字符
unichr(x) 将一个整数转换为Unicode字符
ord(x) 将一个字符转换为它的整数值
hex(x) 将一个整数转换为一个十六进制字符串
oct(x) 将一个整数转换为一个八进制字符串
'''
print("-" * 100)
print(int(4))
