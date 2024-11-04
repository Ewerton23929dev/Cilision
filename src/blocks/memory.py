# function make malloc memory
def malloc(types,name,leght):
    """
    Funcao malloc do C criar memoria 
    BUG: Ele cria uma nova variavel nao utiliza uma!
    """
    return f"{types.type()} *{name} ({types.type()}*)malloc({leght});"
def free(var):
    """
    Funcao free do C limpar memoria
    """
    return f"free({var});"
def resize(var,leght: int):
    """
    Funcao resize do C realoca a memoria para novo tamanho
    """
    return f"rezise({var},{int(leght)})"
