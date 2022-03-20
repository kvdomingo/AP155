def main():
    arr = []
    m = 1
    n = 1
    next_ = m + n
    while m <= 1000:
        arr.append(m)
        m, n = n, next_
        next_ = m + n
    print(*arr, sep="\n")


if __name__ == "__main__":
    main()
