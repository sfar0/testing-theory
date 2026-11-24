
from z3 import *

D_TEMP = 65

# ==========================================
# CREATE TWO INDEPENDENT TESTS
# ==========================================
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

def create_test(suffix):

    inputs = {
        "cur_temp": Int(f"cur_temp_{suffix}"),
        "threshold_diff": Int(f"threshold_diff_{suffix}"),
        "time_since_last_run": Int(f"time_since_last_run_{suffix}"),
        "min_lag": Int(f"min_lag_{suffix}"),
        "override": Bool(f"override_{suffix}"),
        "over_temp": Int(f"over_temp_{suffix}")
    }

    cur_temp = inputs["cur_temp"]
    threshold_diff = inputs["threshold_diff"]
    time_since_last_run = inputs["time_since_last_run"]
    min_lag = inputs["min_lag"]
    override = inputs["override"]
    over_temp = inputs["over_temp"]

    clauses = {
        "a": cur_temp < D_TEMP - threshold_diff,
        "b": override,
        "c": cur_temp < over_temp - threshold_diff,
        "d": time_since_last_run > min_lag
    }

    p = And(
        Or(clauses["a"], And(clauses["b"], clauses["c"])),
        clauses["d"]
    )

    major_clauses = {
        "a": And(clauses["d"],Or(Not(clauses["b"]), Not(clauses["c"]))),

        "b": And(clauses["c"], clauses["d"],Not(clauses["a"])),

        "c": And(clauses["b"], clauses["d"],Not(clauses["a"])),

        "d": Or(clauses["a"],And(clauses["b"], clauses["c"]))
    }

    return inputs, clauses, major_clauses, p


# ==========================================
# DISPLAY TEST RESULTS
# ==========================================

def display_test(model, test_name, inputs, clauses, p):

    print(f"\n--- {test_name} ---")

    print("\nInput variables:")

    for name, variable in inputs.items():
        print(f"{name} = {model.eval(variable, model_completion=True)}")

    print("\nClauses:")

    for name, clause in clauses.items():
        print(f"{name} = {model.eval(clause, model_completion=True)}")

    print("\nPredicate:")

    print(f"p = {model.eval(p, model_completion=True)}")


# ==========================================
# CACC
# ==========================================

def cacc(clause_name):

    s = Solver()

    inputs_1, clauses_1, major_1, p_1 = create_test("1")
    inputs_2, clauses_2, major_2, p_2 = create_test("2")

    # Major clause must be active in both tests
    s.add(major_1[clause_name])
    s.add(major_2[clause_name])

    # Major clause must change
    s.add(clauses_1[clause_name] != clauses_2[clause_name])

    # Predicate must change
    s.add(p_1 != p_2)

    result = s.check()

    print(f"\n========== CACC: clause {clause_name} ==========")

    if result == sat:

        model = s.model()

        display_test(model, "TEST 1", inputs_1, clauses_1, p_1)
        display_test(model, "TEST 2", inputs_2, clauses_2, p_2)

        return model

    elif result == unsat:
        print("No CACC solution found.")

    else:
        print("Z3 returned unknown:", s.reason_unknown())

    return None


# ==========================================
# RACC
# ==========================================

def racc(clause_name):

    s = Solver()

    inputs_1, clauses_1, major_1, p_1 = create_test("1")
    inputs_2, clauses_2, major_2, p_2 = create_test("2")

    # Major clause must be active in both tests
    s.add(major_1[clause_name])
    s.add(major_2[clause_name])

    # Major clause must change
    s.add(clauses_1[clause_name] != clauses_2[clause_name])

    # Predicate must change
    s.add(p_1 != p_2)

    # Minor clauses must remain unchanged
    for key in clauses_1:

        if key != clause_name:
            s.add(clauses_1[key] == clauses_2[key])

    result = s.check()

    print(f"\n========== RACC: clause {clause_name} ==========")

    if result == sat:

        model = s.model()

        display_test(model, "TEST 1", inputs_1, clauses_1, p_1)
        display_test(model, "TEST 2", inputs_2, clauses_2, p_2)

        return model

    elif result == unsat:
        print("No RACC solution found.")

    else:
        print("Z3 returned unknown:", s.reason_unknown())

    return None


# ==========================================
# MAIN
# ==========================================

def main():

    # CACC
    print("\n\n========== CACC ==========")

    for key in ["a", "b", "c", "d"]:
        cacc(key)

    # RACC
    print("\n\n========== RACC ==========")

    for key in ["a", "b", "c", "d"]:
        racc(key)


if __name__ == "__main__":
    main()
