from . import *
from numpy import cos, sin, linspace, pi


def main():
    theta = linspace(0, 10 * pi, 1000)
    r = theta**2
    x = r * cos(theta)
    y = r * sin(theta)
    graph(x, y, "Galilean spiral", "c-.")
    plt.show()


if __name__ == "__main__":
    main()
