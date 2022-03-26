from numpy import array
from scipy.linalg import lu


def main():
    A = array(
        [
            [2, 1, 4, 1],
            [3, 4, -1, -1],
            [1, -4, 1, 5],
            [2, -2, 1, 3],
        ],
        "float64",
    )
    P, L, U = lu(A)
    print(
        *[f"A = \n{A}", f"P = \n{P}", f"L = \n{L}", f"U = \n{U}", f"P . A = \n{P.dot(A)}", f"L . U = \n{L.dot(U)}"],
        sep="\n\n",
    )


if __name__ == "__main__":
    main()
