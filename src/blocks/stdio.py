
# add printf in ptyhon blocks for C
def printf(text):
    if text.type() == "int":
        return f"printf('%d',{text.name});"
