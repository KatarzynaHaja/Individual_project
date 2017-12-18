import sys
import re
from coverage import Coverage
from collections import defaultdict
from test_package import tests
import os


class Track:
    def __init__(self,file, if_unittest=True):
        self.track_file = file
        self.files = list()
        self.statements_flow = defaultdict(list)

    def get_name_of_files(self):
        cov = Coverage()
        cov.start()
        exec(compile(open(self.track_file, "rb").read(), self.track_file, 'exec'))
        #exec(compile("python -m pytest " + self.track_file),self.track_file,'exec')
        data = cov.get_data()
        datas = data.measured_files()
        cov.stop()
        for i in datas:
            self.files.append(re.sub('\\\\',"/",i).split("/")[-1])
            self.statements_flow["Files"].append(re.sub('\\\\',"/",i).split("/")[-1])

    def trace_lines(self,frame, event,arg):
        if event != 'line':
            return
        co = frame.f_code
        func_name = co.co_name
        line_no = frame.f_lineno
        filename = co.co_filename
        self.statements_flow["Number of line"].append(line_no)
        #print( ' %s line func %s filenmae %s' % (line_no, func_name,filename))

    def trace_calls(self,frame, event, arg):
        if event != 'call':
            return
        co = frame.f_code
        func_name = co.co_name
        line_no = frame.f_lineno
        filename =co.co_filename
        if re.sub('\\\\',"/",filename).split("/")[-1] not in self.files or func_name == "<module>":
            return
        self.statements_flow["Number of line"].append(line_no)
        self.statements_flow["Name of function"].append(func_name)
        #print (' %s line %s ' % (line_no,func_name))
        return self.trace_lines

    def trace_file(self):
        self.get_name_of_files()
        sys.settrace(self.trace_calls)
        exec(compile(open(self.track_file, "rb").read(), self.track_file, 'exec'))

    def number_of_calls(self):
        count_func = dict()
        for i in self.statements_flow["Name of function"]:
            if i in count_func.keys():
                count_func[i]+=1
            else:
                count_func[i]=1
        return count_func

    def compare_paths(self,orgin,mut):
        the_same = list()
        len_path = min(len(orgin),len(mut))
        for i in range(len_path):
            if orgin[i] == mut[i]:
                the_same.append(orgin[i])
        return the_same

# tutaj moge zobaczyc czy wchodzi do rekurencji
#trace_all(os.path.join("examples_to_mutation","main.py"))
# print("Orgin file")
# t = Track(os.path.join("examples_to_mutation","operator_call_clean.py"))
# t.trace_file()
# print(t.statements_flow)
# print(t.number_of_calls())
# lines_clean = t.statements_flow["Number of line"]
#
# print("Mut file")
# t = Track(os.path.join("examples_to_mutation","operator_call_mut_code.py"))
# t.trace_file()
# print(t.statements_flow)
# lines_mut = t.statements_flow["Number of line"]
# print(t.number_of_calls())
#
# print("Compare lines")
# print(t.compare_paths(lines_clean,lines_mut))
#
# print('--------------------------')
#
# print("Orgin file")
# t = Track(os.path.join("examples_to_mutation","flow_operator_example.py"))
# t.trace_file()
# print(t.statements_flow)
# print(t.number_of_calls())
# lines_clean = t.statements_flow["Number of line"]
#
# print("Mut file")
# t = Track(os.path.join("flow_operator_example","1509825380_flow_operator_example.py"))
# t.trace_file()
# print(t.statements_flow)
# print(t.number_of_calls())
# lines_mut = t.statements_flow["Number of line"]
#
# print("compare lines")
# print(t.compare_paths(lines_clean,lines_mut))

print("Unittest")
t = Track("tests.py")
t.trace_file()
print(t.statements_flow)
print(t.number_of_calls())
lines_mut = t.statements_flow["Number of line"]


