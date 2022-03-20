import matplotlib.pyplot as plt
from numpy import ndarray

plt.rcParams["font.family"] = "serif"
plt.rcParams["figure.figsize"] = (7, 7)
plt.rcParams["figure.dpi"] = 100


def graph(x: ndarray, y: ndarray, label: str, line_style: str = "r:"):
    plt.plot(x, y, line_style)
    plt.title(label)
    plt.xlabel("$x$")
    plt.ylabel("$f(x)$")
