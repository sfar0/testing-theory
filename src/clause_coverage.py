from z3 import *
from helpers import *
from clause_coverage_helpers import *
from testing import *
from logging import *
from predicate import *

def main():
    s = Solver()
    gacc_dic = {}
    #======GACC======
    print("\n====GACC====")
    for key , clause in clauses.items():
        print(f"\n====for clause ({key})====")
        gacc_i = gacc(s , major_clauses[key], clause , key)
        pretty_log_gacc(gacc_i , key)
        gacc_dic[key] = gacc_i

    print("\n==== TEST GACC====")
    for key, sol in gacc_dic.items():
        test_gacc(key, sol)

    #======CACC======
    print("\n====CACC====")
    for key , clause in clauses.items():
        print(f"\n====for clause ({key})====")
        cacc_i = cacc(s , major_clauses[key], clause , key)
        pretty_log_cacc(cacc_i , key)

    #======RACC======
    print("\n====RACC====")
    for key , clause in clauses.items():
        print(f"\n====for clause ({key})==== ")
        racc_i = racc(s , major_clauses[key] , clause , key)
        pretty_log_racc(racc_i , key)

    #======GICC======
    print("\n====GICC====")
    for key , clause in clauses.items():
        print(f"\n====for clause ({key})==== ")
        gicc_i = gicc(s , inactive_clauses[key] , clause , key)
        pretty_log_gicc(gicc_i , key)
    #======RICC======
    print("\n====RICC====")
    for key , clause in clauses.items():
        print(f"\n====for clause ({key})==== ")
        ricc_i = ricc(s , inactive_clauses[key] , clause , key)
        pretty_log_ricc(ricc_i , key)

if (__name__ == "__main__"):
    main()
