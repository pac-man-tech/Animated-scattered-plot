
#a debug version on the terminal to understand how the animate works
import numpy as np


num_points = 5

x,y =np.random.rand(2, num_points) *10
print("Initial position: ")
for i in range(num_points):
    print(f"Dot{i+1}: x= {x[i]:.2f}, y = {y[i]:.2f}")

for frame in range(1,4):
    new_X = x + np.random.randn(num_points) *0.1
    new_y = y + np.random.randn(num_points) *0.1

print(f"\n Movement {frame}:")
for i in range(num_points):
    print(f"Dot {i+1} moved to: X = {new_X[i]:.2f}, Y= {new_y[i]:.2f}")

x, y = new_X, new_y
