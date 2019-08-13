# 循环语句
# Python的循环语句分为两种，for和while循环

'''
while循环，需要注意冒号和缩进，在Python中没有do...while 循环
下面一个例子，计算100以内数字的和
'''
n = 100
sum = 0
while n > 0:
    sum += n
    n -= 1
print("100以内数字的和是：%d" % (sum))

# 无限循环
# 我们可以通过设置表达式的值永远不为false，来实现一个无限循环

# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
#
# print("Good bye!")

# while循环中使用else语句
# 在while...else语句中，当条件判断为false的时候，执行else代码块

# for语句
# for语句可以遍历任何序列的项目，可以是一个列表或者一个字符串
languages = ["C", "C++", "Java", "Kotlin", "Python"]
for item in languages:
    print(item)

# 在for循环中我们可以使用break语句表示跳出当前循环体，如下
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    if num >= 5:
        break
    print("当前数字是%d" % num)
else:
    print("退出循环了")
# range()函数
# 如果我们需要遍历数字列表，我们可以使用内置函数range()，他会生成数列，如下所示

for i in range(10):
    print("当前的数字是%d" % i)

# 同样我们可以指定遍历数字列表的范围
for ii in range(2,6):
    print("当前的数字是%d" % ii)

# 我们可以指定遍历数字列表的步长
for iii in range(1,20,3):
    print("当前的数字是%d" % iii)




