import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

total_points = 100000000
def does_hit(x,y):
    if (x**2+y**2 <=1):
        return True
    else:
        return False

def calculate_area(points_hit, total_points, area):
    return points_hit / total_points * area

def random_point():
    return np.random.uniform(-1,1)

hits = 0
x_hits = []
y_hits = []
x_miss = []
y_miss = []

for itteration in tqdm(range(1, total_points), desc=f"Throwing the rocks", leave=False):
    x = random_point()
    y = random_point()
    if does_hit(x, y):
        hits += 1
        x_hits.append(x)
        y_hits.append(y)
    else:
        x_miss.append(x)
        y_miss.append(y)

pi = calculate_area(hits,total_points,2*2)/1**2

plt.figure(figsize=(8, 8))
plt.scatter(x_hits, y_hits, color='blue', s=1, label='Inside Circle')
plt.scatter(x_miss, y_miss, color='red', s=1, label='Outside Circle')
plt.title(f"Monte Carlo Simulation with n={total_points}\nEstimated π ≈ {pi}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper right")
plt.axis('equal')
plt.show()