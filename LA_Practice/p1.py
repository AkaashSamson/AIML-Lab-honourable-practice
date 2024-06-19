import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 40, 1000)
dr = 2.5*t
ds = 3*(t-5)

fig, ax = plt.subplots()
plt.title("Robber caught")
plt.xlabel("time")
plt.ylabel("distance")
ax.plot(t, dr, label="Robber", c="red")
ax.plot(t, ds, label="Suspect", c="blue")
ax.legend()
plt.show()