import cilision as cili
from cilision.blocks import *
from cilision.dynamic import *

main = C_build("data")
main.add(c_funt(c_int(),"main"))
print(main)
cili.CCompiler(main,"main",[C_math()])
