# 面向对象

'''
面向对象技术介绍
1.类：用来面试具有相同属性和相同方法的对象的集合，它定义了该集合中每个对象所共有的属性和方法，对象是类的实例
2.方法：类中定义的函数
3.类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中切函数体之外。类变量通常不错为实例变量使用
4.数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据
5.方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个改写的过程就是方法的覆盖，也叫方法的重写
6.局部变量：定义在方法中的变量，只作用于当期实例的类
7.实例变量：在类的声明中，属性是用变量表示的，这种变量就成为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的
8.继承：即一个派生类继承基类的字段和方法，继承也允许把一个派生类的对象作为一个基类对象对待
9.实例化：创建一个类的实例，类的具体对象
10.对象：通过类定义的数据结构实例。对象包括两个数据成员(类变量和实例变量)和方法

Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用积累中的同名方法
对象可以包含任意数量和类型的数据
'''


# 类定义
class Student:
    '''一个简单的类对象'''
    name = ""
    age = 20

    def f(self):
        return 'hello world'


# 类对象
'''
类对象支持两种操作：属性引用和实例化
属性引用使用和Python中所有的属性引用一样的标准语法：obj.name
类对象创建后，类命名空间中所有的命名都是有效属性名
'''
x = Student()
x.name = "张三"
x.age = 29
print(x)  # 这样返回的是内存地址对象

'''
类有一个名为__init__()的特殊方法(构造方法)，该方法在类实例化是会自动调用，如下
def __init__(self):
    self.data = []
类定义了__init__()方法，类的实例化操作会自动调用__init__()方法。如果我们通过Student()创建实例化对象，那么构造方法就会自动执行
当然，__init__()方法可以有参数，参数通过__init__()传递到类的实例化操作上，如
'''


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


x = Dog("puppy", 3)
print(x)

'''
self代表类的实例，而非类
类的方法与普通函数只有一个特别的区别：他们必须有一个额外的第一个参数名称，按照惯例他的名称是self
'''


class Class:
    def prt(self):
        print(self)
        print(self.__class__)


c = Class()
c.prt()

'''
self代表的是类的实例，代表当前对象的地址，而self.class则指向类
self不是Python的关键字，我们把它可以换成别的字符串
'''

# 类的方法
'''
在类的内部，使用def关键字来定义一个方法，与一般函数的定义不同，类方法必须包含参数self，且作为第一个参数，self代表的是类的实例
'''


class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说：我 %d 岁了" % (self.name, self.age))


# 实例化类
p = People("paulniu", 27, 65)
p.speak()

# 继承
'''
继承我们是通过（）的方式来说明继承关系的。
这里我们通过一个单继承的实例来看一下
'''


class Teacher(People):
    className = "语文"

    def __init__(self, n, a, w, c):
        # 调用父类的构造方法
        People.__init__(self, n, a, w)
        self.className = c

    # 覆盖父类的方法
    def speak(self):
        print("%s 说：我 %d 岁了,我教的是科目是 %s" % (self.name, self.age, self.className))


t = Teacher("董仲舒", 100, 60, "古文")
t.speak()

# 多继承
'''
需要注意的是继承父类的顺序，若父类中有相同的方法名，而在子类使用时未指定，则Python从左到右一次搜索，即方法在子类中未找到时，从左到右查找父类中是否包含该方法
'''


class Speaker():
    topic = ""
    realName = ""

    def __init__(self, n, t):
        self.realName = n
        self.topic = t

    def speak(self):
        print("%s 讲话的主题是 %s" % (self.realName, self.topic))


class Sample(Speaker, Teacher):
    a = ""

    def __init__(self, n, a, w, g):
        Teacher.__init__(self, n, a, w, c)
        Speaker.__init__(self, n, t)


s = Sample("lili", 25, 60, "Python")
s.speak()

# 方法重写
'''
如果父类方法的功能不能满足需要，我们可以在子类中重写父类的方法
'''


# !/usr/bin/python3

class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法

'''
super()函数是用于调用父类(超类)的一个方法
'''

# 类属性和方法
'''
类的私有属性
__private_attrs:两个下划线开头，表名当前属性为私有属性，不能在类的外部被使用或者直接访问。在类内部的方法中使用也要通过self.__private_attrs的方式
类的方法
在类的内部，使用def关键字来定义一个方法，与一般的函数定义不同，类方法必须包含参数self，且为第一个参数，self代表的是类的实例
self的名字并不是规定死的，我们也可以使用this，但是最好还是用约定的self
类的私有方法
__private_method:两个下划线开头，声明该方法为私有方法，只能在类的内部调用，不能在类的外部调用，在类的内部调用的时候使用过的是self.__private_method
'''

# !/usr/bin/python3

# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量


# 类的私有方法实例
# !/usr/bin/python3

# class Site:
#     def __init__(self, name, url):
#         self.name = name  # public
#         self.__url = url  # private
#
#     def who(self):
#         print('name  : ', self.name)
#         print('url : ', self.__url)
#
#     def __foo(self):  # 私有方法
#         print('这是私有方法')
#
#     def foo(self):  # 公共方法
#         print('这是公共方法')
#         self.__foo()
#
#
# x = Site('菜鸟教程', 'www.runoob.com')
# x.who()  # 正常输出
# x.foo()  # 正常输出
# x.__foo()  # 报错

# 类的专有方法
'''
1.__init__:构造方法，在生成对象时调用
2.__del__:析构函数，释放对象的时候调用
3.__repr__:打印，转换
4.__setitem__:按照索引赋值
5.__getitem__:按照索引获取值
6.__len__:获取长度
7.__cmp__:比较运算
8.__call__:函数调用
9.__add__:加运算
10.__sub__:减运算
11.__mul__:乘运算
12.__truediv__:除运算
13.__mod__:求余运算
14.__pow__:乘方
'''


# 运算符重载

# !/usr/bin/python3

# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)


# 一些小demo

# 1.针对__str__方法
class Class1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "这个人的名字是%s，目前已经%d岁了" % (self.name, self.age)


cc = Class1("mafei", 27)
print(cc)

# 在Python3.7之后的版本，对类的构造函数进行了精简
'''
from dataclasses import dataclass
@dataclass
class A:
  x:int
  y:int
  def add(self):
    return self.x + self.y
相当于之前的
class A:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def add(self):
    return self.x + self.y    
'''

# 静态方法，普通方法，类方法
'''
1.静态方法：用@staticmethod修饰不带self参数的就是静态方法，类的静态方法可以没有参数，直接通过类名调用
2.普通方法：默认有一个self参数，只能通过对象调用
3.类方法：默认有一个cls参数，可以被类和对象调用，需要加上@classmethod修饰器
'''
class ClassName:
    @staticmethod
    def fun():
        print("我是静态方法")

    @classmethod
    def a(cls):
        print("我是类方法")

    #普通方法
    def b(self):
        print("我是普通方法")

ClassName.a()
ClassName.fun()

cc = ClassName()
cc.fun()
cc.a()
cc.b()






