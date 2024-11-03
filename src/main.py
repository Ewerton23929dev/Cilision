from blocks import *

data = C_build("data")
nome = c_char("nome","ola")
data.add(nome)
main = c_funt(c_int("ola"),"main")
main.add(printf(c_int("ola",90)))
data.add(main)
print(data.code)
