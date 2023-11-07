import numpy as np

rad1 = 2.493
rad2 = 0.911

deg1 = 137.7
deg2 = 62.3

degrees = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

print(np.degrees(rad1))
print(np.degrees(rad2))

print(np.radians(deg1))
print(np.radians(deg2))

for i in degrees:
    print(np.radians(i))

