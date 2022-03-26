from numpy import array, zeros


def main():
    A = array(
        [
            [4, -1, -1, -1],
            [-1, 3, 0, -1],
            [-1, 0, 3, -1],
            [-1, -1, -1, 4],
        ],
        dtype="float64",
    )
    v = array([5, 0, 5, 0], "float64")
    N = len(v)

    for m in range(N):
        div = A[m, m]
        A[m] /= div
        v[m] /= div
        for i in range(m + 1, N):
            mult = A[i, m]
            A[i] -= mult * A[m]
            v[i] -= mult * v[m]

    x = zeros(N, "float64")
    for m in range(N - 1, -1, -1):
        x[m] = v[m]
        for i in range(m + 1, N):
            x[m] -= A[m, i] * x[i]

    print(*[f"V{i + 1} = {x[i]:.2f} V" for i in range(len(x))], sep="\n")


if __name__ == "__main__":
    main()
