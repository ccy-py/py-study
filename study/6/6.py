import os
import collections


def readFile(files):
    for file in files:
        if os.path.isfile(os.getcwd() + "\\test\\" + file):
            with open(os.getcwd() + "\\test\\" + file, 'r', encoding='UTF-8') as f:
                line = f.readline()
                res = {}
                text=""
                while line:
                    for s in line.replace("\n","").split(" "):
                        if res.get(s):
                            res[s]=res.get(s) + 1
                        else:
                            res[s]=1
                    text=text+line
                    line = f.readline()
            print(res.items())
            print(max(res.items(),key=lambda x:x[1]))
            print(collections.Counter(text))


files = os.listdir(os.getcwd() + "\\test")
readFile(files)
