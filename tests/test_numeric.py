from cq.numeric import *
from cq.pythonic import vecbasis, vbinom
from cq import symbolic
from random import randint
from sympy import Symbol
import numpy as np



N = 10
D = 5



#Hermite functions
def test_hermfval():
    x = np.linspace(-12, +12, 10000)
    H = np.array([hermfval(vecbasis(j), x) for j in range(6)])
    G = np.trapezoid(H[:, None, :]*H[None, :, :], x, axis=-1)
    assert np.allclose(G, np.eye(6)) #orthonormality
    
    #cross-check with symbolic
    for _ in range(N):
        f = np.random.rand(np.random.randint(1, D))
        for _ in range(10):
            x = np.random.randn()
            assert np.isclose(
                hermfval(f, x),
                float(
                    sum(fj*symbolic.hermf(j) for j, fj in enumerate(f))
                    .subs({Symbol('x'):x})
                )
            )

def test_hermfder():
    #cross-check with symbolic
    for _ in range(N):
        f = vbinom(randint(0, D))
        prediction = hermfder(f)
        actual = symbolic.hermfder(f)
        assert np.allclose(
            prediction,
            np.asarray(actual.T, dtype=float)
        )

def test_hermfkin():
    #cross-check with symbolic
    for _ in range(N):
        f = vbinom(randint(0, D))
        prediction = hermfkin(f)
        actual = symbolic.hermfkin(f)
        assert np.isclose(prediction, float(actual))

def test_hermfpmul():
    x = np.linspace(-4, +4, 1000)
    for _ in range(N):
        f = np.random.rand(np.random.randint(1, D))
        g = np.random.rand(np.random.randint(1, D))
        fg = hermfpmul(f, g)
        assert np.allclose(
            hermfval(f, x) * hermfval(g, x),
            hermfval([1], x) * hermfval(fg, x)
        )
    
    #cross-check with symbolic
    for _ in range(N):
        f, g = vbinom(randint(1, D)), vbinom(randint(1, D))
        assert np.allclose(
            hermfpmul(f, g),
            np.array(symbolic.hermfpmul(f, g).T, dtype=float)
        )



#quantum mechanics
def test_states_to_density():
    for d in range(D):
        v, w = np.random.rand(d), np.random.rand(d)
        assert np.allclose(
                states_to_density(v, w),
                np.outer(v, v) + np.outer(w, w)
        )

def test_T_matrix():
    #cross-check with symbolic
    for d in range(D):
        assert np.allclose(
            T_matrix(d),
            np.array(symbolic.T_matrix(d), dtype=float)
        )

def test_rho_to_g():
    x = np.linspace(-4, +4, 1000)
    for _ in range(10):
        rho = np.random.rand(4, 4)
        assert np.allclose(
            sum(rho[i, j]*hermfval(vecbasis(i), x)*hermfval(vecbasis(j), x)
                    for i in range(rho.shape[0]) for j in range(rho.shape[1])),
            hermfval([1], x) * hermfval(rho_to_g(rho), x)
        )
    
    #cross-check with symbolic
    for _ in range(N):
        m, n = randint(1, D), randint(1, D)
        rho = np.random.rand(m, n)
        assert np.allclose(
            rho_to_g(rho),
            np.array(symbolic.rho_to_g(rho).T, dtype=float)
        )



#random
def test_rand_ortho_pair():
    for _ in range(N):
        v, w = rand_ortho_pair(randint(2, D))
        assert np.isclose(np.linalg.norm(v), 1)
        assert np.isclose(np.linalg.norm(w), 1)
        assert np.isclose(v@w, 0)
