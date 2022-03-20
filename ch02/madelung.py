from multiprocessing import Pool, cpu_count
from numpy import sqrt

NUM_CORES = (cpu_count() // 2) - 1


def job(chunk: list[int]) -> float:
    return sum([(-1) ** (i + j + k) / sqrt(i**2 + j**2 + k**2) for i in chunk for j in chunk for k in chunk])


def main():
    L = 1000
    arr = [*range(-L, 0), *range(1, L + 1)]
    chunks = [arr[i : i + NUM_CORES] for i in range(0, len(arr), NUM_CORES)]
    pool = Pool(NUM_CORES).imap_unordered(job, chunks)
    M = abs(sum(pool))
    print(f"M = {M:.2f}")


if __name__ == "__main__":
    main()
