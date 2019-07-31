# Python3 标准库概览

# 操作系统接口
'''
OS模块提供了不少于操作系统相关联的函数
'''
import os

print(os.getcwd())  # 返回当前的工作目录

# print(os.chdir("")) # 修改当前的工作目录

'''
这里建议使用import os 而不是 from os import*  这样额看哟你保证随着操作系统的不同而有所变化的os.open()不会覆盖内置函数
在使用os这样的大型模块时内置的dir和help方法也是很有用的
'''

print(dir(os))
print(help(os))

'''
针对日常的文件和目录管理任务，:mod:shutil模块提供了一个易于使用的高级接口
import shutil
shutil.copyfile("data.db","archive.db")
shutil.move("/build/executables","installdir")
'''

# 文件通配符
'''
glob模块提供了一个函数用于从目录通配符中生成文件列表
'''
import glob

print(glob.glob("*.py"))

# 命令行参数
'''
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于sys模块的argv变量中，例如，在命令行中执行pythondemo.py one two three
之后可以得到如下结果
improt sys
print(sys.argv)
['demo.py','one','two','three']
'''

# 正则表达式
'''
re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案
'''
import re
str = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(str)
str = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat');
print(str)
del str

# 数学
'''
math模块为浮点运算提供了对底层C函数库的访问:
'''
import math
print(str(math.cos(math.pi / 4)))

# 互联网

'''
有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从urls接收的数据的urllib.request以及用于发送电子邮件的smtplib
'''
# from urllib.request import urlopen
# for line in urlopen("http://www.paulniu.com/2019/06/06/index.html"):
#     line = line.decode('utf-8')
#     if 'EST' in line or 'EDT' in line:
#         print(line)

# 日期和时间

'''
datetime模块为日期和时间处理同时提供了简单和复杂的方法
支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。同时还支持时区处理
'''
# dates format
import datetime
now = datetime.date.today()
print(now)
# 将时间格式化
print(now.strftime("%m-%d-%y.%d %b %Y is a %A on the %d day of %B."))

# 计算时间
birthday = datetime.date(1992,6,29)
age = now - birthday
print(age.days)
print(age.seconds)
# 今天
today = datetime.date.today()
# 昨天
yesterday = today - datetime.timedelta(days=1)
# 上个月
last_month = today.month - 1 if today - 1 else 12
# 当前时间戳


# 数据压缩
'''
通过各自的模块支持通用的数据打包和压缩格式:zlib,gzip,bz2,zipfile，tarfile
'''
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))
