from numpy import exp, ndarray
from typing import Union


def f(x: Union[float, ndarray]) -> Union[float, ndarray]:
    return 1 - exp(-2 * x)


def df(x: Union[float, ndarray]) -> Union[float, ndarray]:
    return 2 * exp(-2 * x)


def overrelax(w: float) -> float:
    relax = []
    x, xprev = 1.0, 1.0
    err = 1.0
    acc = 1e-6
    while err > acc:
        Dx = f(x) - x
        x += (1 + w) * Dx
        err = abs((xprev - x) / (1 - 1 / ((1 + w) * df(x) - w)))
        relax.append(x)
        xprev = x
    print(f"Final x = {relax[-1]}", f"Num. iters = {len(relax)}", sep="\n")
    return relax[-1]


def main():
    overrelax(0.5)


if __name__ == "__main__":
    main()
