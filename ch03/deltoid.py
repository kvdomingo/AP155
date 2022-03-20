from . import *
from numpy import cos, sin, linspace, pi


def main():
    theta = linspace(0, 2 * pi)
    x = 2 * cos(theta) + cos(2 * theta)
    y = 2 * sin(theta) - sin(2 * theta)
    graph(x, y, "Deltoid", "r:")
    plt.show()


if __name__ == "__main__":
    main()
