# Check "Additional Axis objects" in https://matplotlib.org/stable/tutorials/introductory/quick_start.html#axis-scales-and-ticks
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)


fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(5, 2), layout="constrained")
# fig, ax1 = plt.subplots(figsize=(5, 2), layout="constrained")
(l1,) = ax1.plot(t, s)
ax2 = ax1.twinx()
(l2,) = ax2.plot(t, range(len(t)), "C1")
ax1.set_xlabel("Angle [rad]")
ax1.set_ylabel("Sine")
ax2.set_ylabel("Straight")
ax2.legend([l1, l2], ["Sine (left)", "Straight (right)"])

ax3.plot(t, s)
ax3.set_xlabel("Angle [rad]")
ax3.set_ylabel("Sine")
ax4 = ax3.secondary_xaxis("top", functions=(np.rad2deg, np.deg2rad))
ax4.set_xlabel("Angle [°]")


plt.show()
