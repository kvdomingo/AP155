from . import *
from numpy import pi, zeros, sqrt, sin


def main():
    wavelength = 5.0
    k = 2 * pi / wavelength
    xi0 = 1.0
    sep = 20
    side = 100
    points = 500
    spacing = side / points
    x1 = side / 2 + sep / 2
    y1 = side / 2
    x2 = side / 2 - sep / 2
    y2 = side / 2
    xi = zeros((points, points), float)
    for i in range(points):
        y = spacing * i
        for j in range(points):
            x = spacing * j
            r1 = sqrt((x - x1) ** 2 + (y - y1) ** 2)
            r2 = sqrt((x - x2) ** 2 + (y - y2) ** 2)
            xi[i, j] = xi0 * sin(k * r1) + xi0 * sin(k * r2)
    plt.imshow(xi, origin="lower", extent=[0, side, 0, side])
    plt.gray()
    plt.show()


if __name__ == "__main__":
    main()
