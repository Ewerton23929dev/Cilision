from blocks import *

data = C_build("data")
mov = c_funt(c_int(),"main")

ola = c_int("ola", 900)
data.add(ola)
mov.add(scanf(c_int(),ola))
data.add(mov)
with open("main.c","w") as file:
    file.write(str(data))
