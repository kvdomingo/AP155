from ch03 import *
from . import *
from numpy import tanh, cosh, linspace


def f(x: Numeric) -> Numeric:
    return 1 + 1 / 2 * tanh(2 * x)


def df(x: Numeric, slices: int) -> Numeric:
    h = 4 / slices
    num = f(x + h / 2) - f(x - h / 2)
    return num / h


def sech(x: Numeric) -> Numeric:
    return 1 / cosh(x)


def g(x: Numeric) -> Numeric:
    return sech(2 * x) ** 2


def main():
    x = linspace(-2, 2, 100)
    y1 = df(x, 100)
    y2 = g(x)
    plt.plot(x, y1, "--", label="numeric")
    plt.plot(x, y2, ":", label="analytic")
    plt.xlabel("$x$")
    plt.ylabel("$f(x)$")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
