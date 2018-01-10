import sys
import linecache
import importlib
import inspect
import os
import re
from run_unittest import Run

class Tracker:
    def __init__(self, filename,package,unittest= False, content = False):
        self.module = package+'.'+re.sub(".py","",filename)
        self.mod = importlib.import_module(self.module)
        self.filename = filename
        self.package = package
        self.content = content
        self.classes = list()
        self.result = list()
        if unittest == True:
            for name, obj in inspect.getmembers(sys.modules[self.module]):
                if inspect.isclass(obj):
                   self.classes.append(name)


    def traceit(self,frame, event, arg):
        lineno = frame.f_lineno
        co = frame.f_code
        p = co.co_filename
        if p != None:
            t = os.path.basename(p)
        else:
            t=""

        if self.content == True:
            if p != None:
                line = linecache.getline(p, lineno)
                if line !=None:
                    self.result.append([lineno,p, t,line,event])
        else:
            self.result.append([lineno, p, t, event])

        return self.traceit


    def run(self):
        r = Run(self.filename,self.package)
        sys.settrace(self.traceit)
        r.run()
        sys.settrace(None)
        return self.result

