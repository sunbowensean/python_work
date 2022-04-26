#   定义函数:

def birthday():
    """发送生日快乐的消息。"""
    print("My birthday is on 9/8.")
birthday()


#   向函数传递信息:

def birthday_1(day):
    """发送生日快乐的消息。"""
    print(f"My birthday is on {day}.")
birthday_1("2010/9/8")


#   形参和实参:

# "2010/9/8"是一个实参，即调用函数时传递给函数的信息。
# 'day'是一个形参，即函数完成工作所需要的信息.


#   传递实参：

# 函数定义中可能包含多个实参，因此函数调用中也可能包含多个实参。
# 可使用位置实参；也可使用关键字实参；还可使用列表和字典。
# 下面依次介绍这些方法


#   位置实参:

# 基于函数实参位置的关联方式被称为位置实参：
def birthday_2(name,day):
    """发送生日快乐的消息。"""
    print(f"{name}'s birthday is on {day}.")
birthday_2("孙博文","2010/09/08")
# 这个函数的定义表明，它需要一个姓名和一个时间，调用“birthday_2”
# 时，需要按顺序提供一个人名和一个日期。


#   关键字实参:
def birthday_3(name,day):
    """发送生日快乐的消息。"""
    print(f"{name}'s birthday is on {day}.")
birthday_2(day = "2010/9/8",name = "孙博文")


#让实参变成可选的
def back_name (first,last,middle = " "):
    print(f"Your name is {first}{middle}{last}")

back_name("孙","文","博")



def f_name (first,last,):
    fn = {"first":first, "last":last}
    return fn

n = f_name("Sun","Bo Wen")
print(n)