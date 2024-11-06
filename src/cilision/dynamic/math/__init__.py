from pathlib import Path
local = Path(__file__).parent

class C_math:
    def __init__(self):
        self.local = local
        self.name = "mathlib.h"
        self.fileMain = local / "mathlib.h"
    def fast_add(self,num1,num2):
        """
        Implementa a soma rapida dentro do C!
        """
        return f"fast_add({num1},{num2});"
    def fast_sub(self,num1,num2):
        """
        Implementa subtrcao rapida em C!
        """
        return f"fast_sub({num1},{num2});"
    def fast_sqrt(self,num1,num2):
        """
        Implementa raiz em c de forma rapida!
        """
        return f"fast_sqrt({num1},{num2});"
