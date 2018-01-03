import os
from tracer import Tracker


def filter(result):
    r = result.copy()
    number_line = list()
    flow = list()
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    t = os.path.split(ROOT_DIR)[1]
    for i in r:
        if t in i[1] and os.path.basename(__file__) != i[2] :
            flow.append(i)
            number_line.append(i[0])
    return number_line,flow




print(filter(Tracker("tests.py","test_package",True,True).run()))
