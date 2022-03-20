from ch03 import *
from .gamma import gamma
from numpy import array


def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    x = range(1, 10)
    factorial_list = array([factorial(n) for n in x])
    gamma_list = array([gamma(n) for n in x])
    y = abs(factorial_list - gamma_list)
    plt.semilogy(x, y, "ro")
    plt.show()


if __name__ == "__main__":
    main()
