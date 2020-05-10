"""
Mypy是Python的可选静态类型检查器。您可以在Python程序中添加类型提示（PEP 484），
并使用mypy进行静态类型检查。查找程序中的错误，甚至不运行它们！

"""

# 参数name后面跟了:str 代表name期望是str类型
# 参数括号后面跟了->str代表返回类型为str类型
def greeting(name: str) -> str:
    return 'Hello ' + name
x: str = 'xxx' # 声明一个变量为str类型
greeting(x) # Hello xxx
# greeting(123) # TypeError: can only concatenate str (not "int") to str

"""
参数传递；可变对象、不可变对象、可变对象作为默认参数
"""

def flist(l=[1,]):
    """
    因为l 是可变对象，所以每次操作都是此列表操作。
    :param l:
    :return:
    """

    l.append(1)
    print(l)

flist()
flist()
print(flist.__defaults__)

"""
*args **kwargs
"""
def print_all(a, *args, **kwargs):
    print(a)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

print_all('hello', 'world', name='Sky')