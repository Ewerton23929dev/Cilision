
# builder for code C
class C_build:
    """
    Cria o arquivo do codigo C onde e relacionado entre si!
    """
    def __init__(self,name):
        self.name = name
        self.code = "#include <stdio.h>\n\n"
    def add(self,code):
        self.code += str(code.__str__()) + "\n"
    def include(self,lib: str):
        self.code = f"#include <{lib}>\n" + self.code
    def __str__(self):
        return str(self.code)
