from z3 import *
from helpers import copy_of , lit
from predicate import *

# Solve function
def solve(s , label , *constraints):
    s.reset()
    s.add(*constraints)
    is_solvable = s.check()
    if(is_solvable == unsat):
        print(f"\nNot solvable, {label}")
        return None
    elif(is_solvable == unknown):
        print(f"\nz3 failed, {label}")
        return None
    return s.model()


# GACC P_i = 1 for each i = {1, 0} => pair ()
def gacc(s , major_i , clause_i , key_i):
    solution = []
    for c in (False , True):
        sol_i = solve(s , f"active clause {key_i} when {key_i} is true"  , major_i ,
                        lit(clause_i , c))
        solution.append(sol_i)
    return solution


# CACC
def cacc(s , active_i , i , key_i):
    solution = []
    def cacc_helper(c_val ,p_val):
        if len(solution) > 2:
            return
        label = f"active clause {key_i} with {key_i} = {c_val} and p = {p_val}"
        sol_i = solve(s , label , active_i , lit(i , c_val) , lit(p ,p_val))
        if sol_i is None:
            solution.append(None)
            cacc_helper(c_val,not(p_val))
        else:
            if (len(solution) > 0 and solution[0] is None):
                solution.pop()
            solution.append(sol_i)
            cacc_helper(not (c_val),not(p_val))

    cacc_helper(True , True)
    return solution

# RACC
def racc(s, active_i, i, i_key):
    constraints = [
        copy_of(i, "t"),            # c_i = True in test t
        Not(copy_of(i, "f")),       # c_i = False in test f
        copy_of(active_i, "t"),     # c_i determines p in test t
        copy_of(active_i, "f"),     # c_i determines p in test f
    ]
    # RACC: every minor clause has the same truth value in both tests
    for key, clause in clauses.items():
        if key != i_key:
            constraints.append(copy_of(clause, "t") == copy_of(clause, "f"))
    label = f"active clause {i_key} (restricted)"
    return solve(s, label, *constraints)


# GICC
def gicc(s , inactive_i , i , key_i):
    results = {}
    for p_val in (True , False):
        for c_val in (True , False):
            label = f"inactive clause {key_i} with {key_i} = {c_val} and p = {p_val}"
            results[(c_val , p_val)] = solve(s , label , inactive_i , lit(i , c_val) , lit(p , p_val))
    return results

# RICC : for p = T and for p = F, a pair of tests (c_i = T , c_i = F) with c_i inactive
# and the minor clauses having the same truth value in both tests.
# Returns {p value : model or None}; the model contains the two states (suffix _t and _f)
def ricc(s , inactive_i , i , i_key):
    results = {}
    for p_val in (True , False):
        constraints = [
            copy_of(i , "t"),                  # test 1 : c_i = True
            Not(copy_of(i , "f")),             # test 2 : c_i = False
            copy_of(inactive_i , "t"),         # c_i inactive in both tests
            copy_of(inactive_i , "f"),
            lit(copy_of(p , "t") , p_val),     # p has the same value in both tests
            lit(copy_of(p , "f") , p_val),
        ]
        # RICC : every minor clause has the same truth value in both tests
        for key , clause in clauses.items():
            if key != i_key:
                constraints.append(copy_of(clause , "t") == copy_of(clause , "f"))
        label = f"inactive clause {i_key} (restricted) with p = {p_val}"
        results[p_val] = solve(s , label , *constraints)
    return results

