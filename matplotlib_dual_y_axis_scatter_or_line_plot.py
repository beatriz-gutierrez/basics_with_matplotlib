import numpy as np
import matplotlib.pyplot as plt

x, y = np.random.random((2, 50))
fig, (ax1, ax2) = plt.subplots(1, 2)

#  2 scatter plots
ax11 = ax1.twinx()
ax1.scatter(x, y, c="b", label="ax11")
# ax2.plot(np.sort(x), np.arange(x.size), c="r", linestyle=" ", marker=".")
ax11.scatter(np.sort(x), np.arange(x.size), c="r", label="a")

# 1 scatter plot and 1 line plot
ax22 = ax2.twinx()
ax2.scatter(x, y, c="b")
ax22.plot(np.sort(x), np.arange(x.size), c="r", linestyle=" ", marker=".")

ax1.legend()

plt.show()
