# 导入其他模块
from day01 import base_type

def def1():
    print('def1')

def def2():
    print('def2')

def def3():
    print('def3')

if __name__ == '__main__':
    def3()
    def1()
    def2()
    # 使用其他模块的方法 (快捷键ctrl+alt+V 如果不能就关闭其他软件 或者手写)
    vaule = base_type.add(80, 80)
    print(vaule)

    #字符串是有序的 索引 0代表第一个字 1代表第二个字 能通过索引取值的就是有序的
    a = '分隔符切豆浆粉'
    print(a[4:])
    print(a[0])
    print(a[1:3])#切片
    print(a[-1])

    # 根据索引取值演示
    print(a[0])
    print(a[-1])

    b = '难受地发动机'
    print(b[2:5])
    print(b[0:5])
    print(b[::-1])
    print(b[0]+b[-1])


    # #数字是无序的 所以报错
    # a = 123
    # print(a[0])

    # 反转
    print(a[::-1])
    print(a[:3:-1])


    list

