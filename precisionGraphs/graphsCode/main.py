import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress


def main_function():
    precision_values = [
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        0.909090909, 0.916666667, 0.923076923, 0.928571429, 0.866666667, 0.875, 0.882352941, 0.888888889, 0.894736842,
        0.9,
        0.904761905, 0.909090909, 0.913043478, 0.916666667, 0.92, 0.923076923, 0.925925926, 0.928571429, 0.896551724,
        0.9,
        0.903225806, 0.90625, 0.878787879, 0.882352941, 0.885714286, 0.861111111, 0.864864865, 0.868421053, 0.871794872,
        0.85,
        0.829268293, 0.833333333, 0.837209302, 0.840909091, 0.844444444, 0.847826087, 0.829787234, 0.833333333,
        0.836734694, 0.84,
        0.843137255, 0.846153846, 0.849056604, 0.851851852, 0.854545455, 0.857142857, 0.842105263, 0.844827586,
        0.830508475, 0.816666667,
        0.819672131, 0.806451613, 0.793650794, 0.78125, 0.784615385, 0.787878788, 0.776119403, 0.764705882, 0.753623188,
        0.742857143,
        0.732394366, 0.722222222, 0.726027397, 0.716216216, 0.72, 0.723684211, 0.714285714, 0.717948718, 0.708860759,
        0.7,
        0.703703704, 0.707317073, 0.710843373, 0.702380952, 0.694117647, 0.686046512, 0.67816092, 0.681818182,
        0.674157303, 0.666666667,
        0.659340659, 0.652173913, 0.64516129, 0.638297872, 0.642105263, 0.635416667, 0.628865979, 0.62244898,
        0.626262626, 0.62
    ]

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
    plt.title('Iteration 4 - Architectural Issue All Emails NO DUPLICATES - Precision Trendlines')

    plt.xticks(x_values[::2])  # Adjust the step size as needed
    plt.legend()
    # Set y-axis limits
    plt.ylim(0.0, 1.0)
    plt.show()


if __name__ == '__main__':
    main_function()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
