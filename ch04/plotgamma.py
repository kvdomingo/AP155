from setup import *
from .gamma import gamma
from numpy import linspace


def main():
    x = linspace(-5, 5, 1000)
    y = gamma(x)
    plt.vlines(list(range(0, -6, -1)), -10, 10, "r", linestyles="--")
    plt.plot(x, y, "g-")
    plt.ylim(-10, 10)
    plt.show()


if __name__ == "__main__":
    main()
