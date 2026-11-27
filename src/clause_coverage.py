from z3 import *
from helpers import *
from clause_coverage_helpers import *
from testing import *
from logging import *
from predicate import *
import sys

usage_label = "\nusage:\n  python clause_coverage.py gacc | cacc | racc | gicc | ricc \n u can also  type multiple TR (eg , gacc racc gicc)"
def print_TR(s, arg):
    match arg:
    #======GACC======
        case "gacc":
            gacc_dic = {}
            print("\n====GACC====")
            for key , clause in clauses.items():
                print(f"\n====for clause ({key})====")
                gacc_i = gacc(s , major_clauses[key], clause , key)
                pretty_log_gacc(gacc_i , key)
                gacc_dic[key] = gacc_i
    #======CACC======
        case "cacc":
                print("\n====CACC====")
                for key , clause in clauses.items():
                    print(f"\n====for clause ({key})====")
                    cacc_i = cacc(s , major_clauses[key], clause , key)
                    pretty_log_cacc(cacc_i , key)
    #======RACC======
        case "racc":
            print("\n====RACC====")
            for key , clause in clauses.items():
                print(f"\n====for clause ({key})==== ")
                racc_i = racc(s , major_clauses[key] , clause , key)
                pretty_log_racc(racc_i , key)
    #======GICC======
        case "gicc":
            print("\n====GICC====")
            for key , clause in clauses.items():
                print(f"\n====for clause ({key})==== ")
                gicc_i = gicc(s , inactive_clauses[key] , clause , key)
                pretty_log_gicc(gicc_i , key)
    #======RICC======
        case "ricc":
            print("\n====RICC====")
            for key , clause in clauses.items():
                print(f"\n====for clause ({key})==== ")
                ricc_i = ricc(s , inactive_clauses[key] , clause , key)
                pretty_log_ricc(ricc_i , key)
        case _:
            raise Exception("invalid Input" + usage_label)


def cli_man(s):
    if (len(sys.argv) <= 1):
        print("no input was given" + usage_label)
        sys.exit(1)
    else:
        for tr in sys.argv[1::]:
            try:
                print_TR(s,tr)
            except Exception as e:
                print (str(e))
                sys.exit(1)
        sys.exit(0)






def main():
    s = Solver()
    # print("\n==== TEST GACC====")
    # for key, sol in gacc_dic.items():
    #     test_gacc(key, sol)
    cli_man(s)




if (__name__ == "__main__"):
    main()
