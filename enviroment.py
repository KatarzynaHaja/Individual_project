from generate_code import *
from new_mutation import *
import shutil
from get_result import *
from naive_agent import *
from clever_agent import *
class Enviroment:
    def __init(self):
        self.path =''
        self.possible_mutation = []

    def generate_code(self):
        self.file_code = "codes/neww.py"
        self.file_unittest = "test_package/unit.py"
        self.folder="mut"
        g = Generate_code()
        g.parse_code()
        g.generate_code("codes/neww.py")
        g.generate_file_to_call("codes/neww.py")
        g.generate_unittest("codes/neww.py", "test_package/unit.py")

    def mutate_code(self):
        m = Mutation('codes/neww.py')
        m.find_all_operators()
        m.combination_of_mut()
        m.count_propability()
        m.choose_mutation()
        self.content = m.save_mutate_code("mut", "neww.py")
        self.possible_mutation = m.combination
        self.maximum = m.maximum

    def initialize_agent(self):
        #self.naive_agent = Naive_agent(self.possible_mutation)
        self.clever_agent = Clever_agent(self.possible_mutation,self.maximum)

    def run_unittest(self):
        r = Get_result_of_tests("unit", "test_package")
        r.get_result()

    def mainloop(self):
        self.initialize_agent()
        for i in range(10):
            self.clever_agent.random_action()

    def clean(self):
        shutil.rmtree("mut")


e = Enviroment()
e.generate_code()
e.run_unittest()
e.mutate_code()
e.mainloop()

#
# g = Generate_code()
# g.parse_code()
# g.generate_code("codes/neww.py")
# g.generate_file_to_call("codes/neww.py")
# g.generate_unittest("codes/neww.py", "test_package/unit.py")
# r = Get_result_of_tests("unit", "test_package")
# r.get_result()



