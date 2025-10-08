# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 14:57:28 2018

@author: jfowl
"""

import control as ctl
import numpy as np
import scipy.signal as sig

mi = 300  # initial weight of rocket in kg
Mars_m = 6.39e23  # mass of Mars in kg
G = 6.67408e-11  # Gravitational Constant SI units
Isp = 291  # Specific Impulse of rocket in seconds
g = 9.81  # Gravitational Acceleration on Earth m/s^2
tint = 0  # initial time
op_time = 43  # Operational Time of rocket in seconds
tot_time = 43  # Total Simulation Time in seconds
nt = 1000  # number of time steps
tvec = np.linspace(tint, tot_time, nt)  # time vector
dt = tvec[1]  # length of time step
T = 15000  # Thrust in Newtons
b = 3  # length of rocket in meters
d = 0.5  # diameter of rocket in meters
betai = 0  # intial thrust angle
thetai = 90  # intital pitch angle
d_Mars = 6779000  # diameter of Mars in meters
r_Mars = d_Mars/2  # radius of Mars in meters
start_pos = np.asarray([[0], [r_Mars]])  # starting position of rocket,
# surface of Mars
start_vel = np.asarray([[0], [0]])  # starting velocity in m/s
start_accel = np.asarray([[0], [0]])  # starting accelleration in m/s^2
escape_vel = 5.03e3  # escape velocity of Mars in m/s
start_theta = 90*(np.pi/180)
thetac = -0*(np.pi/180)
thetadc = 0
low_cut_off = -45*(np.pi/180)
high_cut_off = 45*(np.pi/180)
rollover = 0.1

N = [mi*Isp*g, -T]
D = [Isp*g, 0, 0]

sys = ctl.tf(N, D)
zpk = sig.tf2zpk(N, D)

tout, xout = ctl.step_response(sys, tvec)

