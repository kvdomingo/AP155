from numpy import ndarray
from typing import Union, NewType

Numeric = NewType("Numeric", Union[float, ndarray])
