
# add printf in ptyhon blocks for C
def printf(text):
    if text.type() == "int":
        return f'printf("%d", {text.name});'
    if text.type() == "char":
        return f'printf("%c", {text.name});'
    if text.type() == "char*":
        return f'printf("%s", {text.name});'
