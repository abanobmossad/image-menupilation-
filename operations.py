import matplotlib.pyplot as plt
import numpy as np
from math import *

X = 0.1
Y = 0.1
width = 0.2
height = 0.4



def show_shape():
    fig = plt.figure("Object Operations")

    plt.ylim([-5, 6])
    plt.xlim([-5, 6])
    plt.show()


def translate(t1=3, t2=3,show=True):
    fig = plt.figure("Object Operations")
    if show:
        poly = plt.Polygon([(0, 0), (0, 2), (1, 1),
                            (2, 2), (2, 0), (1, 0.8), (0, 0)])
        x = poly.get_xy()
        ax = fig.add_subplot(111)
        ax.plot(x[:, 0], x[:, 1], color='#6699cc', alpha=0.5,
                linewidth=3, solid_capstyle='round', zorder=2)

    poly = plt.Polygon([(0, 0), (0, 2), (1, 1),
                        (2, 2), (2, 0), (1, 0.8), (0, 0)])
    x = poly.get_xy()
    ax = fig.add_subplot(111)
    ax.plot(x[:, 0] + t1, x[:, 1] + t2, color='#000000', alpha=0.7,
            linewidth=3, solid_capstyle='round', zorder=2)
    ax.set_title('Translate ')
    plt.show()


def rotate(deg=45,show=True):
    fig = plt.figure("Object Operations")
    if show:
        poly = plt.Polygon([(0, 0), (0, 2), (1, 1),
                            (2, 2), (2, 0), (1, 0.8), (0, 0)])
        x = poly.get_xy()
        ax = fig.add_subplot(111)
        ax.plot(x[:, 0], x[:, 1], color='#6699cc', alpha=0.5,
                linewidth=3, solid_capstyle='round', zorder=2)

    poly = plt.Polygon([(0, 0), (0, 2), (1, 1),
                        (2, 2), (2, 0), (1, 0.8), (0, 0)])
    shape = poly.get_xy()

    ox, oy = (0.9,0.9)


    xx = []
    yy = []
    for i in range(7):
        px, py = shape[i]
        qx = ox + cos(deg) * (px - ox) - sin(deg) * (py - oy)
        qy = oy + sin(deg) * (px - ox) + cos(deg) * (py - oy)
        xx.append(qx)
        yy.append(qy)

    ax = fig.add_subplot(111)
    ax.plot(xx, yy, color='#000000', alpha=0.7,
            linewidth=3, solid_capstyle='round', zorder=2)
    ax.set_title('Rotate ')

    plt.show()


def scaling(s=20,show=True):

    fig = plt.figure("Object Operations")

    if show:
        poly = plt.Polygon([(0, 0), (0, 2), (1, 1),
                            (2, 2), (2, 0), (1, 0.8), (0, 0)])
        x = poly.get_xy()
        ax = fig.add_subplot(111)
        ax.plot(x[:, 0], x[:, 1], color='#6699cc', alpha=0.5,
                linewidth=3, solid_capstyle='round', zorder=2)
    poly = plt.Polygon([(0, 0), (0, 2), (1, 1),
                        (2, 2), (2, 0), (1, 0.8), (0, 0)])
    x = poly.get_xy()
    ax = fig.add_subplot(111)
    ax.plot(x[:, 0] * (s/10), x[:, 1] * (s/10), color='#000000', alpha=0.7,
            linewidth=3, solid_capstyle='round', zorder=2)
    ax.set_title('Scaling ')

    plt.show()

# scaling(20)

