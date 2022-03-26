from setup import *
from numpy import ndarray


def graph(x: ndarray, y: ndarray, label: str, line_style: str = "r:"):
    plt.plot(x, y, line_style)
    plt.title(label)
    plt.xlabel("$x$")
    plt.ylabel("$f(x)$")
