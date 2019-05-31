def  if_demo():
    a = 3>4

    if a :
        print('a 是 True')
    else:
        print('a 是 Flase')

    b = 100*7>99*7
    if b :
        print('b 是 True')
    else:
        print('b 是 Flase')

def elif_demo():
    a =7
    # =是赋值 , == 是 判断相等
    if a==1: # 判断 a是否等于1
        print('a是1')
    elif a==2: # 判断 a是否等于2
        print('a是2')
    elif a==3: # 判断 a是否等于3
        print('a是3')
    elif a==4: # 判断 a是否等于4
        print('a是4')
    else:
        print('a不是1,2,3,4')


if __name__ == '__main__':
    # if_demo()
    elif_demo()