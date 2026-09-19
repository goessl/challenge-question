"""Algebra."""



from sympy import S, Poly, Matrix, Symbol, symbols



__all__ = (
    'symbol_matrix', 'symbol_matrix_symmetric', 'linear_solutions'
)



def symbol_matrix(sym: str, height: int, width: int) -> Matrix:
    r"""Return a matrix of indexed symbolic coefficients.
    
    $$
        \begin{pmatrix}
            \cdot_{00} & \cdot_{01} & \cdots \\
            \cdot_{10} & \cdot_{11} & \cdots \\
            \vdots     & \vdots     & \ddots
        \end{pmatrix}
    $$
    
    Parameters
    ----------
    sym
        Coefficient symbol.
    height, width
        Matrix dimensions.
    
    Returns
    -------
    :
        Matrix of indexed symbolic coefficients
    
    See also
    --------
    - [`symbol_matrix_symmetric`][cq.symbolic.algebra.symbol_matrix_symmetric]
    """
    if height>10 or width>10:
        raise NotImplementedError('possible index ambiguity')
    return Matrix(height, width, symbols(f'{sym}:{height}:{width}'))

def symbol_matrix_symmetric(sym: str, hw: int) -> Matrix:
    r"""Return a symmetric matrix of indexed symbolic coefficients.
    
    $$
        \begin{pmatrix}
            \cdot_{00} & \cdot_{01} & \cdots \\
            \cdot_{01} & \cdot_{11} & \cdots \\
            \vdots     & \vdots     & \ddots
        \end{pmatrix}
    $$
    
    Parameters
    ----------
    sym
        Coefficient symbol.
    hw
        Matrix dimensions.
    
    Returns
    -------
    :
        Symmetric matrix of indexed symbolic coefficients
    
    See also
    --------
    - [`symbol_matrix`][cq.symbolic.algebra.symbol_matrix]
    """
    if hw > 10:
        raise NotImplementedError('possible index ambiguity')
    return Matrix(hw, hw, lambda i, j: Symbol(f'{sym}{min(i,j)}{max(i,j)}'))

def linear_solutions(p: Poly, *t: Symbol) -> Matrix:
    r"""Return the parametrised solution set for a linear equation.
    
    $$
        \begin{aligned}
            ax+b=0 \quad &\Rightarrow \quad \begin{pmatrix}
                -\frac{b}{a}
            \end{pmatrix} \ \text{(Solution set for $x$)} \\
            ax+by+c=0 \quad &\Rightarrow \quad \begin{pmatrix}
                \frac{-ac}{a^2+b^2}+bt \\
                \frac{-bc}{a^2+b^2}-at
            \end{pmatrix} \ \text{(Solution set for $(x, y)$)}
        \end{aligned}
    $$
    
    Parameters
    ----------
    p
        Linear equation, in the generators for which shall be solved.
    t
        Free parameters to use.
    
    Returns
    -------
    :
        Parametrised solution set.
    
    References
    ----------
    - [Going vectorial - Degree 3 - Some Algebra](../going_vectorial/degree_3/some_algebra.md)
    """
    if not isinstance(p, Poly):
        raise TypeError('p must be a sympy.Poly in the symbols to solve')
    if not len(t) == len(p.gens)-1:
        raise ValueError(
            'one less free parameter than generators must be provided')
    
    d = p.as_dict()
    match len(p.gens):
        case 1: #ax+b=0
            if not d.keys() <= {(0,), (1,)}:
                raise ValueError('p is not linear')
            return Matrix([p.root(0).simplify()])
        
        case 2: #ax+by+c=0
            if not d.keys() <= {(0,0), (0,1), (1,0)}:
                raise ValueError('p is not linear')
            
            a = d.get((1,0), S.Zero)
            b = d.get((0,1), S.Zero)
            c = d.get((0,0), S.Zero)
            x = (-a*c/(a**2+b**2)+b*t[0]).simplify()
            y = (-b*c/(a**2+b**2)-a*t[0]).simplify()
            return Matrix([x, y])
        
        case _:
            raise NotImplementedError('higher dimension not yet implemented')
