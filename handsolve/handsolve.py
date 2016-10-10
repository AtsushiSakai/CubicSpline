#! /usr/bin/python 
# -*- coding: utf-8 -*- 
u""" 
author Atsushi Sakai
"""
import matplotlib.pyplot as plt
import numpy as np

def CubicFunc(x,p):
    y=p[0]*(x**3)+p[1]*(x**2)+p[2]*x+p[3]
    return y

#input, output
x=[1,2,3,4]
y=[2.7,6,5,6.5]

A=np.array([[1,1,1,1, 0,0,0,0,0,0,0,0],
            [8,4,2,1, 0,0,0,0,0,0,0,0],
            [0,0,0,0, 8,4,2,1,0,0,0,0],
            [0,0,0,0,27,9,3,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,27,9,3,1],
            [0,0,0,0,0,0,0,0,64,16,4,1],
            [12,4,1,0,-12,-4,-1,0,0,0,0,0],
            [0,0,0,0,27,6,1,0,-27,-6,-1,0],
            [12,2,0,0,-12,-2,0,0,0,0,0,0],
            [0,0,0,0,18,2,0,0,-18,-2,0,0],
            [6,2,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,24,2,0,0],
            ])

b=np.array([2.7,6,6,5,5,6.5,0,0,0,0,0,0])

xs=np.linalg.solve(A,b)

fx,fy=[],[]
for i in range(3):
    xt=np.arange(x[i],x[i+1]+0.1,0.1)
    p=xs[4*i:4*(i+1)]
    yt=[CubicFunc(xi,p) for xi in xt]
    fx.extend(xt)
    fy.extend(yt)

plt.plot(x,y,"xb")
plt.plot(fx,fy,"-r")
plt.grid(True)
plt.axis("equal")
plt.show()

