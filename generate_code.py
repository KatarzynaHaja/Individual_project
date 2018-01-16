from __future__ import print_function

import random
import re

import codes.neww
import codes.result_code
from get_result import *
from pyfuzz_master.pgen import pgen_opts, ProgGenerator
from pyfuzz_master.pygen.cgen import CodeGenerator


class Generate_code:
    def __init__(self):
        pass

    def find_str(self,s, char):
        index = 0

        if char in s:
            c = char[0]
            for ch in s:
                if ch == c:
                    if s[index:index+len(char)] == char:
                        return [int(index), int(index+len(char))]

                index += 1

        return -1


    def parse_code(self,seed = 43):
        random.seed(seed)
        pgen = ProgGenerator(pgen_opts, random.Random())
        m = pgen.generate()
        cgen = CodeGenerator()
        g = cgen.generate(m)
        position = self.find_str(g, 'if __name__ == "__main__":')
        code = g[0:position[0]]
        called = g[position[1]:len(g)]
        m = called.split("\n")
        main = []
        for i in m:
            if i != "":
                if "for" not in i:
                    main.append(re.sub(" ", "", i))
        self.main = main
        self.code = code
        return code, main

    def create_unittest(self,r, file):
        package, file = file.split("/")
        content = []
        content.append('import unittest \n')
        content.append("from " + re.sub(".py", "", package + "." + file) + " import *\n")
        content.append('class MyTest(unittest.TestCase): \n')
        for i in range(len(self.main)):
            content.append('    def test'+ str(i) + '(self):\n')
            content.append('        self.assertEqual(' + self.main[i] + ',' + str(r[i])+')\n')
        return content

    def generate_unittest(self,from_file, to_file):
        imp.reload(codes.result_code)
        r = codes.result_code.result()
        d = self.create_unittest(r,from_file)
        with open(to_file, 'w') as file:
            file.writelines(d)
            file.close()

    def generate_code(self,f,seed =43):
        self.parse_code(seed)
        file = open(f,'w')
        file.write(self.code)
        file.flush()
        file.close()
        #os.fsync(f)

    def generate_file_to_call(self,from_file):

        package, file = from_file.split("/")
        m = []
        m.append("from " + re.sub(".py", "", package + "." + file) + " import *\n")
        m.append('def result():\n')
        m.append('    z=[]\n')
        for i in self.main:
            m.append('    z.append(' + i + ')\n')
        m.append("    return z")
        imp.reload(codes.neww)

        file1 = open("codes/result_code.py", "w")
        file1.writelines(m)
        file1.flush()
        file1.close()


        # os.fsync(file1)




#
#
# g = Generate_code()
# g.generate_code("codes/neww.py")
# g.generate_file_to_call("codes/neww.py")
# g.generate_unittest("codes/neww.py", "test_package/unit.py")
# r = Get_result_of_tests("unit", "test_package")
# r.get_result()




