import os
import random
import copy
import re
import time
import numpy as np

class Mutation:
    def __init__(self, path, mutant):
        self.mutant = mutant
        self.operator = ["*","-","+"]
        self.path= path
        self.original_content = self.open_file()
        self.matrix_of_mutation  = np.matrix([[0.9, 0.05, 0.05],
                                             [0.1,0.8,0.1],
                                             [0.2,0.1,0.7]])


    def open_file(self):
        with open(self.path, "r") as file:
            content = file.readlines()
        file.close()
        return content

    def find_all_operators(self):
        dict_oper = {}
        oper_occurs = dict()
        for index, line in enumerate(self.original_content):
            for opt in self.operator:
                if opt in line:
                    start, stop = [(m.start(0), m.end(0)) for m in re.finditer(re.escape(opt), line)][0]
                    dict_oper[index,start, stop] = opt
                    if opt in oper_occurs.keys():
                        oper_occurs[opt] +=1
                    else:
                        oper_occurs[opt] = 1
        maximum = max(oper_occurs, key=oper_occurs.get)
        return dict_oper, maximum

    def mut_char(self,opt):
        combination = list()
        contents = list()
        index_to_save =0
        for index, line in enumerate(opt):
            original = opt[line]
            for i in range(len(opt)-1):
                content = copy.deepcopy(self.original_content)
                opt[line] = self.change_operator(opt[line],i)
                content[line[0]] = self.replace_char(content[line[0]],line[1],line[2],opt[line])
                if self.mutant ==True:
                    self.save_mut_code(content,"mut","foo.py",index_to_save)
                    index_to_save += 1
                contents.append(content)
                combination.append([original,opt[line]])
            opt[line]= original
        return combination,contents

    def replace_char(self,text,start, end, replacement):
        return '%s%s%s'%(text[:start],replacement,text[end:])

    def change_operator(self,opt,index):
        operators = copy.deepcopy(self.operator)
        operators.remove(opt)
        return operators[index]

    def save_mut_code(self,content, folder, filename, index):
        if not os.path.exists(folder):
            os.makedirs(folder)
        if self.mutant== True:
            name = "O"+str(index)+ filename
            print("bleee")
        else:
            name = "M" + str(index) + filename
        with open(os.path.join(folder, name), "w") as file:
            for line in content:
                file.write(line)
        return os.path.join(folder,name)

    def count_propability(self,mutations,occur):
        print("muttt",self.mutant)
        p = list()
        matrix = self.matrix_of_mutation
        print(matrix)
        propablity = list()
        hightest = self.get_index([occur,occur])
        if self.mutant == True:
            matrix = np.transpose(matrix)
            print("poo",matrix)
        h = matrix[hightest[0], hightest[1]]
        for i in mutations:
            indexs = self.get_index(i)
            p.append(matrix[indexs[0],indexs[1]]/h)
        for i in p:
            propablity.append(i/sum(np.array(p)))
        return np.array(propablity)

    def choose_mutation(self,prob):
        return random.choice(list(enumerate(prob)))[0]

    def get_index(self,char):
        return [self.operator.index(char[0]),self.operator.index(char[1])]





m = Mutation ('foo.py',False)
opt , most_occurs = m.find_all_operators()
mut, contentes =m.mut_char(opt)
prob = m.count_propability(mut,most_occurs)
index = m.choose_mutation(prob)
name = m.save_mut_code(contentes[index],"mut","foo.py",index)

d = Mutation(name,True)
opt , most_occurs = d.find_all_operators()
mut, contentes =d.mut_char(opt)
prob = d.count_propability(mut,most_occurs)
index = d.choose_mutation(prob)



