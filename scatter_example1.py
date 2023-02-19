import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd':  np.abs(np.random.randn(50)) * 100,
    }
data['b'] = data['a'] + 10 * np.random.randn(50)

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
plt.show()
fig.savefig("scatter_example1")