import numpy as np
import matplotlib.pyplot as plt


def compute_derivative(func, x, dx):
    """
    func: the function to compute derivative of
    x:    the point where to compute the derivative
    dx:   small value used to approximate the derivative (smaller dx = better approximation)
    """
    return (func(x+dx) - func(x)) / (dx)


def square(x):
    """
    returns x^2
    derivative of this function is 2*x
    """
    return x**2


DX = 1e-2
interval = np.linspace(0, 10, 101, dtype=np.float64)      # 101 points between 0 and 10
derivatives = np.empty(len(interval), dtype=np.float64)   # will store derivative for each point in interval


# CALCULATE DERIVATIVE
# calculate the derivative
for i in range(len(interval)):
    # we can pass functions as arguments to other functions
    derivatives[i] = compute_derivative(square, interval[i], DX)


# CALCULATE TRUE DERIVATIVE
# the real derivatives are known (equal to x*2) (numpy will multiply all elements in interval array by 2)
real_derivatives = 2 * interval


# DIFFERENCES (ERROR)
# expected value - computed value
differences = real_derivatives - derivatives


# PLOT THE ERRORS

# plot over the 101 points (interval array is x axis, differences array is y axis)
plt.plot(interval, differences, label=f"DX = {DX:.0E}")

# as we can see, the derivatives diverge (become a worse approximation)

# plot errors for different DX values
for DX in [1e-3, 1e-6, 1e-10, 1e-11]:
    # do the derivative calculations again with given DX
    for i in range(len(interval)):
        derivatives[i] = compute_derivative(square, interval[i], DX)
    differences = real_derivatives - derivatives

    # plot
    plt.plot(interval, differences, label=f"DX = {DX:.0E}")


plt.legend()
plt.show()
