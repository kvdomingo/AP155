from .trapezoidal import f


def main():
    N = 10
    simp = []
    simp_error = []
    while N <= 1000:
        a = 0.0
        b = 2.0
        h = (b - a) / N
        s = f(a) + f(b)
        s += sum([f(a + (2 * k - 1) * h) * 4 for k in range(1, N // 2 + 1)])
        s += sum([f(a + 2 * k * h) * 2 for k in range(1, N // 2)])
        sum_ = 1 / 3 * h * s
        simp.append(sum_)
        dev = abs((4.4 - sum_) / 4.4) * 100
        simp_error.append(dev)
        print(f"sum = {sum_:.5f} ({dev:.2f}% err)")
        N *= 10


if __name__ == "__main__":
    main()
