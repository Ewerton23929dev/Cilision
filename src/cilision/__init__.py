from .blocks import C_build
import subprocess as sub
import os

# copiler usando arquivo temp
def CCompiler(code,exitt:str,libs=None) -> None:
    """
    Copilador embutido nao nessesario para copilar
    Suporte a Dynamic libs!
    """
    # cria a pasta build ser nao tiver!
    if not os.path.exists("build") and not os.path.isdir("build"):
            os.mkdir("build")
    # checa ser tem libs a ser incluidas
    if libs == None:
        # cria o arquivo temporario!
        with open(f"temp.temp.c","w") as file:
            file.write(code.__str__())
        # copila
        os.system(f"gcc temp.temp.c -o build/{exitt}")
        os.remove("temp.temp.c")
    else:
        # criar o arquivo temporario
        with open(f"temp.temp.c","w") as file:
            used = ""
            for lib in libs:
                code.include(lib.name)
                used = "-I" + str(lib.local)
            file.write(code.__str__())
        # copila com libs
        os.system(f"gcc {used}  temp.temp.c -o build/{exitt}")
        os.remove("temp.temp.c")
