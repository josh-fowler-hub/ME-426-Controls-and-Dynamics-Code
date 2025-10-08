# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 11:45:38 2018

@author: jfowl
"""
import numpy as np
import scipy.integrate as scI
import matplotlib.pyplot as plt
import control as ctl

data = np.genfromtxt('ME_426_Project_3.csv', delimiter=',', skip_header=1)
ex_angle = data[:, 0]
ex_time = data[:, 1]
ex_angle = [-(30/107)*(a - 458) for a in ex_angle]

length = 0.8
gravity = 9.81
mass = 0.356
dmp = 0.33
initial_angle = 30
theta_d_init = 0
t_start = min(ex_time)
t_final = max(ex_time)


init_ang_rad = (initial_angle/180)*np.pi
init_cond = [init_ang_rad, 0]
tvec = np.linspace(t_start, t_final, 10000)
sys = ctl.tf([init_ang_rad, theta_d_init + (dmp/(mass*length))*init_ang_rad],
             [1, dmp/mass, gravity/length])
tout, theta_out = ctl.impulse_response(sys, ex_time)
theta_new = [t*(180/np.pi) for t in theta_out]


def non_linear_pend(sys, tvec):
    theta = sys[0]
    theta_d = sys[1]
    theta_dd = -(dmp/mass)*theta_d - (gravity/length)*np.sin(theta)
    return [theta_d, theta_dd]


solution = scI.odeint(non_linear_pend, init_cond, ex_time)

solution_theta = [s*(180/np.pi) for s in solution[:, 0]]
solution_theta_d = [s*(180/np.pi) for s in solution[:, 1]]

plt.figure()
plt.plot(ex_time, ex_angle, 'b', label='Experimental Data', linewidth=3)
plt.plot(tout, theta_new, 'r',
         label='Inverse Laplace Solution w/ Small Angle Approx', linewidth=2)
plt.plot(ex_time, solution_theta, '--k',
         label='Numerical Solution w/o Small Angle Approx', linewidth=2)
plt.title('Angle vs. Time: Damped Pendulum')
plt.xlabel('Time (Sec)')
plt.ylabel('Angle (Deg)')
plt.xlim([min(ex_time), max(ex_time)])
plt.ylim([min(solution_theta), max(solution_theta)])
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(ex_time, solution_theta_d, '--k',
         label='Numerical Solution w/o Small Angle Approx', linewidth=3)
plt.title('Angular Velocity vs. Time: Damped Pendulum')
plt.xlabel('Time (Sec)')
plt.ylabel('Angular Velocity (Deg/s)')
plt.xlim([min(ex_time), max(ex_time)])
plt.ylim([min(solution_theta_d), max(solution_theta_d)])
plt.legend()
plt.grid()
plt.show()
