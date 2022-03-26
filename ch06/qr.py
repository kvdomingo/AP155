from numpy import abs, array, diagonal, identity, logical_not, ndarray, zeros_like
from numpy.linalg import norm


def qr(A: ndarray) -> (ndarray, ndarray):
    Q = zeros_like(A, dtype="float64")
    R = zeros_like(A, dtype="float64")
    for i in range(len(A)):
        sum_ = 0
        for j in range(i):
            qa = Q[:, j].dot(A[:, i])
            sum_ += qa * Q[:, j]
            R[j, i] = qa
        u = A[:, i] - sum_
        unorm = norm(u)
        q = u / unorm
        Q[:, i] = q
        R[i, i] = unorm
    return Q, R


def main():
    A = array(
        [
            [1, 4, 8, 4],
            [4, 2, 3, 7],
            [8, 3, 6, 9],
            [4, 7, 9, 2],
        ],
        "float64",
    )
    N = len(A)
    V = identity(N)
    epsilon = 1e-6
    off_diag = logical_not(V)
    while not abs(A * off_diag < epsilon).all():
        Q, R = qr(A)
        A = R.dot(Q)
        V = V.dot(Q)
    print(diagonal(A))


if __name__ == "__main__":
    main()
