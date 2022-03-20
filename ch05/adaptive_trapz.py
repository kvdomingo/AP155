from numpy import sin, sqrt


def f(x: float) -> float:
    return sin(sqrt(100 * x)) ** 2


def I(i: int) -> float:
    N = 100
    a = 0.0
    b = 1.0
    h = (b - a) / N
    so = sum([f(a + k * h) for k in range(1, N, 2)]) * h
    if i == 0:
        si = sum([f(a + k * h) + 1 / 2 * (f(a) + f(b)) for k in range(1, N)]) * 1 / 2 * h
    else:
        si = 1 / 2 * I(i - 1)
    return si + so


def main():
    print(I(100))


if __name__ == "__main__":
    main()
