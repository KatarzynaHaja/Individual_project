import os
import random
import copy
import re
import time

compare_operator = [">","<","==","!=","<=",">="]
arithmetic_operator = ["*","/","-","+","%","**","+=","-="]
flow_operator = ['break','continue']
all_operators = [">","<","==","!=","<=",">=","*","/","-","+","%","**","+=","-=",'break','continue']

def open_file(path):
    with open(path,"r") as file:
        content = file.readlines()
    file.close()
    return content

def find_all_operators(content):
    for index, line in enumerate(content):
        for  opt in all_operators:
            if opt in line:
                print(opt)
                start, stop = [(m.start(0), m.end(0)) for m in re.finditer(re.escape(opt), line)][0]
                print(start,stop)
                print(line[start:stop])
                line = line[:start] + '-'+ line[stop:]
                print(line)
                # l = list(line)
                # print(l)
                # print(l.index(opt))
                # print(line)

def mut_compare_operator(content):
    new_content = list()
    number_of_lines = list()
    for index, line in enumerate(content):
        for opt in compare_operator:
            if opt in line:
                finded_operator = opt
                changed_operator = modyfy_operators(compare_operator,finded_operator)
                line = re.sub(finded_operator,changed_operator,line)
                number_of_lines.append(index)
                break
        new_content.append(line)
    return (new_content,number_of_lines)

def mut_arithemtic_operator(content):
    new_content = list()
    number_of_lines = list()
    for index, line in enumerate(content):
        for opt in arithmetic_operator:
            if opt in line:
                finded_operator = opt
                changed_operator = modyfy_operators(arithmetic_operator,finded_operator)
                line = re.sub(finded_operator,changed_operator,line)
                number_of_lines.append(index)
                break
        new_content.append(line)
    return (new_content,number_of_lines)


def mut_change_flow_operator(content):
    new_content = list()
    number_of_lines = list()
    for index, line in enumerate(content):
        for opt in flow_operator:
            if opt in line:
                finded_operator = opt
                changed_operator =  modyfy_flow_element(flow_operator,finded_operator)
                line = re.sub(finded_operator,changed_operator,line)
                number_of_lines.append(index)
                break
        new_content.append(line)
    return (new_content,number_of_lines)

def mut_constant_variable(content):
    new_content = list()
    number_of_lines = list()
    for index, line in enumerate(content):
            if re.match(".*True.*",line):
                line = re.sub("True","False",line)
                number_of_lines.append(index)
            elif re.match(".*False.*",line):
                line = re.sub("False", "True", line)
                number_of_lines.append(index)
            if  re.match(".*=\s*\d+",line) or re.match(".*return\s+\d+",line):
                line = re.sub("\d+",str(random.random()*10),line)
                number_of_lines.append(index)
            if re.match(".*=\s*'",line) or re.match(".*return\s+'",line) or re.match('.*return\s+"',line) or re.match('.*=\s*"',line):
                line = re.sub("'.*'", "'mut'", line)
                line = re.sub('".*"', '"mut"', line)
                number_of_lines.append(index)
            new_content.append(line)

    print(new_content)
    return (new_content,number_of_lines)



def modyfy_operators(operators,char):
    set_operators = copy.copy(operators)
    print(set_operators)
    set_operators.remove(char)
    return random.choice(set_operators)

def modyfy_flow_element(operators,char):
    print(operators)
    set_operators = copy.copy(operators)
    set_operators.append("")
    set_operators.remove(char)
    print(set_operators)
    return random.choice(set_operators)

def save_mut_code(content,folder,filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    unix_time = int(time.time())
    name = str(unix_time)+"_"+ filename
    with open(os.path.join(folder,name),"a") as file:
        for line in content:
            file.write(line)

#Compare operator mut
# folder = "compare_operator_example"
# filename = "compare_operator_example.py"
# path = os.path.join("examples_to_mutation","compare_operator_example.py")
# content = open_file(path)
# new_code,numbers_of_line = mut_compare_operator(content)
# save_mut_code(new_code,folder,filename)
# print(numbers_of_line)

"-----------------------------------------------------"

#Arithemtic operator mut
# folder = "arithmetic_operator_example"
# filename = "arithmetic_operator_example.py"
# path = os.path.join("examples_to_mutation","arithmetic_operator_example.py")
# content = open_file(path)
# new_code,numbers_of_line = mut_compare_operator(content)
# save_mut_code(new_code,folder,filename)
# print(numbers_of_line)

"------------------------------------------------------------"
#Flow operator mut
# folder = "flow_operator_example"
# filename = "flow_operator_example.py"
# path = os.path.join("examples_to_mutation","flow_operator_example.py")
# content = open_file(path)
# new_code,numbers_of_line = mut_change_flow_operator(content)
# save_mut_code(new_code,folder,filename)
# print(numbers_of_line)

#Constant mut
# folder = "constant_variable_example"
# filename = "constant_variable_example.py"
# path = os.path.join("examples_to_mutation","constant_variable_example.py")
# content = open_file(path)
# new_code,numbers_of_line = mut_constant_variable(content)
# save_mut_code(new_code,folder,filename)
# print(numbers_of_line)

folder = "arithmetic_operator_example"
filename = "arithmetic_operator_example.py"
path = os.path.join("examples_to_mutation","arithmetic_operator_example.py")
content = open_file(path)
find_all_operators(content)
