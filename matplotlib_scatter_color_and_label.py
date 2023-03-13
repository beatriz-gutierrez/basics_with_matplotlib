import numpy as np
import matplotlib.pyplot as plt

data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets

fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
ax.plot(np.arange(len(data1)), data1, label="data1")
ax.plot(np.arange(len(data2)), data2, label="data2")
ax.plot(np.arange(len(data3)), data3, "d", label="data3")

# ax.legend()
fig.legend(loc="outside upper right")
plt.show()
