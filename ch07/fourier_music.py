from setup import *
from numpy import loadtxt, argmax
from scipy.fft import rfft


def main():
    piano = loadtxt(BASE_DIR / "Chapter 7 Resources" / "piano.txt", float)
    trumpet = loadtxt(BASE_DIR / "Chapter 7 Resources" / "trumpet.txt", float)
    sample_rate = 44100

    fig, ax = plt.subplots(2, 2, figsize=(12, 6))

    ax[0, 0].plot(piano[40000:40500])
    ax[0, 0].set_title("Piano")
    ax[0, 0].set_ylabel("amplitude")

    c = rfft(piano)
    ax[0, 1].plot(abs(c[:10000]))
    p = argmax(c)
    N = len(piano)
    f = p * sample_rate / N
    print(f"Piano frequency = {f:.2f} Hz")

    ax[1, 0].plot(trumpet[40000:40500])
    ax[1, 0].set_title("Piano")
    ax[1, 0].set_xlabel("sampling time")

    c = rfft(trumpet)
    ax[1, 1].plot(c[:10000])
    ax[1, 0].set_xlabel("frequency")
    p = argmax(c)
    N = len(trumpet)
    f = p * sample_rate / N
    print(f"Trumpet frequency = {f:.2f} Hz")

    plt.show()


if __name__ == "__main__":
    main()
