import numpy as np
import matplotlib.pyplot as plt


def lorenz(init_x, init_y, init_z, sigma, rho, beta, time_range):
    """
    uses sigma, rho, and beta values
    updates x, y, and z according to Lorenz equations
    returns array of x, y, and z values varying with time
    """

    xs = np.empty(len(time_range), dtype=time_range.dtype)
    ys = np.empty(len(time_range), dtype=time_range.dtype)
    zs = np.empty(len(time_range), dtype=time_range.dtype)

    # set initial values of variables
    xs[0] = init_x
    ys[0] = init_y
    zs[0] = init_z

    # delta time
    dt = time_range[1] - time_range[0]

    for i in range(len(time_range) - 1):
        # calculate variables at time step i+1 from their values at time step i
        
        x, y, z = xs[i], ys[i], zs[i]

        # just get dt on the other side of equation
        dx = ( sigma*(y - x)   ) * dt
        dy = ( rho*x - y - x*z ) * dt
        dz = ( x*y - beta*z    ) * dt

        xs[i+1] = x + dx
        ys[i+1] = y + dy
        zs[i+1] = z + dz

    return (xs, ys, zs)


# model parameters
SIGMA = 10
RHO   = 28
BETA  = 3

# initial values of variables
init_x = 0.
init_y = 1.
init_z = 1.05

print(f"initial values: x = {init_x}, y = {init_y}, z = {init_z}")

# time range
t = np.linspace(0, 50, 5000, endpoint=True, dtype=np.float32)

# calculate x, y, and z
x, y, z = lorenz(init_x, init_y, init_x, SIGMA, RHO, BETA, t)

# prepare 2 plots (ax1: x,y,z as a function of time,
#                  ax2: x     as a function of y)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))
fig.suptitle(r'$\sigma = ' + str(SIGMA) + r',   \rho = ' + str(RHO) + r',   \beta = ' + str(BETA) + r"$")

# plot x, y, z with respect to time
ax1.set_title("x,y,z as a function of time")
ax1.plot(t, x, label="x")
ax1.plot(t, y, label="y")
ax1.plot(t, z, label="z")
ax1.legend()

# plot x with respect to y phase diagram
ax2.set_title("x versus y phase diagram")
ax2.plot(y, x)

plt.show()
