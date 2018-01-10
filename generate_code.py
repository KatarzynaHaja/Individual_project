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
import imp

import random

from pyfuzz_master.pgen import pgen_opts, ProgGenerator
from pyfuzz_master.pygen.cgen import CodeGenerator
import codes.neww
import result_code
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
    main.append("from " + re.sub(".py", "", package + "." + file) + " import *\n")
    for i in m:
        if i != "":
            if "for" not in i:
                main.append(re.sub(" ", "", i))
    return code, main

def create_unittest(code,r):
    content = []
    content.append('import unittest \n')
    content.append(code[0]+ '\n')
    content.append('class MyTest(unittest.TestCase): \n')
    for i in range(1,len(code)):
        content.append('    def test'+ str(i) + '(self):\n')
        content.append('        self.assertEqual(' + code[i] + ',' + str(r[i-1])+')\n')
    return content


def generate_code(f,u,seed =43):
    code, main = parse_code(f,seed)
    file = open(f,'w')
    file.write(code)
    file.flush()
    os.fsync(file)
    m = []
    m.append(main[0] + '\n')
    m.append('def result():\n')
    m.append('    z=[]\n')
    for i in main[1:]:
        m.append('    z.append('+i+')\n')
    m.append("    return z")

    file1 = open("result_code.py", "w")
    file1.writelines(m)
    file1.flush()
    os.fsync(file1)
    imp.reload(codes.neww)
    imp.reload(result_code)

    r = result_code.result()

    d = create_unittest(main,r)
    with open(u,'w') as file:
        file.writelines(d)
        file.close()



generate_code("codes/neww.py","test_package/unit.py")
