def catalan(n: int, prev: int) -> int:
    return (4 * n + 2) * prev // (n + 2)


def main():
    C = [1, 1]
    while C[-1] <= 1e9:
        C.append(catalan(len(C), C[-1]))
    print(*C, sep="\n")


if __name__ == "__main__":
    main()
