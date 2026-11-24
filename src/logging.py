from z3 import *
from predicate import *
from helpers import *

# logging
def pretty_log_state(model, tag=None, need_p=True):
    for v in pred_vars:
        print(f"{v} = {model.eval(copy_of(v, tag), model_completion=True)}")
    values = {k: is_true(model.eval(copy_of(c, tag), model_completion=True))
              for k, c in clauses.items()}
    if need_p:
        values["p"] = is_true(model.eval(copy_of(p, tag), model_completion=True))
    print("  -> " + "  ".join(f"{k} = {'T' if x else 'F'}" for k, x in values.items()))

def pretty_log_gacc(result , clause_name):
    for i in range(len(result)):
        print(f"\nfor clause ({clause_name}) = {"False" if i == 0 else "True"}:")
        model = result[i]
        if model is None:
            print("no solution")
        else:
            pretty_log_state(model ,need_p=False)

def pretty_log_cacc(result , clause_name):
    for i in range(len(result)):
        print(f"\nfor clause ({clause_name}) = {"False" if i == 0 else "True"}:")
        model = result[i]
        if model is None:
            print("no solution")
        else:
            pretty_log_state(model)

def pretty_log_racc(result, clause_name):
    if result is None:
        print("no solution")
    else:
        print(f"test 1, {clause_name} = True:")
        pretty_log_state(result, "t")
        print(f"test 2, {clause_name} = False:")
        pretty_log_state(result, "f")

def pretty_log_gicc(result , clause_name):
    for (c_val , p_val) , model in result.items():
        print(f"\nfor clause ({clause_name}) = {c_val} and p = {p_val}:")
        if model is None:
            print("no solution")
        else:
            pretty_log_state(model)


def pretty_log_ricc(result , clause_name):
    for p_val , model in result.items():
        print(f"\nfor clause ({clause_name}) pair with p = {p_val}:")
        if model is None:
            print("no solution")
        else:
            print(f"test 1, {clause_name} = True:")
            pretty_log_state(model , "t")
            print(f"test 2, {clause_name} = False:")
            pretty_log_state(model , "f")

