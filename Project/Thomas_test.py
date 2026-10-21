import numpy as np
import time
from thomas import thomas
from matplotlib import pyplot as plt

Ns = [100, 200, 400, 800, 1600, 3200]

times_thomas = []
times_lu = []

for N in Ns:

    # Generate tridiagonal matrix
    main = N * np.ones(N) + np.random.rand(N)
    sub = np.random.rand(N - 1)
    super = np.random.rand(N - 1)

    A = (
        np.diag(sub, k=-1)
        + np.diag(main, k=0)
        + np.diag(super, k=1)
    )

    # Known solution and manufactured RHS
    known_x = np.pi * np.ones(N)
    b = A @ known_x

    # Time Thomas algorithm
    start = time.perf_counter()
    x = thomas(A, b)
    end = time.perf_counter()

    times_thomas.append(end - start)

    # Time standard dense solve
    start = time.perf_counter()
    x_lu = np.linalg.solve(A, b)
    end = time.perf_counter()

    times_lu.append(end - start)


print("N        Thomas time        LU time")

for N, t1, t2 in zip(Ns, times_thomas, times_lu):
    print(f"{N:<8} {t1:<18.6e} {t2:<18.6e}")


Ns = np.array([100, 200, 400, 800, 1600, 3200, 6400])

# Number of repetitions for each size
reps = 500

times = []

for N in Ns:

    # Create the tridiagonal matrix
    main = N * np.ones(N) + np.random.rand(N)
    sub = np.random.rand(N - 1)
    super = np.random.rand(N - 1)

    A = (
        np.diag(sub, k=-1)
        + np.diag(main, k=0)
        + np.diag(super, k=1)
    )

    # Known solution
    known_x = np.pi * np.ones(N)

    # Manufacture b
    b = A @ known_x

    # Warm-up
    thomas(A, b)

    # Timing
    trial_times = []

    for _ in range(reps):
        start = time.perf_counter()
        thomas(A, b)
        trial_times.append(time.perf_counter() - start)

    times.append(np.median(trial_times))


# Convert to NumPy array
times = np.array(times)


# Print timing table
print("N        Thomas time")
print("--------------------")

for N, t in zip(Ns, times):
    print(f"{N:<8} {t:.6e}")


# Plot

# Reference O(N) line
reference = times[0] * Ns / Ns[0]

plt.figure(figsize=(7, 5))

plt.loglog(Ns, times, 'o-', label='Thomas algorithm')
plt.loglog(Ns, reference, '--', label=r'$O(N)$ reference')

plt.xlabel('N')
plt.ylabel('CPU time [s]')
plt.title('Computational cost of the Thomas algorithm')
plt.legend()
plt.grid(True, which='both')

plt.tight_layout()
plt.savefig("thomas_timing.eps", dpi=300)
plt.show()