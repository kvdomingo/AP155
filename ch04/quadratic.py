import sys
from numpy import sqrt


def quadratic1(a: float, b: float, c: float) -> tuple[float, float]:
    x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    return x1, x2


def quadratic2(a: float, b: float, c: float) -> tuple[float, float]:
    x1 = 2 * c / (-b - sqrt(b**2 - 4 * a * c))
    x2 = 2 * c / (-b + sqrt(b**2 - 4 * a * c))
    return x1, x2


def main(a: float, b: float, c: float):
    x1, x2 = quadratic1(a, b, c)
    print(f"Eq. 1:", f"\tx1 = {x1}", f"\tx2 = {x2}", sep="\n")

    x1, x2 = quadratic2(a, b, c)
    print(f"Eq. 2:", f"\tx1 = {x1}", f"\tx2 = {x2}", sep="\n")


if __name__ == "__main__":
    main(*map(lambda s: float(s), sys.argv[1:]))
