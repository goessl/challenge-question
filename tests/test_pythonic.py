from cq.pythonic import *
import numpy as np



def test_veczero():
    assert veczero == ()

def test_vecbasis():
    assert vecbasis(0) == (1,)
    assert vecbasis(1) == (0, 1)
    assert vecbasis(2) == (0, 0, 1)

def test_vecpos():
    assert vecpos([+1, -2]) == (+1, -2)

def test_vecneg():
    assert vecneg([+1, -2, +3]) == (-1, +2, -3)

def test_vecadd():
    assert vecadd([1, 2, 3], (4, 5)) == (5, 7, 3)

def test_vecsub():
    assert vecsub([1, 2, 3], (4, 5)) == (-3, -3, 3)

def test_vecmul():
    assert vecmul([1, 2, 3], 2) == (2, 4, 6)

def test_vecrmul():
    assert vecrmul(2, [1, 2, 3]) == (2, 4, 6)

def test_vectruediv():
    assert vectruediv([2, 4, 6], 2) == (1, 2, 3)

def test_vecfloordiv():
    assert vecfloordiv([3, 4, 7], 2) == (1, 2, 3)

def test_vecmod():
    assert vecmod([3, 4, 7], 2) == (1, 0, 1)

def test_vecdot():
    assert vecdot([1, 2, 3], [4, 5, 6]) == 32

def test_vecabsq():
    assert vecabsq([1, 2, 3]) == 14


def test_binom():
    N = 10000
    for sigma in (10, 20, 40, 80, 160, 320):
        x = [binom(sigma) for _ in range(N)]
        assert abs(np.mean(x)) < 5 * sigma/np.sqrt(N) #std(X_bar)=sigma/sqrt(N), test within 5 sigma
        assert abs(np.var(x)-sigma**2) < 5 * sigma**2*np.sqrt(2/N) #std(X_var)=sigma^2*sqrt(2/N), test within 5 sigma
        #not sure about formulas for X_bar & X_var standard deviations
