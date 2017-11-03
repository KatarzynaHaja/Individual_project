import os
import random
import copy
import re
compare_operator = [">","<","==","!=","<=",">="]
def open_file(path):
    with open(path,"r") as file:
        content = file.readlines()

    print(content)
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
    print(new_content)
    print(number_of_lines)



def modyfy(operators,char):
    set_operators = copy.copy(operators)
    print(set_operators)
    set_operators.remove(char)
    return random.choice(set_operators)

def save_mut_code(content):
    with open(os.path.join("examples","mut_operator.py"),"a") as file:
        for line in content:
            file.write(line)


content = open_file(os.path.join("examples","compare_operator_example.py"))
new_code,numbers_of_line = mut_compare_operator(content)
save_mut_code(new_code)
print(numbers_of_line)