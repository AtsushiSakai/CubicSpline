#! /usr/bin/python
# -*- coding: utf-8 -*-
u"""
Cubic Spline library

author Atsushi Sakai

license: MIT
"""
import math
import numpy as np


class Spline:
    u"""
    Cubic Spline class

    usage:
        spline=Spline(x,y)
        rx=np.arange(0,4,0.1)
        ry=[spline.calc(i) for i in rx]
    """

    def __init__(self, x, y):
        self.b, self.c, self.d, self.w = [], [], [], []

        self.x = x
        self.y = y

        self.nx = len(x)  # dimension of x
        h = np.diff(x)

        # calc coefficient c
        self.a = [iy for iy in y]

        # calc coefficient c
        A = self.__calc__A(h)
        B = self.__calc__B(h)
        self.c = np.linalg.solve(A, B)
        #  print(self.c1)

        # calc spline coefficient b and d
        for i in range(self.nx - 1):
            self.d.append((self.c[i + 1] - self.c[i]) / (3.0 * h[i]))
            tb = (self.a[i + 1] - self.a[i]) / h[i] - h[i] * (self.c[i + 1] + 2.0 * self.c[i]) / 3.0
            self.b.append(tb)

    def calc(self, t):
        u"""
        Calc position

        if t is outside of the input x, return None

        """

        if t < self.x[0]:
            return None
        elif t > self.x[-1]:
            return None

        i = self.__search_index(t)
        dx = t - self.x[i]
        result = self.a[i] + self.b[i] * dx + self.c[i] * dx ** 2.0 + self.d[i] * dx ** 3.0

        return result

    def __search_index(self, x):
        u"""
        search data segment index
        """

        for i in range(self.nx):
            if self.x[i] - x > 0:
                return i - 1

    def __calc__A(self, h):
        u"""
        calc matrix A for spline coefficient c
        """
        A = np.zeros((self.nx, self.nx))
        A[0, 0] = 1.0
        for i in range(self.nx - 1):
            if i is not self.nx - 2:
                A[i + 1, i + 1] = 2.0 * (h[i] + h[i + 1])
            A[i + 1, i] = h[i]
            A[i, i + 1] = h[i]

        A[0, 1] = 0.0
        A[self.nx - 1, self.nx - 2] = 0.0
        A[self.nx - 1, self.nx - 1] = 1.0
        #  print(A)
        return A

    def __calc__B(self, h):
        u"""
        calc matrix B for spline coefficient c
        """
        B = np.zeros(self.nx)
        for i in range(self.nx - 2):
            B[i + 1] = 3.0 * (self.a[i + 2] - self.a[i + 1]) / h[i + 1] - 3.0 * (self.a[i + 1] - self.a[i]) / h[i]
        #  print(B)
        return B

    def calcd(self, t):
        u"""
        Calc first derivative
        """

        j = int(math.floor(t))
        if(j < 0):
            j = 0
        elif(j >= len(self.a)):
            j = len(self.a) - 1

        dt = t - j
        result = self.b[j] + 2.0 * self.c[j] * dt + 3.0 * self.d[j] * dt * dt
        return result

    def calcdd(self, t):
        u"""
        Calc second derivative
        """
        j = int(math.floor(t))
        if(j < 0):
            j = 0
        elif(j >= len(self.a)):
            j = len(self.a) - 1

        dt = t - j
        result = 2.0 * self.c[j] + 6.0 * self.d[j] * dt
        return result


def calc_xy_curvature(s, sx, sy):
    u"""
    Calc curvature x-y spline curve
    """
    dx = sx.calcd(s)
    ddx = sx.calcdd(s)
    dy = sy.calcd(s)
    ddy = sy.calcdd(s)
    k = (ddy * dx - ddx * dy) / (dx ** 2 + dy ** 2)
    return k


def calc_yaw(s, sx, sy):
    u"""
    calc yaw of x-y spline curve
    """
    dx = sx.calcd(s)
    dy = sy.calcd(s)
    yaw = math.atan2(dy, dx)
    return yaw


def test1():
    import matplotlib.pyplot as plt
    # input
    #  x = [-1.0, 0.0, 1.0, 2.0, 3.0]
    #  x = [-0.5, 0.0, 0.5, 1.0, 1.5]
    x = [-2.5, 0.0, 2.5, 5.0, 7.5]
    #  y = [3.2, 2.7, 6, 5, 6.5]
    y = [0.7, -6, 5, 6.5, 0.0]

    # 3d spline interporation
    spline = Spline(x, y)
    rx = np.arange(-2.0, 4, 0.01)
    ry = [spline.calc(i) for i in rx]

    plt.plot(x, y, "xb")
    plt.plot(rx, ry, "-r")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


if __name__ == '__main__':
    test1()
