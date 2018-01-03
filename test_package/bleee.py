import importlib
from os import listdir
from os.path import isfile, join
import os
import re
onlyfiles = [f for f in listdir("../mut") if isfile(join("../mut", f))]
print(onlyfiles)
os.chdir("../mut")
for i in onlyfiles:
    module = "mut." + re.sub(".py","",i)
    blee = importlib.import_module(module)
    print(blee.operator())
os.chdir("../test_package")
print(os.getcwd())

with open("tests.py") as file:
    f = file.readlines()
    lines = list()
    # for j in onlyfiles:
    #     j= re.sub('.py', "",j)
    for i in f:
        if re.search('from test_package',i):
            i = re.sub('from test_package' , 'from mut', i)
        if re.search('foo',i):
            i = re.sub("foo",'M0test',i)
        lines.append(i)

with open('tests1.py', "w") as file:
    for line in lines:
        file.write(line)

