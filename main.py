# z_0 = 0
# z_(n+1) = z^2 + c
# point in mandelbrot set if abs(z) <= 2; 
# 
# at each iteration, value for each point within frame
import cmath
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

def gen(c, z, n=1): # a + b j
  for _ in range(n):
    if abs(z) <= 2:
      z = z ** 2 + c
  return z

# arr = np.zeros((n_pixels, n_pixels))
# def init_array(n_pixels):
#   return np.zeros((n_pixels, n_pixels))
#   c = complex((step * i1), (step * i2))
#   arr[r][c]
#   for x in range(n_pixels):
#     for y in range(n_pixels):
#       arr[x][y] = gen()

# gen(complex(0,1), 0, 10)
N_PIXELS = 500
TIME_STEPS = 1
LOWER, UPPER = -2, 2
STEP = (UPPER - LOWER) / N_PIXELS
TICK_RANGE = list(np.arange(0, N_PIXELS+1, step=1 / STEP))
LABEL_RANGE = list(np.arange(LOWER, UPPER+1))
mArr = np.zeros((N_PIXELS, N_PIXELS))
# c = 0 + 0 j for x, y = (0, 0)

def mandelbrot(i):
  plt.cla()
  plt.xticks(TICK_RANGE, LABEL_RANGE)
  plt.yticks(TICK_RANGE, LABEL_RANGE)
  plt.gca().invert_yaxis()
  for (x, y), z in np.ndenumerate(mArr):
    c = complex(STEP * y + LOWER, STEP * x + LOWER)
    mArr[x][y] = abs(gen(c, z, n=(i+1)*TIME_STEPS))
    print(f"{(i+1)} Progress: {N_PIXELS*x + y}", end="\r")
  # img = plt.imshow(mArr)
  return plt.imshow(mArr),

# fig = plt.figure(figsize=(N_PIXELS, N_PIXELS))
# plt.xticks(TICK_RANGE, LABEL_RANGE)
# plt.yticks(TICK_RANGE, LABEL_RANGE)
# plt.gca().invert_yaxis()
fig = plt.figure()


anim = animation.FuncAnimation(fig, mandelbrot, frames=30, interval = 200, blit=True)
# plt.show()

anim.save("jankelbrot.gif")

# for animation arraygen from n = 1 to TIME_STEPS
# THIS WORKS DONT DELETE
# plt.title("")
# plt.imshow(mArr)
# plt.xticks(TICK_RANGE, LABEL_RANGE)
# plt.yticks(TICK_RANGE, LABEL_RANGE)
# plt.gca().invert_yaxis()
# plt.savefig('m.png')
# plt.show()
