# 全局变量
a = 5
# def: 声明方法的关键字 ;int_demo: 方法的名字; ():下面写方法的内容
def int_demo():
    # 声明一个变量=前面是变量名 aint, = 后面是变量值,int类型的5 (变量名可以任意取名)
    aint = 5

    # type(aint) : 获取 aint的数据类型(变量类型), print: 打印出他的类型
    print(type(aint))

# def: 声明方法的关键字 ;str_demo: 方法的名字; ():下面写方法的内容
def str_demo():
    # 声明一个变量=前面是变量名 astr, = 后面是变量值,str类型的5 (变量名可以任意取名)
    astr = '5'

    # type(astr) : 获取 astr的数据类型(变量类型), print: 打印出他的类型
    print(type(astr))

def zhengshu():
    xyz = 5
    print(type(xyz))
def zifuchuan():
    qua = '5'
    print(type(qua))


def float_demo():# 局部变量
    afloat = 1.1
    print(type(afloat))
    print(a)

def fjk():
    sss = 5.5
    print(type(sss))
# 字符串 转换成 数字类型
def type_zhuanhuan():
    b = '100'
    print(type(b))
    # int(b) : 将b的类型转换成int
    b = int(b)
    print(type(b))

def type_nihao():
    a = 200
    # str(b) : 将b的类型转换成str
    print(type(a))
    a = str(a)
    print(type(a))

# 字符串拼接
def str_jion():
    a = 123
    b = '哈哈哈'
    c = '嘻嘻嘻'
    # 如果两个变量都是字符串类型,直接用 + 连接
    print(b+c)

    # 如果有其他类型 ,第一种: 需要用 str() 方法转换成str 类型才能用 + 连接
    print(str(a)+b)

    # 第二种: %s : 这是占位符 ,
    print('a是 %s , b是 %s'%(a,b))


def ddddd():
    x = 666
    y = '好的'
    z = '知道'
    print(y+z)
    print(str(x)+y)
    print('%s%s%s'%(y,x,z))

# 方法中括号里面的东西 叫 参数, 多个参数用 , 分隔开
def add(num1,num2):
    print(num1)
    print(num2)
    print(num1+num2)
    # 方法执行到 return 就返回return后面的内容 (可以填return(x,y,z))
    return num1+num2

#这是一个main方法,可以直接执行,main方法下面不能再有其他方法
if __name__ == '__main__':
    #打印
    print('Hello World')


    # 声明一个变量=前面是变量名 aint, = 后面是变量值,int类型的5 (变量名可以任意取名)
    aint = 5

    # type(aint) : 获取 aint的数据类型(变量类型), print: 打印出他的类型
    print(type(aint))

    astr = '5'

    print(type(astr))
    # 方法的调用 : 写方法的名字就行,加上()
    int_demo()
    str_demo()
    zhengshu()
    zifuchuan()

    float_demo()
    fjk()

    type_zhuanhuan()
    type_nihao()

    str_jion()
    ddddd()

    # str_jion() 没有返回值,所以 a 的值 就是 None
    a = str_jion()

    # add(5,30) 是有返回值的 , 所以 b 的值就是 35
    b = add(5,30)
    print('-----------')
    print(a)
    print(type(a))
    print(b)