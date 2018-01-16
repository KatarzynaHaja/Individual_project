import numpy as np
import random
import copy
class Naive_agent:
    def __init__(self, combination):
        self.combination = combination
        self.execute_action = []

    def random_action(self,seed=43):
        np.random.shuffle(self.combination)
        action = self.combination[random.randint(0,len(self.combination))]
        print(action)
        self.combination.remove(action)
        return action

