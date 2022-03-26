from numpy import array, pi, sqrt, zeros
from setup import *
from scipy.constants import epsilon_0


def calc_potential(
    q1: float, q2: float, q1_coord: [float, float], q2_coord: [float, float], coord: [float, float]
) -> float:
    rq1 = sqrt((q1_coord[1] - coord[1]) ** 2 + (q1_coord[0] - coord[0]) ** 2)
    rq2 = sqrt((q2_coord[1] - coord[1]) ** 2 + (q2_coord[0] - coord[0]) ** 2)
    if rq1 == 0 or rq2 == 0:
        return 0
    else:
        return (q1 * q2) / (4 * pi * epsilon_0 * rq1 * rq2)


def main():
    q1, q2 = 1, -1
    q1_loc = (0, -5)
    q2_loc = (0, 5)
    potential = array(zeros((101, 101)))
    for y, row in enumerate(potential):
        for x, val in enumerate(row):
            coord = (y - 50, x - 50)
            potential[y, x] = calc_potential(q1, q2, q1_loc, q2_loc, coord)
    fig, ax1 = plt.subplots()
    pot = ax1.imshow(potential)
    ax1.set_xlim(25, 75)
    ax1.set_ylim(25, 75)
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.hot()
    fig.colorbar(pot, ax=ax1, cmap="hot")
    plt.show()


if __name__ == "__main__":
    main()
