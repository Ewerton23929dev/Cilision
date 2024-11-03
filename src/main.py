from blocks import *

data = C_build("data")
main = Function(c_int("ola"),"main")
main.add(printf(c_int("ola",90)))
data.add(main)
print(data.code)
