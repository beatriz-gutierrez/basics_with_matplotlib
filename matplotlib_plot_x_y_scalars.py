import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


df = pd.DataFrame(
    {
        "x": ["group_A", "group_B", "group_C", "group_D"],
        "y": [10, 80, 100, 250],
        "z": ["type1", "type2", "type2", "type1"],
    }
)


def example_x_or_y_as_scalars(data):
    # example: when x or y are scalars
    x = 1
    y = 2
    fig, ax1 = plt.subplots(figsize=(5, 3.5))
    # ax1.plot(x, y, "o", data)
    # ax1.plot("x", "y", "o", data=data)
    ax1.plot(x, y, "o", data=data)
    plt.show()


if __name__ == "__main__":
    example_x_or_y_as_scalars(data=df)
