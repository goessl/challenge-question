"""Challenge-Question support package.

Consisting solely of three modules:

- [`pythonic`][cq.pythonic]

    Pure Python helpers using built-in types
    like `int`s and `fractions.Fraction`s.

- [`numeric`][cq.numeric] & [`symbolic`][cq.symbolic]

    Near mirrors of each other with submodules for
    
    - Hermite functions
    - quantum mechanics
    - random sampling
    - automatic algebra & polynomials

Due to otherwise resulting in name clashes
always explicitly import from the latter two:

```python
from cq.numeric import ...
```
"""

from . import pythonic, numeric, symbolic
