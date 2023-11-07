from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

# Tehtävä 1
radiaanit = np.radians([30, 45, 60, 90, 120, 150, 180, 270])

# Tehtävä 2
fig = plt.figure(figsize=(6.4*3, 4.8))
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')
ax.set_xlim([-3*np.pi, 3*np.pi])

# Piirrä käyrät
for i, radiaani in enumerate(radiaanit):
    x = np.cos(radiaani)
    y = np.sin(radiaani)
    plt.plot([0, x], [0, y], color=f'C{i}', linestyle='--', label=f'${fr(radiaanit[i]/np.pi)}\pi$')

# Tehtävä 3
ax.set_xticks([-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi])
ax.set_xticklabels(['$-3\pi$', '$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$', '$3\pi$'])

ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticklabels(['$-1$', '$-0.5$', '0', '0.5', '1'])

# Selite
plt.legend(loc='upper left')

plt.show()
