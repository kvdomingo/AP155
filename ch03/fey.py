from . import *
from numpy import cos, sin, linspace, pi, exp


def main():
    theta = linspace(0, 24 * pi, 100000)
    r = exp(cos(theta)) - 2 * cos(4 * theta) + sin(theta / 12) ** 5
    x = r * cos(theta)
    y = r * sin(theta)
    graph(x, y, "Fey's function", "m-")
    plt.show()


if __name__ == "__main__":
    main()
