import numpy as np
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=40)  # run each time to get same random values
data1, data2, data3 = rng.standard_normal((3, 150))
# data1, data2, data3 = np.random.randn(3, 5)

fig, ax = plt.subplots(figsize=(5, 2.5))
pc = ax.scatter(data1, data2, c=data3)  # PathCollection object
fig.colorbar(pc, ax=ax)  # , extend="both")
plt.show()
