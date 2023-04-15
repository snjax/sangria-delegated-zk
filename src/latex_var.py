from sage.all import *


def normalize(name):
    res = []
    for c in name:
        if c.isalnum():
            res.append(c)
        else:
            res.append(f'_{ord(c)}')
    return ''.join(res)
    

def latex_var(expr):
    exprs = expr.split(" ")
    res = []
    for e in exprs:
        nm = normalize(e)
        res.append(var(nm, latex_name=e))
    if len(res) == 1:
        return res[0]
    return res



