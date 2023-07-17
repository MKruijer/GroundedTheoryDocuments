import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress


def main_function():
    precision_values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.909090909, 0.916666667, 0.923076923, 0.928571429, 0.866666667, 0.875, 0.882352941, 0.888888889, 0.894736842, 0.9, 0.904761905, 0.909090909, 0.913043478, 0.916666667, 0.92, 0.923076923, 0.925925926, 0.928571429, 0.931034483, 0.933333333, 0.935483871, 0.9375, 0.909090909, 0.911764706, 0.914285714, 0.888888889, 0.891891892, 0.894736842, 0.897435897, 0.875, 0.853658537, 0.857142857, 0.860465116, 0.863636364, 0.866666667, 0.869565217, 0.872340426, 0.875, 0.87755102, 0.88, 0.882352941, 0.884615385, 0.886792453, 0.888888889, 0.890909091, 0.892857143, 0.894736842, 0.896551724, 0.881355932, 0.883333333, 0.885245902, 0.870967742, 0.873015873, 0.859375, 0.861538462, 0.863636364, 0.850746269, 0.838235294, 0.826086957, 0.814285714, 0.802816901, 0.791666667, 0.794520548, 0.783783784, 0.786666667, 0.789473684, 0.779220779, 0.782051282, 0.772151899, 0.7625, 0.765432099, 0.768292683, 0.771084337, 0.761904762, 0.752941176, 0.744186047, 0.735632184, 0.738636364, 0.730337079, 0.722222222, 0.714285714, 0.706521739, 0.698924731, 0.691489362, 0.694736842, 0.6875, 0.680412371, 0.673469388, 0.676767677, 0.67]


    # Generate x-values for the data entry indices
    x_values = np.arange(1, len(precision_values) + 1)

    # Define the quadratic function
    def quadratic_func(x, a, b, c):
        return a * x ** 2 + b * x + c

    # Perform curve fitting to find the best-fit quadratic curve
    popt_quadratic, _ = curve_fit(quadratic_func, x_values, precision_values)

    # Generate the y-values for the quadratic curve
    y_values_quadratic = quadratic_func(x_values, *popt_quadratic)

    # Perform linear regression to find the best-fit line
    slope, intercept, _, _, _ = linregress(x_values, precision_values)
    y_values_linear = slope * x_values + intercept

    # Set the figure size and adjust spacing
    plt.figure(figsize=(12, 6))  # Adjust the width and height as needed

    # Plot the precision values, quadratic trendline, and linear trendline
    plt.plot(x_values, precision_values, 'bo-', label='Precision Values', markersize=4)
    plt.plot(x_values, y_values_quadratic, 'r-', label='Quadratic Trendline')
    plt.plot(x_values, y_values_linear, 'g-', label='Linear Trendline')

    plt.xlabel('Pairs')
    plt.ylabel('Precision score ')
    plt.title('Iteration 4 - Architectural Issues All Emails - Precision Trendlines')

    plt.xticks(x_values[::2])  # Adjust the step size as needed
    plt.legend()
    # Set y-axis limits
    plt.ylim(0.0, 1.0)
    plt.show()


if __name__ == '__main__':
    main_function()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
