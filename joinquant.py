# -*- coding: UTF-8 -*-  
import numpy as np
from pandas import DataFrame,Series
import pandas as pd

aa=np.array([[1,0,6],[1,7,0],[2,4,0],[2,3,1]])

print (aa)

import random 
position = 0
walk = [position]
steps = 1000
for i in xrange (steps):
	step = 1 if random.randint(0,1) else -1
	position + step
	walk.append(position)

nsteps = 1000
draws = np.random.randint(0,2,size=nsteps)
steps = np.where(draws>0,1,-1)
walk = steps.cumsum()
print walk.min()
print walk.max()

print (np.abs(walk)>10).argmax()


obj = Series([4,7,-5,3])
print obj
import numpy as np
from scipy.linalg import solve
# a = np.array([[3, 1, -2], [1, -1, 4], [2, 0, 3]])
# b = np.array([5, -2, 2.5])
# x = solve(a, b)
# print x

a = np.array([[20, 15], [25, 15]])
b = np.array([5875000,6940000])
x = solve(a, b)
print x


import matplotlib.pyplot as plt

X = np.arange(-5.0, 5.0, 0.1)
Y = np.arange(-5.0, 5.0, 0.1)

x, y = np.meshgrid(X, Y)
f = 17 * x ** 2 - 16 * np.abs(x) * y + 17 * y ** 2 - 225

fig = plt.figure()
cs = plt.contour(x, y, f, 0, colors = 'r')
plt.show()

##pi,默认密码是raspberry,