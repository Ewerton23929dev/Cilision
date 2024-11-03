from blocks import *

data = C_build("data")
nome = c_char("nome","ola<space>",5)
data.add(nome)
main = c_funt(c_int("ola"),"main")
main.add(printf(nome))
data.add(main)
with open("exemple.c","w") as file:
    print(data)
    file.write(str(data))
