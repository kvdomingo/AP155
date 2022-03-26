from setup import *
from numpy import loadtxt, where, max
from .fourier_simple import dft


def main():
    spots = loadtxt(BASE_DIR / "Chapter 7 Resources" / "sunspots.txt", "float64")
    y = spots[:, 1]
    N = len(y)

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[
        0,
    ].plot(y, linewidth=1)
    ax[0].set_xlabel("time (months)")
    ax[0].set_ylabel("number of sunspots")
    ax[0].set_title("Observed no. of sunspots since Jan 1749")

    c = dft(y)
    power = c.real**2 + c.imag**2
    ax[1].plot(power[:50])
    ax[1].set_xlabel("frequency")

    plt.show()

    solar_max1 = where(y == max(y[1000:1100]))
    solar_max2 = where(y == max(y[1100:1200]))
    period = int(solar_max2[0]) - int(solar_max1[0])
    est_k = where(power == max(power[10:]))
    print(f"Estimated period ~ {period:.2f} months ({period/12:.2f} years)")
    print(f"Estimated k ~ {int(est_k[0])}")
    print(f"Period = {N/int(est_k[0]):.2f} months")


if __name__ == "__main__":
    main()
