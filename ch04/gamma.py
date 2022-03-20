import sys
from numpy import euler_gamma, exp, prod, ndarray
from fractions import Fraction
from typing import Union


def gamma(z: Union[float, ndarray]) -> Union[float, ndarray]:
    upper_limit = 100000
    outer = z * exp(euler_gamma * z)
    inner = prod([(1 + (z / n)) * exp(-z / n) for n in range(1, upper_limit + 1)], axis=0)
    return 1 / (outer * inner)


def main(z: str):
    try:
        z = float(z)
    except ValueError:
        z = float(Fraction(z))
    print(gamma(z))


if __name__ == "__main__":
    main((sys.argv[1]))
