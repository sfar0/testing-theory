
# Test Requirement Result

## GACC

```text
====for clause (a)====

for clause (a) = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = T

for clause (a) = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = T

====for clause (b)====

for clause (b) = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = T

for clause (b) = True:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 66
  -> a = F  b = T  c = T  d = T

====for clause (c)====

for clause (c) = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 65
  -> a = F  b = T  c = F  d = T

for clause (c) = True:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 66
  -> a = F  b = T  c = T  d = T

====for clause (d)====

for clause (d) = False:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 0
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = F

for clause (d) = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = T
```

## CACC

```text
====for clause (a)====

for clause (a) = False:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = T  p = T

for clause (a) = True:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = T  p = F

====for clause (b)====

for clause (b) = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 66
  -> a = F  b = T  c = T  d = T  p = T

for clause (b) = True:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = T  p = F

====for clause (c)====

for clause (c) = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 66
  -> a = F  b = T  c = T  d = T  p = T

for clause (c) = True:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 65
  -> a = F  b = T  c = F  d = T  p = F

====for clause (d)====

for clause (d) = False:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = T  p = T

for clause (d) = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 0
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = F  p = F
```

## RACC

```text
====for clause (a)====
test 1, a = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = T  p = T
test 2, a = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = T  p = F

====for clause (b)====
test 1, b = True:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 66
  -> a = F  b = T  c = T  d = T  p = T
test 2, b = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = T  p = F

====for clause (c)====
test 1, c = True:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 66
  -> a = F  b = T  c = T  d = T  p = T
test 2, c = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 65
  -> a = F  b = T  c = F  d = T  p = F

====for clause (d)====
test 1, d = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 65
  -> a = T  b = T  c = T  d = T  p = T
test 2, d = False:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 0
min_lag = 0
override = True
over_temp = 65
  -> a = T  b = T  c = T  d = F  p = F
```

## GICC

```text
====for clause (a)====

for clause (a) = True and p = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 65
  -> a = T  b = T  c = T  d = T  p = T

for clause (a) = False and p = True:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 66
  -> a = F  b = T  c = T  d = T  p = T

for clause (a) = True and p = False:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 0
min_lag = 0
override = False
over_temp = 0
  -> a = T  b = F  c = F  d = F  p = F

for clause (a) = False and p = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 0
min_lag = 0
override = True
over_temp = 66
  -> a = F  b = T  c = T  d = F  p = F

====for clause (b)====

for clause (b) = True and p = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 65
  -> a = T  b = T  c = T  d = T  p = T

for clause (b) = False and p = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 0
  -> a = T  b = F  c = F  d = T  p = T

for clause (b) = True and p = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 65
  -> a = F  b = T  c = F  d = T  p = F

for clause (b) = False and p = False:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 0
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = F  p = F

====for clause (c)====

for clause (c) = True and p = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = T  p = T

for clause (c) = False and p = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 64
  -> a = T  b = F  c = F  d = T  p = T

for clause (c) = True and p = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = T  p = F

for clause (c) = False and p = False:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 0
min_lag = 0
override = True
over_temp = 64
  -> a = T  b = T  c = F  d = F  p = F

====for clause (d)====

Not solvable, inactive clause d with d = True and p = True

Not solvable, inactive clause d with d = False and p = True

for clause (d) = True and p = True:
no solution

for clause (d) = False and p = True:
no solution

for clause (d) = True and p = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = T  p = F

for clause (d) = False and p = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 0
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = F  p = F
```

## RICC

```text
====for clause (a)====

for clause (a) pair with p = True:
test 1, a = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 65
  -> a = T  b = T  c = T  d = T  p = T
test 2, a = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 66
  -> a = F  b = T  c = T  d = T  p = T

for clause (a) pair with p = False:
test 1, a = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 0
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = F  p = F
test 2, a = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 0
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = F  p = F

====for clause (b)====

for clause (b) pair with p = True:
test 1, b = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 65
  -> a = T  b = T  c = T  d = T  p = T
test 2, b = False:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = T  p = T

for clause (b) pair with p = False:
test 1, b = True:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = True
over_temp = 65
  -> a = F  b = T  c = F  d = T  p = F
test 2, b = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 65
  -> a = F  b = F  c = F  d = T  p = F

====for clause (c)====

for clause (c) pair with p = True:
test 1, c = True:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 65
  -> a = T  b = F  c = T  d = T  p = T
test 2, c = False:
cur_temp = 64
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 64
  -> a = T  b = F  c = F  d = T  p = T

for clause (c) pair with p = False:
test 1, c = True:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = T  p = F
test 2, c = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 65
  -> a = F  b = F  c = F  d = T  p = F

====for clause (d)====

Not solvable, inactive clause d (restricted) with p = True

for clause (d) pair with p = True:
no solution

for clause (d) pair with p = False:
test 1, d = True:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 1
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = T  p = F
test 2, d = False:
cur_temp = 65
threshold_diff = 0
time_since_last_run = 0
min_lag = 0
override = False
over_temp = 66
  -> a = F  b = F  c = T  d = F  p = F
```
