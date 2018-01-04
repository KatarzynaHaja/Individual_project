import os
import subprocess
def generate_code(f):
	s = "python pyfuzz-master/pgen-example.py > %s" % f
	os.system(s)
	r = subprocess.check_output(["python", "pyfuzz-master/pgen-example.py"])
	print(r)
	return r
generate_code("hh.py")