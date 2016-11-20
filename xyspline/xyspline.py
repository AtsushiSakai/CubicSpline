#! /usr/bin/python 
# -*- coding: utf-8 -*- 
u""" 
xy Spline sample

author Atsushi Sakai
license: MIT
"""

import pandas as pd
from PyCubicSpline import PyCubicSpline
import numpy as np
import matplotlib.pyplot as plt
import math

def CalcXYCurvature(s,sx,sy):
    dx  = sx.Calcd(s)
    ddx = sx.Calcdd(s)
    dy  = sy.Calcd(s)
    ddy = sy.Calcdd(s)
    k   = (ddy*dx-ddx*dy)/(dx**2+dy**2)
    return k

def Test():
    print("test")

    fname="course.csv"
    data=pd.read_csv(fname)
    x   = list(data["x"])
    y   = list(data["y"])
    yaw = list(data["yaw"])
    kp   = list(data["curvature"])
    ds   = list(data["ds"])

    d=0.1
    s=np.arange(0,sum(ds),d)

    sx=PyCubicSpline(x)
    sy=PyCubicSpline(y)

    xs,ys=[],[]

    for ts in s:
        xs.append(sx.Calc(ts))
        ys.append(sy.Calc(ts))

    flg,ax=plt.subplots(1)
    plt.plot(xs,ys,".r",label="spline interporation")
    plt.plot(x,y,"xb",label="input points")
    plt.legend()
    plt.axis("equal")
    plt.grid(True)

    k=[]
    for ts in s:
        k.append(CalcXYCurvature(ts,sx,sy))

    flg,ax=plt.subplots(1)
    plt.plot(kp,"-b",label="True curvature")
    plt.plot(s,k,"-r",label="Calc with spline")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    Test()
