from z3 import *
from predicate import *

def lit(e , v):
    return e if v else Not(e)

def copy_of(expr , tag):
    if tag is None:
        return expr
    return substitute(expr , *[(v , Const(f"{v}_{tag}" , v.sort())) for v in pred_vars])

# evaluate solution :check is it correct ?
def holds(m, expr):
    return is_true(m.eval(expr, model_completion=True))
