# 基本运算符

'''
Python支持的运算符主要从以下几个方面入手
1.算术运算符
2.比较(关系运算符)
3.赋值运算符
4.逻辑运算符
5.位运算符
6.成员运算符
7.运算符的优先级
'''

# 算术运算符

a = 10
b = 21
print("-" * 100)
print("算数运算符")
print("a + b = " + str(a + b))  # 加
print("a - b = " + str(a - b))  # 减
print("a * b = " + str(a * b))  # 乘
print("a / b = " + str(a / b))  # 商
print("a % b = " + str(a % b))  # 取余
print("a // b = " + str(a // b))  # 向下取整

# 算术运算符 跟字符串相结合
c = "hello"
print(c + " world!")
# 字符串之间可以通过+号进行拼接
del a, b, c

# 比较运算符

a1 = 21
b1 = 10
print("-" * 100)
print("比较运算符")
print("a == b : " + str(a == b))
print("a != b : " + str(a != b))
print("a > b : " + str(a > b))
print("a < b : " + str(a < b))
print("a >= b : " + str(a >= b))
print("a <= b : " + str(a <= b))
del a1, b1

# 赋值运算符

a2 = 10
b2 = 21
print("-" * 100)
print("赋值运算符")
a2 += b2
print("a += b : " + str(a2))
a2 -= b2
print("a -= b : " + str(a2))
a2 *= b2
print("a *= b : " + str(a2))
a2 /= b2
print("a /= b : " + str(a2))
a2 %= b2
print("a %= b : " + str(a2))
a2 //= b2
print("a //= b : " + str(a2))
del a2, b2
