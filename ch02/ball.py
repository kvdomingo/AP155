from scipy.constants import g


def main():
    h = float(input("Enter the height of the tower in meters: "))
    t = float(input("Enter the time elapsed in seconds: "))
    s = 1 / 2 * g * t**2
    H = h - s
    if H <= 0:
        print("The ball has already hit the ground!")
    else:
        print(f"The ball is {H:.2f} meters above the ground")


if __name__ == "__main__":
    main()
