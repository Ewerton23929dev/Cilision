# function make malloc memory
def malloc(types,name,leght):
    return f"{types.type()} *{name} ({types.type()}*)malloc({leght});" 
