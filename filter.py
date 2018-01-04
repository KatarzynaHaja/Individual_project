import os
from tracer import Tracker
from collections import defaultdict
import json
def filter(result):
    r = result.copy()
    d = defaultdict(list)
    number_line = list()
    flow = list()
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    t = os.path.split(ROOT_DIR)[1]
    for i in r:
        if t in i[1] and os.path.basename(__file__) != i[2] :
            flow.append(i)
            number_line.append(i[0])
    #         for j in range(len(i)):
    #             d[j].append(i[j])
    # print(d)
    return number_line,flow

def save_to_json(data,filename):
    with open('filename', 'w') as outfile:
        json.dump(data, outfile)





print(filter(Tracker("tests.py","test_package",True,True).run()))
