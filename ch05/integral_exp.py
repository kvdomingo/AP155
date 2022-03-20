from ch03 import *
from numpy import exp, linspace


def E(t: float) -> float:
    return exp(-(t**2))


def main():
    N = 10
    a = 0.0
    sum_ = []
    for i in range(50):
        b = i / 10
        h = (b - a) / N
        s = E(a) + E(b)
        s += sum([E(a + (2 * k - 1) * h) * 4 for k in range(1, N // 2 + 1)])
        s += sum([E(a + 2 * k * h) * 2 for k in range(1, N // 2)])
        sum_.append(1 / 3 * h * s)

    x = linspace(0, 3)
    plt.plot(x, sum_)
    plt.xlabel("$x$")
    plt.ylabel("$E(x)$")
    plt.show()


if __name__ == "__main__":
    main()
