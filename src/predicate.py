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

pred_vars = [cur_temp , threshold_diff , time_since_last_run , min_lag , override , over_temp]

clauses ={
"a" : cur_temp < D_TEMP - threshold_diff,
"b" : override,
"c" : cur_temp < over_temp - threshold_diff,
"d" : time_since_last_run > min_lag,
}

p = And(Or(clauses["a"] , And(clauses["b"] , clauses["c"])) , clauses["d"])

major_clauses ={
"a" : And(clauses["d"] , Or(Not(clauses["b"]) , Not(clauses["c"]))),
"b" : And(clauses["c"] , clauses["d"] ,Not(clauses["a"])),
"c" : And(clauses["b"] , clauses["d"] ,Not(clauses["a"])),
"d" : Or(clauses["a"] , And(clauses["b"], clauses["c"])),
}
inactive_clauses = {key : Not(major) for key , major in major_clauses.items()}


