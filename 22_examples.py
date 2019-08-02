# 部分示例展示

# 1.hello world 示例
# print("-" * 200)
# print("1. hello world示例")
# print("hello world!")
# print("hello python!")

# 2.数字求和
# 要求用户输入两个数字，并求出两个数字的和
# 实现
# isbreak = 1
# while isbreak:
#     sum1 = input("请输入第一个数字")
#     sum2 = input("请输入第二个数字")
#     if sum1.isdigit() and sum2.isdigit():
#         isbreak = 0
#     else:
#         print("请输入正确的数字，输入字母或者符号是无效的哟")
# sum = float(sum1) + float(sum2)
# print("求和的结果是：" + str(sum))

# 3.平方根
# 平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16=4。语言描述为：根号下16=4。
# 实现 这个是只能用于正数
# iskeepgoing = 1
# while iskeepgoing:
#     square = input("请输入您需要开平方根的数字")
#     if square.isdigit():
#         iskeepgoing = 0
#     else:
#         print("请输入正确的数字o(╯□╰)o")
# square_root = float(square) ** 0.5
# # 这里我们要求只保留小数点后3位小数
# print(' %0.3f  的平方根是  %0.3f ' % (float(square), float(square_root)))
# 实现 可以适用于负数或者复数
# import cmath
# isbreak = 1
# while isbreak:
#     square = input("请输入您需要开平方的数字")
#     if square.isdigit():
#         square = float(square)
#         isbreak = 0
#     else:
#         print("请输入正确的数字o(╯□╰)o")
# square_root = cmath.sqrt(square)
# print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(square ,square_root.real,square_root.imag))

# 4.二次方程
# 二次方程的一般格式为ax**2 + bx + c = 0，我们这里要求用户传入a,b,c的值，然后计算出x的值
# 需要导入cmath模块
# import cmath
# a = float(input("请输入a的值：\n"))
# b = float(input("请输入b的值：\n"))
# c = float(input("请输入c的值：\n"))
# # 计算
# d = (b ** 2) - (4 * a * c)
# # 两种求解方式
# sol1 = (-b - cmath.sqrt(d)) / (2 * a)
# sol2 = (-b + cmath.sqrt(d)) / (2 * a)
# print("结果为{0} 和 {1}".format(sol1, sol2))

# 5.计算三角形的面积
# 需要用户输入三角形的三条边长，然后计算出三角形的面积
# a = float(input("请输入第一条三角形的边\n"))
# b = float(input("请输入第二条三角形的边\n"))
# c = float(input("请输入第三条三角形的边\n"))
# # 计算半周长
# s = (a + b + c) / 2
# # 计算面积
# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# print("三角形的面试为%0.2f" % area)

# 6.计算圆的面积
# 需要用户输入圆的半径
# import math
# isbreak = 1;
# while isbreak:
#     r = input("请输入圆的半径\n")
#     if r.isdigit():
#         isbreak = 0
#     else:
#         print("请输入数字哟")
# radius = float(r)
# res = radius ** 2 * math.pi
# print("求圆的面积为%0.3f" % res)

# 随机数
# 随机获得0-9的随机数
# import random
# print(random.randint(0, 9))

# 随机数字小游戏
# import random
# i = 1
# a = random.randint(0,100)






