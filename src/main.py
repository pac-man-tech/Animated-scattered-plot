import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

num_points = 80
frames = 100
interval = 80
trail_length = 8


x = np.random.rand(num_points) *10
y = np.random.rand(num_points)*10
colors = np.random.rand(num_points)
sizes = np.random.rand(num_points)* 2000

fig, axes = plt.subplots()
scatter_plot = axes.scatter( x, y, c= colors, s= sizes,alpha = 0.7, cmap ='tab10') #viridis, plasma, coolwarm
axes.set_xlim(0, 10)
axes.set_ylim(0, 10)
axes.set_title("Animated Scatter Plot with Trails")

lines =[axes.plot([],[], lw=1, alpha = 0.4, color= 'gray')[0] for _ in range (num_points)]
x_history =[x.copy()]
y_history = [y.copy()]

def animate(frame_num):
    global x, y
    x += np.random.randn(num_points) * 0.1
    y += np.random.randn(num_points) * 0.1
    dynamic_size = np.random.rand(num_points) *50
    new_colors = np.random.rand(num_points)

    x_history.append(x.copy())
    y_history.append(y.copy())
    if len(x_history) > trail_length:
        x_history.pop(0)
        y_history.pop(0)

    scatter_plot.set_offsets(np.c_[x, y])
    scatter_plot.set_sizes(dynamic_size)
    scatter_plot.set_array(new_colors)

    for i, line in enumerate(lines):
        trail_x = [history[i] for history in x_history]
        trail_y = [history[i] for history in y_history]
        line.set_data(trail_x, trail_y)
    
    return scatter_plot, *lines

animated_plot = animation.FuncAnimation(fig,animate,frames= frames, interval= interval, blit= True)
plt.show()