from setup import *
from numpy import ndarray, arange, ones, zeros, exp, pi, linspace, sin
from scipy.signal import sawtooth


def dft(y: ndarray) -> ndarray:
    N = len(y)
    c = zeros(N // 2 + 1, complex)
    n = arange(0, N)
    for k in range(N // 2 + 1):
        c[k] = sum(y * exp(-1j * 2 * pi * k * n / N))
    return c


def main():
    N = 1000
    fig, ax = plt.subplots(3, 2, figsize=(8, 10))

    y = ones(N)
    y[: N // 2] = 0
    ax[0, 0].plot(y)
    ax[0, 0].set_title("Single-cycle square wave")

    c = dft(y)
    ax[0, 1].plot(abs(c))

    x = linspace(0, 1000, N)
    y = sawtooth(2 * pi * 5 * x)
    ax[1, 0].plot(x, y)
    ax[1, 0].set_title("Sawtooth wave")
    ax[1, 0].set_ylabel("amplitude")

    c = dft(y)
    ax[1, 1].plot(abs(c))

    n = arange(N)
    y = sin(pi * n / N) * sin(20 * pi * n / N)
    ax[2, 0].plot(y)
    ax[2, 0].set_title("Modulated sine wave")
    ax[2, 0].set_xlabel("time")

    c = dft(y)
    ax[2, 1].plot(abs(c))
    ax[2, 1].set_xlabel("frequency")

    plt.show()


if __name__ == "__main__":
    main()
