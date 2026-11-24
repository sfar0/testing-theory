from z3 import *
# ====the predicate====
#
# p = (a ∨ (b ∧ c)) ∧ d
#
#  ====clause====
#
# a = curTemp < dTemp - thresholdDiff
#
# b = override
#
# c = curTemp < over_temp - thresholdDiff
#
# d = timeSinceLastRun > minLag
#
# p = turn heat
#
# ====var types====

#  curTemp: Integer
#  thresholdDiff: Integer
#  timeSinceLastRun: Integer
#  minLag: Integer
#  override = b : boolean
#  over_temp: Integer
#  runTime: Integer
#  heaterOn = p: boolean
#
# ====Active clause====
#
# p_a = d ∧ (¬b ∨ ¬c)
#
# p_b = c ∧ d ∧ ¬a
#
# p_c = b ∧ d ∧ ¬a
#
# p_d = a ∨ (b ∧ c)


D_TEMP = 65

cur_temp = Int("cur_temp")

threshold_diff = Int("threshold_diff")

time_since_last_run = Int("time_since_last_run")

min_lag = Int("min_lag")

override = Bool("override")

over_temp = Int("over_temp")

run_time = Int("run_time")

clauses ={
"a" : cur_temp < D_TEMP - threshold_diff,
"b" : override,
"c" : cur_temp < over_temp - threshold_diff,
"d" : time_since_last_run > min_lag,
}

major_clauses ={
"a" : And(clauses["d"] , Or(Not(clauses["b"]) , Not(clauses["c"]))),
"b" : And(clauses["c"] , clauses["d"] ,Not(clauses["a"])),
"c" : And(clauses["b"] , clauses["d"] ,Not(clauses["a"])),
"d" : Or(clauses["a"] , And(clauses["b"], clauses["c"])),
}

p = And(Or(clauses["a"] , And(clauses["b"] , clauses["c"])) , clauses["d"])

# GACC P_i = 1 for each i = {1, 0} => pair ()
def gacc(s , p_i , i , i_key):
    s.reset()
    s.add(p_i)
    s.push()
    s.add(i)
    is_solvable = s.check()
    if(is_solvable == "unsat"):
        print(f"\nNot solvabale, active clause {i_key}  when  {i_key} is true")
        sol_i_t = None
    elif(is_solvable == "unknown"):
        print(f"\n z3 failed, active clause {i_key}")
        sol_i_t = None
    else :
        sol_i_t = s.model()
    s.pop()
    s.push()
    s.add(Not(i))
    is_solvable = s.check()

    #  we need find a way for this to not be redundant
    if(is_solvable == "unsat"):
        print(f"\nNot solvabale, active clause {i_key}  when  {i_key} is false ")
        sol_i_f = None
    elif(is_solvable == "unknown"):
        print(f"\n z3 failed, active clause {i_key}")
        sol_i_f = None
    else :
        sol_i_f = s.model()
    return (sol_i_f , sol_i_t)

def pretty_log_model(model):
    for d in model.decls():
        print ("\n%s = %s" % (d.name(), model[d]))

# this need to be updated to suit RACC , CACC , GICC , RICC
def pretty_log(result , clause_name):
    for i in range(len(result)):
        print(f"\nfor clause ({clause_name}) = {"False" if i == 0 else "True"}:")
        pretty_log_model(result[i])

def main():
    s = Solver()
    #======GACC======
    print("\n====GACC====")
    for key , clause in clauses.items():
        print(f"\n====for clause ({key})==== ")
        gacc_i = gacc(s , major_clauses[key], clause , key)
        pretty_log(gacc_i , key)
    #======CACC======
    #======RACC======

if (__name__ == "__main__"):
    main()
