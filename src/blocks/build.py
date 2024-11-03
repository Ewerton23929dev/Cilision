
# builder for code C
class C_build:
    def __init__(self,name):
        self.name = name
        self.code = "#include <stdio.h>\n"
    def add(self,code):
        self.code += str(code) + "\n"
