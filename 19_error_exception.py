# 错误和异常

# 异常
'''
即便Python的语法是正确的，在程序运行的过程中依然会报一些错误。那么运行时检查到的错误，就成为异常
大多数的异常是不会被程序处理的，而是以错误信息的形式展现出来
异常以不同的类型出现，这些类型都作为信息的一部分打印出来: 例子中的类型有 ZeroDivisionError，NameError 和 TypeError。
错误信息的前面部分显示了异常发生的上下文，并以调用栈的形式显示具体信息。
'''

# 异常处理
'''
例如：我们写一个程序，要求用户输入一个合法的整数，但是我们可以通过执行exit()方法让程序强制退出，或者使用command+c的方式。那么这时候用户中断程序就会抛出一个KeyboardInterrupt异常
'''
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again   ")
'''
try语句按照如下方式工作；
1. 首先，执行try子句（在关键字try和关键字except之间的语句）
2. 如果没有异常发生，忽略except子句，try子句执行后结束。
3. 如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。最后执行 try 语句之后的代码。
4. 如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
'''
