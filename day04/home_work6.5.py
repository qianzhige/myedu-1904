#冒泡排序
def paixu():
    alist=[3,2,1,5,4,9,6,7,8]


    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j]>alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp

    print(alist)


if __name__ == '__main__':
    paixu()

