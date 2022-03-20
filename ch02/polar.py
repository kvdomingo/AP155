from numpy import pi, cos, sin


def main():
    r = float(input("Enter the radius: "))
    theta = float(input("Enter the angle in degrees: "))
    theta *= pi / 180
    x = r * cos(theta)
    y = r * sin(theta)
    print(f"x = {x:.2f}, y = {y:.2f}")


if __name__ == "__main__":
    main()
