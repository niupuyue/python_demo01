# Python的输入输出



# 验证向文件中输入内容

'''
str = input("请输入您想要输入的内容\n")

f = open("test.txt","w")
f.write(str)
f.close()
'''

# 读取文件中的内容

'''
f = open("test.txt","r")
ss = f.read()
print(ss)
'''

# 打开一个网页，并将网页中的内容输入到文件中
from urllib import request
response = request.urlopen("http://www.baidu.com")
f = open("test.txt","w")
f.write(str(response.read()))
f.close()

# 清空文本中的内容
ff = open("test.txt","w")
ff.write("")
ff.close()