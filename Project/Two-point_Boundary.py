from thomas import thomas
import numpy as np


def xi(i, x0, h):
    return x0 + i * h

def r(x):
    return 4 / x

def s(x):
    return 2 / x**2

def t(x):
    return 2 * np.log(x) / x**2

def y(x):
    return 4/x - 2/(x**2) + np.log(x) - 3/2

def solve(n, x0, xn):
    '''Solves Ax = b, returns x'''

    h = (xn - x0) / (n + 1)

    # Diagonals
    main = []
    sub = []
    super = []
    b = []
    y_ex = []

    # Constructs
    for i in np.arange(1, n + 1):

        x_i = xi(i, x0, h)

        main += [2 - h**2 * s(x_i)]
        sub += [-1 + h * r(x_i) / 2]
        super += [-1 - h * r(x_i) / 2]
        b += [-h**2 * t(x_i)]

        y_ex += [y(x_i)]
    
    # Boundary values
    y_left = y(x0)
    y_right = y(xn)

    b[0] -= sub[0] * y_left
    b[-1] -= super[-1] * y_right

    A = (
        np.diag(sub[1:], k=-1)
        + np.diag(main, k=0)
        + np.diag(super[:-1], k=1)
    )

    y_approx = thomas(A, np.array(b))

    #print('\nA:', A)
    #print('\nb:', np.array(b))

    #print('\nApproximate Y:', y_approx)
    #print('\nExact Y:', np.array(y_ex))
    #print('\nError:', inf_norm_error(y_ex, y_approx))

    return inf_norm_error(np.array(y_ex), y_approx)

def inf_norm_error(y_ex, y_approx):
    """Return error between exact y and approximate y using infinity-norm."""
    # Difference
    error = np.linalg.norm(y_approx - y_ex, ord=np.inf)
    return error

if __name__ == "__main__":
    nodes = [10, 20, 40, 80, 160, 320]
    errors = []

    for n in nodes:
        error = solve(n, 1, 2)
        errors.append(error)

    print("Errors:", errors)

    print("\nResults:")
    print(f"{'n':>5} {'Error':>15} {'Error ratio':>15} {'Expected ratio':>16}")

    for i, n in enumerate(nodes):
        if i == 0:
            print(f"{n:5d} {errors[i]:15.8e} {'-':>15} {'-':>16}")
        else:
            ratio = errors[i-1] / errors[i]

            h_old = 1 / (nodes[i-1] + 1)
            h_new = 1 / (n + 1)
            expected = (h_old / h_new)**2

            print(
                f"{n:5d} {errors[i]:15.8e} "
                f"{ratio:15.6f} {expected:16.6f}"
            )
