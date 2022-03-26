from numpy import arange, array, exp
from setup import *


def relax(acc: float) -> float:
    relax = []
    x = 1.0
    xprev = 1.0
    err = 1.0
    while err > acc:
        x = 1 - exp(-2 * x)
        err = abs(x - xprev) / xprev
        relax.append(x)
        xprev = x
    return relax[-1]


def relax_mod(c: float) -> float:
    relax = []
    x = 1.0
    xprev = 1.0
    err = 1.0
    acc = 1e-6
    while err > acc:
        x = 1 - exp(-c * x)
        err = abs(x - xprev) / xprev
        relax.append(x)
        xprev = x
    return relax[-1]


def main():
    print(relax(1e-6))

    x = arange(0.0, 3.1, 0.1)
    y = array([relax_mod(c) for c in x])
    plt.plot(x, y)
    plt.xlabel("$c$")
    plt.ylabel("$x$")
    plt.show()


if __name__ == "__main__":
    main()
