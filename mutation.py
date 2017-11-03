import os
import random
import copy
import re
import time

compare_operator = [">","<","==","!=","<=",">="]
arithmetic_operator = ["*","/","-","+","%","**","+=","-="]
def open_file(path):
    with open(path,"r") as file:
        content = file.readlines()
    return content

def mut_compare_operator(content):
    new_content = list()
    number_of_lines = list()
    for index, line in enumerate(content):
        for opt in compare_operator:
            if opt in line:
                finded_operator = opt
                changed_operator = modyfy(compare_operator,finded_operator)
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
                changed_operator = modyfy(compare_operator,finded_operator)
                line = re.sub(finded_operator,changed_operator,line)
                number_of_lines.append(index)
                break
        new_content.append(line)
    return (new_content,number_of_lines)


def modyfy(operators,char):
    set_operators = copy.copy(operators)
    print(set_operators)
    set_operators.remove(char)
    return random.choice(set_operators)

def save_mut_code(content,folder,filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    unix_time = int(time.time())
    name = str(unix_time)+"_"+ filename
    with open(os.path.join(folder,name),"a") as file:
        for line in content:
            file.write(line)

#Compare operator mutation
# folder = "compare_operator_example"
# filename = "compare_operator_example.py"
# path = os.path.join("examples_to_mutation","compare_operator_example.py")
# content = open_file(path)
# new_code,numbers_of_line = mut_compare_operator(content)
# save_mut_code(new_code,folder,filename)
# print(numbers_of_line)

"-----------------------------------------------------"

#Arithemtic operator mutation
folder = "arithmetic_operator_example"
filename = "arithmetic_operator_example.py"
path = os.path.join("examples_to_mutation","arithmetic_operator_example.py")
content = open_file(path)
new_code,numbers_of_line = mut_compare_operator(content)
save_mut_code(new_code,folder,filename)
print(numbers_of_line)
