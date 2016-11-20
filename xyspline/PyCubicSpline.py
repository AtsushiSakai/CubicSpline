#! /usr/bin/python 
# -*- coding: utf-8 -*- 
u""" 
Cubic Spline library

author Atsushi Sakai
license: MIT
"""
import math
import numpy as np

class PyCubicSpline:
    u"""
    Cubic Spline class

    usage:
        spline=PyCubicSpline(y)
        rx=np.arange(0,4,0.1)
        ry=[spline.Calc(i) for i in rx]
    """

    def __init__(self,y):
        self.a,self.b,self.c,self.d,self.w=[],[],[],[],[]

        self.a=[iy for iy in y]

        for i in range(len(self.a)):
            if i==0:
                self.c.append(0)
            elif i==(len(self.a)-1):
                self.c.append(0)
            else:
                self.c.append(3.0*(self.a[i-1]-2.0*self.a[i]+self.a[i+1]))

        for i in range(len(self.a)):
            if i==0:
                self.w.append(0)
            elif i==(len(self.a)-1):
                pass
            else:
                tmp=4.0-self.w[i-1]
                self.c[i]=(self.c[i]-self.c[i-1])/tmp
                self.w.append(1.0/tmp)

        i=len(self.a)-1
        while(i>0):
            i-=1
            self.c[i]=self.c[i]-self.c[i+1]*self.w[i]

        for i in range(len(self.a)):
            if i==(len(self.a)-1):
                self.b.append(0)
                self.d.append(0)
            else:
                self.d.append((self.c[i+1]-self.c[i])/3.0)
                self.b.append(self.a[i+1]-self.a[i]-self.c[i]-self.d[i])

        #  print(self.a)
        #  print(self.b)
        #  print(self.c)
        #  print(self.d)


    def Calc(self,t):
        u"""
        Calc position
        """
 
        j=int(math.floor(t))
        if(j<0):
            j=0
        elif(j>=len(self.a)):
            j=len(self.a)-1

        dt=t-j
        result=self.a[j]+(self.b[j]+(self.c[j]+self.d[j]*dt)*dt)*dt
        return result

    def Calcd(self,t):
        u"""
        Calc first derivative
        """
 
        j=int(math.floor(t))
        if(j<0):
            j=0
        elif(j>=len(self.a)):
            j=len(self.a)-1

        dt=t-j
        result=self.b[j]+2.0*self.c[j]*dt+3.0*self.d[j]*dt*dt
        return result

    def Calcdd(self,t):
        u"""
        Calc second derivative
        """
        j=int(math.floor(t))
        if(j<0):
            j=0
        elif(j>=len(self.a)):
            j=len(self.a)-1

        dt=t-j
        result=2.0*self.c[j]+6.0*self.d[j]*dt
        return result


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    #input
    x=[0,1,2,3]
    y=[2.7,6,5,6.5]

    # 3d spline interporation
    spline=PyCubicSpline(y)
    rx=np.arange(0,4,0.1)
    ry=[spline.Calc(i) for i in rx]

    plt.plot(x,y,"xb")
    plt.plot(rx,ry,"-r")
    plt.grid(True)
    plt.axis("equal")
    plt.show()

 
