import matplotlib.pyplot as plt
import numpy as np

data1, data2, data3 = np.random.randn(3, 150)
fig, ax = plt.subplots()

# colormaps: https://matplotlib.org/stable/tutorials/colors/colormaps.html
pc = ax.scatter(data1, data2, c=data3, cmap="plasma")  # cmap="viridis" by default

fig.colorbar(pc, ax=ax)  # , extend="both")
ax.set_title("Scatter plot with color bar")

plt.show()
