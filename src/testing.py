from z3 import *
from helpers import holds
from predicate import *

# test GACC
def test_gacc(key, sol):
    if sol[0] is None or sol[1] is None:
        print(f"clause {key}: no GACC pair, skipping")
        return
    m_f, m_t = sol                      # gacc returns (x=False model, x=True model)
    x, P = clauses[key], major_clauses[key]

    assert not holds(m_f, x), f"{key} should be False in m_f"
    assert holds(m_t, x),     f"{key} should be True in m_t"
    assert holds(m_f, P) and holds(m_t, P), f"P_{key} fails"
    assert holds(m_f, p) != holds(m_t, p), f"p doesn't change with {key}"
    print(f"clause {key}: GACC pair OK")

