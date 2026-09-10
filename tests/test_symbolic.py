from cq.symbolic import *
from random import randint
from cq.pythonic import vrandz
import sympy as sp
from sympy.abc import x as spx, y as spy, t as spt
import numpy as np



N = 10
D = 5


#sympy
def test_symbol_matrix():
    assert symbol_matrix('rho', 4, 3).equals(
            sp.Matrix([[sp.Symbol('rho00'), sp.Symbol('rho01'), sp.Symbol('rho02')],
                       [sp.Symbol('rho10'), sp.Symbol('rho11'), sp.Symbol('rho12')],
                       [sp.Symbol('rho20'), sp.Symbol('rho21'), sp.Symbol('rho22')],
                       [sp.Symbol('rho30'), sp.Symbol('rho31'), sp.Symbol('rho32')]])
    )

def test_symbol_matrix_symmetric():
    assert symbol_matrix_symmetric('rho', 4).equals(
            sp.Matrix([[sp.Symbol('rho00'), sp.Symbol('rho01'), sp.Symbol('rho02'), sp.Symbol('rho03')],
                       [sp.Symbol('rho01'), sp.Symbol('rho11'), sp.Symbol('rho12'), sp.Symbol('rho13')],
                       [sp.Symbol('rho02'), sp.Symbol('rho12'), sp.Symbol('rho22'), sp.Symbol('rho23')],
                       [sp.Symbol('rho03'), sp.Symbol('rho13'), sp.Symbol('rho23'), sp.Symbol('rho33')]])
    )



#Hermite functions
def test_hermf():
    pass

def test_hermfxpr():
    pass

def test_hermfder():
    for _ in range(N):
        f = vrandz(randint(0, D))
        prediction = hermfexpr(hermfder(f))
        actual = hermfexpr(f).diff()
        assert prediction.equals(actual)

def test_hermfkin():
    for _ in range(N):
        f = vrandz(randint(0, D))
        prediction = hermfkin(f)
        actual = sp.integrate(hermfexpr(f).diff()**2, (spx, -sp.oo, +sp.oo)) / 2
        assert prediction.equals(actual)

def test_hermfpmul():
    for _ in range(N):
        f, g = vrandz(randint(0, D)), vrandz(randint(0, D))
        prediction = hermfpmul(f, g)
        actual = hermfexpr(f)*hermfexpr(g) / hermf(0)
        assert hermfexpr(prediction).equals(actual)


#quantum mechanics
def test_states_to_density():
    for d in range(1, D+1):
        v, w = sp.Matrix(sp.symbols(f'v:{d}')), sp.Matrix(sp.symbols(f'w:{d}'))
        assert states_to_density(v, w).equals(
                sp.Matrix([[v[i]*v[j]+w[i]*w[j] for j in range(d)] for i in range(d)])
        )

def test_T_matrix():
    assert T_matrix(2).equals(
            sp.Matrix([[         1 ,       0 , -sp.sqrt(2)],
                       [         0 ,       3 ,          0 ],
                       [-sp.sqrt(2),       0 ,          5 ]]) / 4
    )
    assert T_matrix(3).equals(
            sp.Matrix([[         1 ,          0 , -sp.sqrt(2),          0 ],
                       [         0 ,          3 ,          0 , -sp.sqrt(6)],
                       [-sp.sqrt(2),          0 ,          5 ,          0 ],
                       [         0 , -sp.sqrt(6),          0 ,          7 ]]) / 4
    )
    for d in range(D):
        T = T_matrix(d)
        for _ in range(N):
            f = sp.Matrix(vrandz(d+1))
            assert f.dot(T@f).equals(hermfkin(f))

def test_rho_to_g():
    rho = sp.Matrix([[ 0,  1,  2,  3],
                     [ 4,  5,  6,  7],
                     [ 8,  9, 10, 11],
                     [12, 13, 14, 15]])
    g = sp.Matrix([[30],
                   [ 5 + 15*sp.sqrt(2) + 25*sp.sqrt(3)],
                   [10 + 70*sp.sqrt(2) + 20*sp.sqrt(3)],
                   [15 + 75*sp.sqrt(2) + 15*sp.sqrt(3)],
                   [40 + 55*sp.sqrt(6)],
                   [25*sp.sqrt(10)],
                   [30*sp.sqrt(5)]])
    assert rho_to_g(rho).equals(g)



#solvers
def test_linear_solutions():
    assert linear_solutions(sp.Poly(sp.sympify('k*x+d'), spx)).equals(
            sp.Matrix([sp.sympify('-d/k')]))
    assert linear_solutions(sp.Poly(sp.sympify('a*x+b*y+c'), spx, spy), spt).equals(
            sp.Matrix([sp.sympify('-a*c/(a^2+b^2)+b*t'),
                       sp.sympify('-b*c/(a^2+b^2)-a*t')]))



#random
def test_rand_ortho_pair():
    for _ in range(N):
        v, w = rand_ortho_pair(randint(2, D))
        assert v.dot(v).equals(1)
        assert w.dot(w).equals(1)
        assert v.dot(w).equals(0)
