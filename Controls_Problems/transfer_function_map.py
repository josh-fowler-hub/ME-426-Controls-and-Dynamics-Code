# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:52:11 2018

@author: jfowl
"""
from numba import jit
import numpy as np
import control as ctl
import matplotlib.pyplot as plt
from matplotlib import colors
import datetime as dt


data = np.genfromtxt('ME_426_Project_3.csv', delimiter=',', skip_header=1)
ex_angle = data[:, 0]
ex_time = data[:, 1]
ex_angle = [-(30/107)*(a - 458) for a in ex_angle]

length = 2
gravity = 9.81
mass = 0.356
dmp = 0.315
initial_angle = 30
theta_d_init = 0
t_start = min(ex_time)
t_final = max(ex_time)

init_ang_rad = (initial_angle/180)*np.pi
init_cond = [init_ang_rad, 0]
tvec = np.linspace(t_start, t_final, 10000)
sys = ctl.tf([init_ang_rad, theta_d_init + (dmp/(mass*length))*init_ang_rad],
             [1, dmp/mass, gravity/length])

print(sys)


def save_image(fig, time):
    now = dt.datetime.now()
    tstmp = now.timestamp()
    filename = "system_image_{}_{}".format(int(tstmp), int(time))
    fig.savefig(filename, bbox_inches='tight')


@jit
def system(z, freq, maxiter):
    c = freq
    for n in range(maxiter):
        az = abs(z)
        if az > c:
            return abs(z)
        z = z**n + c
    return 0


@jit
def sys_set(sys, freq, xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = system(sys(r1[i] + 1j*r2[j]), freq, max_iter)
    return (r1, r2, n3)


def sys_image(sys, freq, xmin, xmax, ymin, ymax, width=11, height=7,
              maxiter=1, cmap='jet', axis='on'):
    timer = dt.datetime.now()
    time = timer.timestamp()
    dpi = 384
    img_width = dpi * width
    img_height = dpi * height
    x, y, z = sys_set(sys, freq, xmin, xmax, ymin, ymax, img_width, img_height,
                      maxiter)
    fig, ax = plt.subplots(figsize=(width, height), dpi=216)
    ticks = np.arange(0, img_width, 3*dpi)
    x_ticks = xmin + (xmax - xmin)*ticks/img_width
    plt.xticks(ticks, x_ticks)
    y_ticks = ymin + (ymax-ymin)*ticks/img_width
    plt.yticks(ticks, y_ticks)
    plt.title('System @ {} Hz Rendered in {}'.format(freq, cmap))
    plt.axis(axis)
    ax.imshow(z.T, cmap=cmap, origin='lower')
    save_image(fig, time)


sys_image(sys, 100, -22/7, 22/7, -2, 2)
