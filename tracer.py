import sys
import re
from coverage import Coverage
from collections import defaultdict
import os
files = list()
statements_flow = defaultdict(list)
def get_name_of_files(file):
    cov = Coverage()
    cov.start()
    exec(compile(open(file, "rb").read(), file, 'exec'))
    data = cov.get_data()
    datas = data.measured_files()
    cov.stop()
    for i in datas:
        files.append(re.sub('\\\\',"/",i).split("/")[-1])
        statements_flow["Files"].append(re.sub('\\\\',"/",i).split("/")[-1])
    print(files)

def trace_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    statements_flow["Number of line"].append(line_no) 
    #print( ' %s line func %s filenmae %s' % (line_no, func_name,filename))

def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename =co.co_filename
    if re.sub('\\\\',"/",filename).split("/")[-1] not in files or func_name == "<module>":
        return
    statements_flow["Number of line"].append(line_no) 
    statements_flow["Name of function"].append(func_name)
    #print (' %s line %s ' % (line_no,func_name))
    return trace_lines
    
def trace_all(file):
    get_name_of_files(file)
    sys.settrace(trace_calls)
    exec(compile(open(file, "rb").read(), file, 'exec'))

def number_of_calls():
    count_func = dict()
    for i in statements_flow["Name of function"]:
        if i in count_func.keys():
            count_func[i]+=1
        else:
            count_func[i]=1
    return count_func

def compare_paths(orgin,mut):
    the_same = list()
    len_path = min(len(orgin),len(mut))
    for i in range(len_path):
        if orgin[i] == mut[i]:
            the_same.append(orgin[i])
    return the_same

# tutaj moge zobaczyc czy wchodzi do rekurencji
#trace_all(os.path.join("examples_to_mutation","main.py"))
# trace_all(os.path.join("examples_to_mutation","operator_call_clean.py"))
# print(statements_flow)
# print(number_of_calls())
# statements_flow.clear()
# print('--------------------------')
# trace_all(os.path.join("examples_to_mutation","operator_call_mut_code.py"))
# print(statements_flow)
# print(number_of_calls())
tracer_list = list()
statements_flow.clear()
trace_all(os.path.join("examples_to_mutation","flow_operator_example.py"))
print(statements_flow)
tracer_list.append(statements_flow['Number of line'])
print(number_of_calls())

statements_flow.clear()
trace_all(os.path.join("flow_operator_example","1509825380_flow_operator_example.py"))
print(statements_flow)
tracer_list.append(statements_flow['Number of line'])
print(number_of_calls())
print(tracer_list)
print(compare_paths(tracer_list[0],tracer_list[1]))


