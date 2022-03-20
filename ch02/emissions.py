from scipy.constants import Rydberg


def main():
    R = Rydberg * 1e-9
    arr = []
    for m in range(1, 4):
        arr.append([])
        print(f"\nSeries for m = {m}")
        for n in range(m + 1, m + 6):
            arr[m - 1].append(1 / (R * (1 / m**2 - 1 / n**2)))
        print(*map(lambda x: f"\t{x:.2f} nm", arr[m - 1]), sep="\n")


if __name__ == "__main__":
    main()
