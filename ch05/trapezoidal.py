def f(x: float) -> float:
    return x**4 - 2 * x + 1


def main():
    N = 10
    trap = []
    trap_error = []
    while N <= 1000:
        a = 0.0
        b = 2.0
        h = (b - a) / N
        s = 1 / 2 * (f(a) + f(b))
        s += sum([f(a + k * h) for k in range(1, N)])
        sum_ = h * s
        trap.append(sum_)
        dev = abs((4.4 - sum_) / 4.4) * 100
        trap_error.append(dev)
        print(f"sum = {sum_:.5f} ({dev:.2f}% err)")
        N *= 10


if __name__ == "__main__":
    main()
