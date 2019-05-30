# 这就是一个列表的数据类型,英文 是 list, 也叫 数组

alist = ['是打发',2,'你好',6,7,1,3]

# 访问list
def list_sel():
    #通过索引访问
    print(alist[0])

    #访问倒数第三位
    print(alist[-3])

    #通过切片访问
    print(alist[2:3])

    #访问 从第五个开始到最后面
    print(alist[4:])

    # 不填值的话  从第一个开始取值
    print(alist[:4])

# 删除list中的元素
def list_del():
    # 调用删除方法 不填参数 默认删除最后一位
    alist.pop()
    print(alist)
    # 调用删除方法, 填写参数: 索引值    就可以删除指定元素
    a=alist.pop(3)
    print(alist)
    print(a)

# 增加list中的元素
def list_add():
    blist = [1,2,3,'4']
    #增加元素 ,增加在末尾
    blist.append('你好')
    print(blist)

    clist = [4,5,6]
    # 合并两个list 中的元素
    blist.extend(clist)
    print(blist)

    # blist.append(clist)
    # print(blist)


def list_update():
    qlist = [1,2,6,4,5]
    # 更新列表中的元素 , 根据索引进行更新,值写在= 后面 就可以了
    qlist[0] = 100
    # qlist[0:2] = [100,99]
    print(qlist)

    #更新第三位 ,改为200
    qlist[2] = 200
    print(qlist)

def list_order_by():
    qlist = [1, 2, 6, 4, 5]
    # 从小到大排序
    qlist.sort()
    print(qlist)
    # 从大到小排序
    qlist.sort(reverse=True)
    print(qlist)

if __name__ == '__main__':
    list_sel()
    list_del()
    list_add()
    list_update()
    list_order_by()