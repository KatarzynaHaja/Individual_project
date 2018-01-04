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

import random

from pyfuzz_master.pgen import pgen_opts, ProgGenerator
from pyfuzz_master.pygen.cgen import CodeGenerator


def generate_code(f,seed=43):
    random.seed(seed)
    pgen = ProgGenerator(pgen_opts, random.Random())
    m = pgen.generate()
    cgen = CodeGenerator()
    with open(f,'w') as file:
    	file.write(cgen.generate(m))
    print(cgen.generate(m))
generate_code("neww.py")
