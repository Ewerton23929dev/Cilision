
# Bloco para o printf do C
def printf(text,formt=None):
    """
    Funcao para escrever conteudo de variavel na tela.
    """
    if isinstance(text,str) and formt != None:
        return f'printf("{formt}", {text});'
    if text.type() == "int":
        return f'printf("%d", {text.name});'
    elif text.type() == "char":
        return f'printf("%c", {text.name});'
    elif text.type() == "char*":
        return f'printf("%s", {text.name});'
# Bloco para entrada de dados do C
def scanf(typer,addr):
    """
    Entrada de dados do C 
    """
    if isinstance(typer,str) and isinstance(addr,str):
        return f'scanf("{text}",&{addr})'
    if typer.type() == "int":
        return f'scanf("%d",&{addr.name});'
    elif typer.type() == "long":
        return f'scanf("%ld",&{addr.name});'
    elif typer.type() == "char":
        return f'scanf("%c",&{addr.name});'
    elif typer.type() == "char*":
        return f'scanf("%s",&{addr.name});'
