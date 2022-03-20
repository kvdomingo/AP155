from numpy import sqrt
from scipy.constants import electron_mass as m, hbar


def main():
    E = 10
    V = 9
    k1 = sqrt(2 * m * E) / hbar
    k2 = sqrt(2 * m * (E - V)) / hbar
    T = (4 * k1 * k2) / (k1 + k2) ** 2
    R = ((k1 - k2) / (k1 + k2)) ** 2
    print(f"T = {T:.2f}", f"R = {R:.2f}", f"Total = {T+R:.2f}", sep="\n")


if __name__ == "__main__":
    main()
