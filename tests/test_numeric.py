from cq.numeric import *
from cq.pythonic import vecbasis, vrandz
from cq import symbolic
from random import randint
from sympy import Symbol
import numpy as np



runs = 10
vectorisation = 5
degree = 5



#Hermite functions
def test_hermfval():
    x = np.linspace(-12, +12, 10000)
    H = np.array([hermfval(vecbasis(j), x) for j in range(6)])
    G = np.trapezoid(H[:, None, :]*H[None, :, :], x, axis=-1)
    assert np.allclose(G, np.eye(6)) #orthonormality
    
    #cross-check with symbolic
    for _ in range(runs):
        f = np.random.rand(randint(1, degree))
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
    #vectorised
    for _ in range(runs):
        M = randint(1, vectorisation)
        f = np.random.rand(M, randint(1, degree))
        fp = hermfder(f)
        for i in range(M):
            assert np.allclose(fp[i], hermfder(f[i]))
    
    #cross-check with symbolic
    for _ in range(runs):
        f = vrandz(randint(0, degree))
        prediction = hermfder(f)
        actual = symbolic.hermfder(f)
        assert np.allclose(
            prediction,
            np.asarray(actual.T, dtype=float)
        )

def test_hermfkin():
    #vectorised
    for _ in range(runs):
        M = randint(1, vectorisation)
        f = np.random.rand(M, randint(1, degree))
        T = hermfkin(f)
        for i in range(M):
            assert np.allclose(T[i], hermfkin(f[i]))
    
    #cross-check with symbolic
    for _ in range(runs):
        f = vrandz(randint(0, degree))
        prediction = hermfkin(f)
        actual = symbolic.hermfkin(f)
        assert np.isclose(prediction, float(actual))

def test_hermfpmul():
    x = np.linspace(-4, +4, 1000)
    for _ in range(runs):
        f = np.random.rand(randint(1, degree))
        g = np.random.rand(randint(1, degree))
        fg = hermfpmul(f, g)
        assert np.allclose(
            hermfval(f, x) * hermfval(g, x),
            hermfval([1], x) * hermfval(fg, x)
        )
    
    #vectorised
    for _ in range(runs):
        M = randint(1, vectorisation)
        f = np.random.rand(M, randint(1, degree))
        g = np.random.rand(M, randint(1, degree))
        fg = hermfpmul(f, g)
        for i in range(M):
            assert np.allclose(fg[i], hermfpmul(f[i], g[i]))
    
    #cross-check with symbolic
    for _ in range(runs):
        f, g = vrandz(randint(1, degree)), vrandz(randint(1, degree))
        assert np.allclose(
            hermfpmul(f, g),
            np.array(symbolic.hermfpmul(f, g).T, dtype=float)
        )



#quantum mechanics
def test_states_to_density():
    for d in range(degree):
        v, w = np.random.rand(d), np.random.rand(d)
        assert np.allclose(
                states_to_density(v, w),
                np.outer(v, v) + np.outer(w, w)
        )

def test_T_matrix():
    #cross-check with symbolic
    for d in range(degree):
        assert np.allclose(
            T_matrix(d),
            np.array(symbolic.T_matrix(d), dtype=float)
        )

def test_rho_to_g():
    x = np.linspace(-4, +4, 1000)
    for _ in range(runs):
        d = randint(1, degree)
        rho = np.random.rand(d, d)
        g = rho_to_g(rho)
        assert np.allclose(
            sum(rho[i, j]*hermfval(vecbasis(i), x)*hermfval(vecbasis(j), x)
                    for i, j in np.ndindex(rho.shape)),
            hermfval([1], x) * hermfval(g, x)
        )
    
    #vectorised
    for _ in range(runs):
        M = randint(1, vectorisation)
        rho = np.random.rand(M, 4, 4)
        g = rho_to_g(rho)
        for i in range(M):
            assert np.allclose(g[i], rho_to_g(rho[i]))
    
    #cross-check with symbolic
    for _ in range(runs):
        m, n = randint(1, degree), randint(1, degree)
        rho = np.random.rand(m, n)
        assert np.allclose(
            rho_to_g(rho),
            np.array(symbolic.rho_to_g(rho).T, dtype=float)
        )



#random
def test_rand_ortho_pair():
    for _ in range(runs):
        N = randint(2, degree)
        v, w = rand_ortho_pair(N)
        
        assert v.shape == w.shape == (N,)
        assert np.isclose(np.linalg.norm(v), 1)
        assert np.isclose(np.linalg.norm(w), 1)
        assert np.isclose(v@w, 0)
    
    #vectorised
    for _ in range(runs):
        M, N = randint(1, vectorisation), randint(2, degree)
        v, w = rand_ortho_pair(N, M)
        
        assert v.shape == w.shape == (M, N)
        assert all(np.isclose(np.linalg.norm(v[i]), 1) for i in range(M))
        assert all(np.isclose(np.linalg.norm(w[i]), 1) for i in range(M))
        assert all(np.isclose(v[i]@w[i], 0) for i in range(M))
