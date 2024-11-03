# function make malloc memory
def malloc(types,name,leght):
    return f"{types.type()} *{name} ({types.type()}*)malloc({leght});"
def free(var):
    return f"free({var});"
def rezise(var,leght: int):
    return f"rezise({var},{int(leght)})"
