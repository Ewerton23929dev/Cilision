
class Function:
    def __init__(self,type_exit,name,paramentrs=None,code=""):
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
                parar += f"{par[0].type()} {par[1]}"
        return f"{self.type.type()} {self.name}({parar})" + "{\n" + self.code + "\n}"


# int type C
class c_int:
    def __init__(self,name,valor=None):
        self.name = name
        if not isinstance(valor,int) and not valor == None:
            raise TypeError("ist not int python type")
        if valor == None:
            self.valor = "NULL"
        else:
            self.valor = valor
    def __str__(self):
        if self.valor == "NULL":
            return f"int {self.name};"
        else:
            return f"int {self.name} = {self.valor};"
    def type(self):
        return "int"
