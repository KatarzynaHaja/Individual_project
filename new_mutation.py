import os
import random
import copy
import re
import time
import numpy as np

class Mutation:
    def __init__(self, path):
        self.operator = ["*","-","+","|","&","<",">","^"]
        self.path= path
        self.original_content = self.open_file()
        self.matrix_of_mutation  = np.matrix([[0.7, 0.1, 0.1, 0.02, 0.02, 0.02,0.02,0.02],
                                             [0.02,0.7,0.08,0.02, 0.02, 0.02, 0.02, 0.02],
                                             [0.09,0.11,0.7, 0.02, 0.02, 0.02, 0.02, 0.02],
                                             [0.02, 0.02, 0.02, 0.7, 0.18, 0.02, 0.02, 0.02],
                                             [0.02, 0.01,0.01,0.2,0.7,0.02,0.02, 0.02],
                                             [ 0.01, 0.01,0.01,0.01,0.1,0.7,0.24,0.01],
                                             [0.01,0.01,0.01,0.01,0.02,0.23,0.7,0.1],
                                             [0.15,0.03,0.02,0.02,0.02,0.02,0.02,0.07]])

        self.operators_in_file = {}
        self.combination = list()
        self.maximum = 0

    def open_file(self):
        with open(self.path, "r") as file:
            content = file.readlines()
        file.close()
        return content

    def find_all_operators(self):
        oper_occurs = dict()
        for index, line in enumerate(self.original_content):
            for opt in self.operator:
                if opt in line:
                    start, stop = [(m.start(0), m.end(0)) for m in re.finditer(re.escape(opt), line)][0]
                    self.operators_in_file[index,start, stop] = opt
                    if opt in oper_occurs.keys():
                        oper_occurs[opt] +=1
                    else:
                        oper_occurs[opt] = 1
        self.maximum = max(oper_occurs, key=oper_occurs.get)


    def combination_of_mut(self):
        for index, line in enumerate(self.operators_in_file):
            original = self.operators_in_file[line]
            for i in range(len(self.operator) - 1):
                mut = self.change_operator(original, i)
                self.combination.append([original, mut, line])

    def save_mutate_code(self,folder, file):
        content = copy.deepcopy(self.original_content)
        self.choose_mutation()
        content[self.chosen_oper_index[2][0]] = self.replace_char(content[self.chosen_oper_index[2][0]],self.chosen_oper_index[2][1],
                                              self.chosen_oper_index[2][2],self.chosen_oper_index[1])
        if not os.path.exists(folder):
            os.makedirs(folder)

        name = "M" + file
        with open(os.path.join(folder, name), "w") as file:
            for line in content:
                file.write(line)
        return content


    def replace_char(self,text,start, end, replacement):
        return '%s%s%s'%(text[:start],replacement,text[end:])

    def change_operator(self,opt,index):
        operators = copy.deepcopy(self.operator)
        operators.remove(opt)
        return operators[index]

    def count_propability(self):
        p = list()
        matrix = self.matrix_of_mutation
        propablity = list()
        hightest = self.get_index([self.maximum,self.maximum])
        # if self.mutant == True:
        #     matrix = np.transpose(matrix)
        #     print("poo",matrix)
        h = matrix[hightest[0], hightest[1]]
        for i in self.combination:
            indexs = self.get_index(i)
            p.append(matrix[indexs[0],indexs[1]]/h)
        for i in p:
            propablity.append(i/sum(np.array(p)))
        self.propablity = np.array(propablity)
        #return np.array(propablity)

    def choose_mutation(self):
        self.chosen_oper_index = self.combination[random.choice(list(enumerate(self.propablity)))[0]]

    def get_index(self,char):
        return [self.operator.index(char[0]),self.operator.index(char[1])]





# m = Mutation ('codes/neww.py')
# m.find_all_operators()
#
# m.combination_of_mut()
# m.count_propability()
# m.choose_mutation()
# m.save_mutate_code("mut","neww.py")
# prob = m.count_propability(mut,most_occurs)
# index = m.choose_mutation(prob)
# m.save_mut_code(contentes[index],"mut","foo.py",index)

# d = Mutation(name,True)
# opt , most_occurs = d.find_all_operators()
# mut, contentes =d.mut_char(opt)
# prob = d.count_propability(mut,most_occurs)
# index = d.choose_mutation(prob)



