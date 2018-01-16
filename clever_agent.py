import numpy as np
import random
import copy
class Clever_agent:
    def __init__(self, combination,maximum):
        self.combination = combination
        self.execute_action = []
        self.maximum = maximum
        self.operator = ["*", "-", "+", "|", "&", "<", ">", "^"]
        self.matrix_of_mutation = np.matrix([[0.7, 0.1, 0.1, 0.02, 0.02, 0.02, 0.02, 0.02],
                                             [0.02, 0.7, 0.08, 0.02, 0.02, 0.02, 0.02, 0.02],
                                             [0.09, 0.11, 0.7, 0.02, 0.02, 0.02, 0.02, 0.02],
                                             [0.02, 0.02, 0.02, 0.7, 0.18, 0.02, 0.02, 0.02],
                                             [0.02, 0.01, 0.01, 0.2, 0.7, 0.02, 0.02, 0.02],
                                             [0.01, 0.01, 0.01, 0.01, 0.1, 0.7, 0.24, 0.01],
                                             [0.01, 0.01, 0.01, 0.01, 0.02, 0.23, 0.7, 0.1],
                                             [0.15, 0.03, 0.02, 0.02, 0.02, 0.02, 0.02, 0.07]])
        self.count_propability()

    def count_propability(self):
        print("bleee")
        p = list()
        matrix = self.matrix_of_mutation
        propablity = list()
        hightest = self.get_index([self.maximum, self.maximum])
        matrix = np.transpose(matrix)
        h = matrix[hightest[0], hightest[1]]
        for i in self.combination:
            indexs = self.get_index(i)
            p.append(matrix[indexs[0], indexs[1]] / h)
        for i in p:
            propablity.append(i / sum(np.array(p)))
        self.propablity = np.array(propablity)

    def get_index(self, char):
        return [self.operator.index(char[0]), self.operator.index(char[1])]


    def random_action(self,seed=43):
        action = self.combination[random.choice(list(enumerate(self.propablity)))[0]]
        print(action)
        return action

