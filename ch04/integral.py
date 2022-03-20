from numpy import sqrt, pi


def main():
    N = 100000
    h = 2 / N
    I = 0
    for k in range(1, N + 1):
        x = -1 + h * k
        y = sqrt(1 - x**2)
        I += h * y
    print(
        f"Slices = {N}",
        f"Integral = {I}",
        f"Actual value = {pi/2}",
        f"Error = {abs((pi/2 - I) / (pi/2) * 100)}%",
        sep="\n",
    )


if __name__ == "__main__":
    main()
