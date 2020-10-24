import random


def caishuzi():
    cusor = random.randint(1, 100)
    num = 0
    while True:
        s = input(">")
        if int(s) > cusor:
            print("大")
            num += 1
        elif int(s) < cusor:
            print("小")
            num += 1
        else:
            break
    print(num)


def cf():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("%d*%d=%d" % (j, i, i * j), end='\t')
        print("")


def sxhs():
    for s in range(100, 1000):
        g = s % 100
        sw = s // 10 % 10
        bw = s // 100
        n = g ** 3 + sw ** 3 + bw ** 3
        if n == s:
            print(n)


def jj():
    for g in range(1, 20):
        for m in range(1, 30):
            if 5 * g + 3 * m + (100 - g - m) / 3 == 100:
                print("%d,%d,%d" % (g, m, (100 - g - m)))


def CRAPS():
    total=1000
    sz = random.randint(1, 12)
    next = False
    while total > 0:
        if sz == 7 or sz == 11:
            total += 100
            next = False
            print("赢,金额%d" % ( total))
        elif sz == 2 or sz == 3 or sz == 12:
            total -= 100
            next = False
            print("输,金额%d" % (total))
        else:
            next = True
            while next:
                sz2 = random.randint(1, 12)
                if sz2 == 7:
                    total -= 100
                    next = False
                    print("赢金额%d" % (total))
                elif sz2 == sz:
                    total += 100
                    next = False
                    print("输金额%d" % (total))
                else:
                    next = True


# 斐波那契数列
def fbnqsl():
    ls=[1,1,2]
    num=len(ls)
    while num <=100 :
        nextNum=ls[num-1]+ls[num-2]
        ls.append(nextNum)
        num=len(ls)
    print(ls)




def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        print("值：%d"%(a))
        yield a


def main():
    for val in fib(20):
        print("值11：%d"%(val))
        print(val)



import  os
import  time
def pmd():
    str="123456789"
    while True:
        os.system('cls')
        print(str)
        time.sleep(0.5)
        str=str[1:]+str[0]
