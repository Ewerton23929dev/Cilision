
# char type in C
class c_char:
    """
    Cria o tipo char e char* do C de forma brevimente simplificada!
    """
    def __init__(self,name=None,valor=None,leght=None):
        self.name = name
        self.leght = leght
        if not isinstance(valor,str) and not valor == None:
            raise TypeError("ist not str python type")
        if valor == None:
            self.valor = "NULL"
        else:
            self.valor = valor.replace("<space>","\\n")
    def __str__(self):
        if self.name == None:
            return "char"
        if self.leght == None and self.valor == "NULL":
            return f'char {self.name};'
        if not self.leght and self.valor == "NULL":
            return f'char {self.name}[{self.leght}];'
        if self.leght == None and not self.valor == "NULL":
            return f'char {self.name} = "{self.valor[0]}";'
        else:
            return f'char {self.name}[{self.leght}] = "{self.valor}";'
    def type(self):
        if self.leght == None:
            return "char"
        else:
            return "char*"

#is type long in C
class c_long:
    """
    Cria o tipo long do C!
    """
    def __init__(self,name=None,valor=None):
        self.name = name
        if not isinstance(valor,int) and not valor == None:
            raise TypeError("ist not long python type")
        if valor == None:
            self.valor = "NULL"
        else:
            self.valor = valor
    def __str__(self):
        if self.name == None:
            return "long"
        if self.valor == "NULL":
            return f"long {self.name};\n"
        else:
            return f"long {self.name} = {self.valor};\n"
    def type(self):
        return "long"
# type for functions
class c_funt:
    """
    Cria um funcao do C!
    Args: type, name, code(opicinal) args(opicinal)
    """
    def __init__(self,type_exit,name,code="",paramentrs=None):
        self.type = type_exit
        self.parar = paramentrs
        self.code = code
        self.name = name
    def add(self,code):
        self.code += str(code)
    def __str__(self):
        parar = ""
        if not self.parar == None:
            for par in self.parar:
                parar += f"{par.type()} {par.name}"
        return f"{self.type.type()} {self.name}({parar})" + "{\n" + self.code + "\n}"


# int type C
class c_int:
    """
    Cria o tipo inteiro int do C!
    """
    def __init__(self,name=None,valor=None):
        self.name = name
        if not isinstance(valor,int) and not valor == None:
            raise TypeError("ist not int python type")
        if valor == None:
            self.valor = "NULL"
        else:
            self.valor = valor
    def __str__(self):
        if self.name == None:
            return "int"
        if self.valor == "NULL":
            return f"int {self.name};\n"
        else:
            return f"int {self.name} = {self.valor};\n"
    def type(self):
        return "int"
