from .satellite import altitude


def main():
    T1 = 24 * 60 * 60
    T2 = 23.93 * 60 * 60
    h1, h2 = altitude(T1), altitude(T2)
    print(f"Orbital altitude for 24 hour period: {h1/1000:.2f} km")
    print(f"Orbital altitude for 23.93 hour period: {h2 / 1000:.2f} km")
    print(f"Orbital altitude difference: {(h1 - h2) / 1000:.2f} km")


if __name__ == "__main__":
    main()
