from .adaptive_trapz import f


def R(less: float, greater: float, m: int) -> float:
    return greater + (greater - less) / (4**m + 1)


def Rerr(own: float, top: float, m: int) -> float:
    return (own - top) / (4**m + 1)


def trapezoidal(N: int, a: float, b: float) -> float:
    h = (b - a) / N
    s = (1 / 2 * (f(a) + f(b))) + sum([f(a + k * h) for k in range(1, N)])
    return h * s


def main():
    N = 10
    a = 0.0
    b = 1.0
    less = trapezoidal(N, a, b)
    greater = trapezoidal(2 * N, a, b)
    Rtab = [[less], [greater]]
    i = 2
    m = 1
    err = Rerr(greater, less, m)
    end = False
    while (err > 1e-6) or not end:
        end = False
        Rnext = R(less, greater, m)
        Rtab[i - 1].append(Rnext)
        m += 1
        if m == i:
            end = True
            i += 1
            m = 1
            Rtab.append([trapezoidal(int(N * 2 ** (i - 1)), a, b)])
        err = Rerr(greater, less, m - 1)
        less = Rtab[i - 2][m - 2]
        greater = Rtab[i - 1][m - 2]

    print(*Rtab, sep="\n")
    print(err)


if __name__ == "__main__":
    main()
