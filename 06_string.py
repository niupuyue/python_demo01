# Python的字符串

'''
字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。

创建字符串很简单，只要为变量分配一个值即可
'''

# Python中访问字符串的值

var1 = "abcdefghjiklmn"
print("var1[2] = " + var1[2])
print("var1[1:3] = " + var1[1:3])
del var1

# Python中更新字符串
var1 = "hello world!"
print("更新后的内容：" + var1[:6] + "Python!")
del var1

# Python的转义字符

'''
\ 在行尾 换行符
\\ 反斜杠符号
\' 单引号
\" 双引号
\a 响铃
\b backspace按键
\000 空
\n 换行
\r 回车
\v 纵向制表符
\t 横向制表符
\f 换页
'''

# Python字符串格式化

'''
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
'''
var1 = "ab%sdefghijklmn"
print(var1 % (" hahah "))

'''
1. %c 格式化字符串以及ASCII码
2. 
'''


