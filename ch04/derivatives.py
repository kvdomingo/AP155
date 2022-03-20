def f(x: float) -> float:
    return x * (x - 1)


def df(x: float, delta: float) -> float:
    return (f(x + delta) - f(x)) / delta


def main():
    print(f"Delta 1e-10 = {df(1, 1e-10)}")


if __name__ == "__main__":
    main()
