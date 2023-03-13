import numpy as np
import matplotlib.pyplot as plt

x, y = np.random.random((2, 50))
fig, ax = plt.subplots()

twin = ax.twinx()
ax.scatter(x, y, c="b", label="ax")
# ax2.plot(np.sort(x), np.arange(x.size), c="r", linestyle=" ", marker=".")
twin.scatter(np.sort(x), np.arange(x.size), c="r", label="twin")

ax.legend(loc="upper left")
twin.legend(loc="upper right")

plt.show()
