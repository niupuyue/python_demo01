# 字典


# 例子
students = {}

write = 1
while write:
    name = str(input("请输入学生姓名"))
    age = int(input("请输入学生年龄"))
    students[str(name)] = age
    write = int(input("是否继续? \n 1/继续  0/结束 \n"))
# 输出最终结果
for key, value in students.items():
    if value > 90:
        print("%s    %s    A".center(20, "-") % (key, value))
    elif value >= 60 and value <= 90:
        print("%s    %s    B".center(20, "-") % (key, value))
    elif value < 60:
        print("%s    %s    C".center(20, "-") % (key, value))


# 字典中key和value的遍历