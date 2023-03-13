# https://matplotlib.org/stable/gallery/spines/multiple_yaxis_with_spines.html#sphx-glr-gallery-spines-multiple-yaxis-with-spines-py

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 3))
# fig.subplots_adjust(right=0.75)

# double y-axis
twin = ax.twinx()

(f1,) = ax.plot([0, 1, 2], [0, 1, 2], "C0", label="Density")
(f2,) = twin.plot([0, 1, 2], [0, 3, 2], "C1", label="Temperature")

ax.set(xlim=(0, 2), ylim=(0, 2), xlabel="Distance", ylabel="Density")
twin.set(ylim=(0, 4), ylabel="Temperature")

ax.legend(handles=[f1, f2])

plt.show()
