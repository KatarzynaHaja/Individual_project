from generate_code import *
from new_mutation import *
import shutil
class Enviroment:
    def __init(self):
        pass

    def generate_code(self):
        self.file_code = "code/neww.py"
        self.file_unittest = "test_package/unit.py"
        self.folder="mut"
        generate_code("codes/neww.py", "test_package/unit.py")

    def mutate_code(self):
        m = Mutation('codes/neww.py')
        m.find_all_operators()
        m.combination_of_mut()
        m.count_propability()
        m.choose_mutation()
        self.path = m.save_mutate_code("mut", "neww.py")

    def clean(self):
        shutil.rmtree("mut")


e = Enviroment()
e.generate_code()
e.mutate_code()
# e.clean()

