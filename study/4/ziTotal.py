import os
import collections

def total(file):
    a=""
    with open(file,'r',encoding="utf-8") as f:
        line=f.readline()
        while line:
           a+=""+line
           line=f.readline()
    b=collections.Counter(a)
    print(b)

total(os.getcwd()+"\\zf")
