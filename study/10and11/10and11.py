import os

jh=[]
with open('cihui','r',encoding='UTF=8') as file:
    line=file.readline()
    while line:
        jh.append(line.replace("\n",""))
        line=file.readline()

print(jh)

a=input("input:")

for j in jh:
  if a.find(j)>=0:
      a=a.replace(j,len(j)*"*")

print(a)
