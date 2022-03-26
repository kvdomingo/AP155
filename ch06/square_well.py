from numpy import tan, sqrt, linspace
from scipy.constants import electron_mass, hbar
from ch03 import *

V = 20
w = 1e-9


def y1(E: ndarray) -> ndarray:
    return tan(sqrt(w**2 * electron_mass * E / 2 * hbar**2))


def y2(E: ndarray) -> ndarray:
    return sqrt((V - E) / E)


def y3(E: ndarray) -> ndarray:
    return -sqrt(E / (V - E))


def main():
    E = linspace(0, 20, 1000)
    plt.plot(E, y1(E), "c", label="$y_1$")
    plt.plot(E, y2(E), "r", label="$y_2$")
    plt.plot(E, y3(E), "y", label="$y_3$")
    plt.xlabel("$E$")
    plt.ylabel("$y$")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
