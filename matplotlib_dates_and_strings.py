import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.dates as mpl_dates

fig, ax = plt.subplots(figsize=(5, 2.7), layout="constrained")
dates = np.arange(
    np.datetime64("2021-11-15"), np.datetime64("2021-12-25"), np.timedelta64(1, "h")
)
data = np.cumsum(np.random.randn(len(dates)))
ax.plot(dates, data)

cdf = mpl_dates.ConciseDateFormatter(ax.xaxis.get_major_locator())
ax.xaxis.set_major_formatter(cdf)
plt.show()
