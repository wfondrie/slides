import numpy as np
import matplotlib.pyplot as plt
from wispy import theme

pal = theme.talk(dark=True)

np.random.seed(42)
plt.figure()
plt.plot(np.random.randn(10))
plt.plot(np.random.randn(10) + np.arange(10))
plt.savefig("img/theme.png", transparent=True, dpi=300)

pal = theme.paper()

np.random.seed(42)
plt.figure()
plt.plot(np.random.randn(10))
plt.plot(np.random.randn(10) + np.arange(10))
plt.savefig("img/theme_paper.png", transparent=False, dpi=300)
