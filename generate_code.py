# import os
# import subprocess
# def generate_code(f):
# 	s = "python pyfuzz-master/pgen-example.py > %s" % f
# 	os.system(s)
# 	r = subprocess.check_output(["python", "pyfuzz-master/pgen-example.py"])
# 	print(r)
# 	return r
# generate_code("hh.py")


from __future__ import print_function
import re
import importlib
import os

import random

from pyfuzz_master.pgen import pgen_opts, ProgGenerator
from pyfuzz_master.pygen.cgen import CodeGenerator
from codes.neww import *
from result_code import result
import time
def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return [int(index), int(index+len(char))]

            index += 1

    return -1


def parse_code(f,seed = 43):
    package, file = f.split("/")
    random.seed(seed)
    pgen = ProgGenerator(pgen_opts, random.Random())
    m = pgen.generate()
    cgen = CodeGenerator()
    g = cgen.generate(m)
    position = find_str(g, 'if __name__ == "__main__":')
    code = g[0:position[0]]
    called = g[position[1]:len(g)]
    m = called.split("\n")
    main = []
    main.append("from " + re.sub(".py", "", package + "." + file) + " import *")
    for i in m:
        if i != "":
            if "for" not in i:
                main.append(re.sub(" ", "", i))
    return code, main

def create_unittest(code):
    content = []
    content.append('import unittest \n')
    content.append(code[0]+ '\n')
    content.append('class MyTest(unittest.TestCase): \n')
    print(len(code))
    print("kod",code)
    for i in range(1,len(code)):
        print(code[i])
        content.append('    def test'+ str(i) + '(self):\n')
        content.append('        self.assertEqual(' + code[i] + ',' + str(eval(code[i]))+')\n')
    return content


def generate_code(f,u,seed =43):
    code, main = parse_code(f,seed)
    print(main)
    with open(f,'w') as file:
        file.write(code)
        file.close()


    m = []
    m.append(main[0] + '\n')
    m.append('def result():\n')
    m.append('    z=[]\n')
    for i in main[1:]:
        m.append('    x =' + i + '\n')
        m.append('    z.append(x)\n')
    m.append("    return z")


    with open("result_code.py", 'w') as file:
        file.writelines(m)
        file.close()


    d = create_unittest(main)
    with open(u,'w') as file:
        file.writelines(d)
        file.close()



generate_code("codes/neww.py","test_package/unit.py")
