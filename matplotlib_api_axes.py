import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

######################################
# Examples from Matplotlib API
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot
######################################
def example_x_1d_array_and_y_2d_array():
    x = [1, 2, 3]  # 1x3
    y = np.array([[1, 2], [3, 4], [5, 6]])  # 3x2
    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize=(5, 3.5))
    ax1.plot(y, "o-")  # by default x is range(len(y)) starting by 1
    ax2.plot(x, y)

    # equivalent to
    for col in range(y.shape[1]):
        ax3.plot(x, y[:, col])

    # equivalent to
    y1 = [1, 3, 5]
    y2 = [2, 4, 6]
    ax4.plot(x, y1, x, y2)

    df = pd.DataFrame({"x": [1, 2, 3], "y1": [1, 3, 5], "y2": [2, 4, 6]})
    ax5.plot("x", "y1", "", data=df)
    ax5.plot("x", "y2", "", data=df)
    plt.show()


def example_x_and_y_2d_array():
    # example: when x and y are 2D arrays
    x = np.array([[1, 2], [3, 4], [5, 6]])  # 3x2
    y = np.array([[1, 4], [3, 6], [5, 8]])  # 3x2
    fig, ax = plt.subplots(figsize=(5, 3.5))
    ax.plot(x, y)
    plt.show()


if __name__ == "__main__":
    example_x_1d_array_and_y_2d_array()
    # example_x_and_y_2d_array()
