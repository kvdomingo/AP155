from numpy import pi
from astropy.constants.iau2015 import M_earth, R_earth
from astropy.constants.codata2018 import G as Gc


def altitude(T: float) -> float:
    G = Gc.value
    M = M_earth.value
    R = R_earth.value
    return ((G * M * T**2) / (4 * pi**2)) ** (1 / 3) - R


def main():
    T = float(input("Enter the desired orbital period in minutes: ")) * 60
    h = altitude(T)
    print(f"The orbital altitude must be {(h / 1000):.2f} km.")


if __name__ == "__main__":
    main()
