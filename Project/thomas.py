import numpy as np


def thomas(a, b, c, d):
    """
    Solve Ax = d where A is tridiagonal using the Thomas algorithm.

    Parameters
    ----------
    a : ndarray
        Subdiagonal, length N-1.
    b : ndarray
        Main diagonal, length N.
    c : ndarray
        Superdiagonal, length N-1.
    d : ndarray
        Right-hand side, length N.

    Returns
    -------
    x : ndarray
        Solution to Ax = d.
    """
    
    N = len(b)

    # Make copies so that the input arrays are not modified.
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    c = np.asarray(c, dtype=float)
    d = np.asarray(d, dtype=float)

    # Scratch space for the modified superdiagonal
    cp = np.zeros(N - 1)

    # Modified right-hand side
    dp = np.zeros(N)

    # First equation
    cp[0] = c[0] / b[0]
    dp[0] = d[0] / b[0]

    # Forward elimination
    for i in range(1, N):
        denom = b[i] - a[i - 1] * cp[i - 1]

        if i < N - 1:
            cp[i] = c[i] / denom

        dp[i] = (d[i] - a[i - 1] * dp[i - 1]) / denom

    # Back substitution
    x = np.zeros(N)
    x[-1] = dp[-1]

    for i in range(N - 2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]

    return x

if __name__ == "__main__":
    N = 100

    # create three random vectors
    main = N * np.ones((N,)) + np.random.random(N)
    sub = np.random.random(N - 1)
    super = np.random.random(N - 1)
    # use the ’np.diag’ command to create tridiagonal matrix
    A = np.diag(sub, k=-1) + np.diag(main, k=0) + np.diag(super, k=1)

    known_x = np.pi * np.ones((N,)) # create known solution vector filled with pi
    manuf_d = A @ known_x # manufacture the right-hand-side

    # Solve using Thomas algorithm
    computed_x = thomas(sub, main, super, manuf_d)

    # Compare
    print("Maximum absolute error:")
    print(np.max(np.abs(computed_x - known_x)))

    print("NumPy residual:")
    print(np.linalg.norm(A @ computed_x - manuf_d))
