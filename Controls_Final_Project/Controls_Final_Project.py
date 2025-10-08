# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:04:20 2018


@author: jfowl
"""
import numpy as np
from numba import jit
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.close('all')

mi = 300  # initial weight of rocket in kg
Mars_m = 6.39e23  # mass of Mars in kg
G = 6.67408e-11  # Gravitational Constant SI units
Isp = 291  # Specific Impulse of rocket in seconds
g = 9.81  # Gravitational Acceleration on Earth m/s^2
tint = 0  # initial time
op_time = 43  # Operational Time of rocket in seconds
tot_time = 7000  # Total Simulation Time in seconds
nt = 70000  # number of time steps
tvec = np.linspace(tint, tot_time, nt)  # time vector
dt = tvec[1]  # length of time step
T = 15000  # Thrust in Newtons
b = 3  # length of rocket in meters
d = 0.5  # diameter of rocket in meters
betai = 0  # intial thrust angle
thetai = 90  # intital pitch angle
d_Mars = 6779000  # diameter of Mars in meters
r_Mars = d_Mars/2  # radius of Mars in meters
start_pos = np.asarray([[r_Mars], [0]])  # starting position of rocket,
# surface of Mars
start_vel = np.asarray([[0], [0]])  # starting velocity in m/s
start_accel = np.asarray([[0], [0]])  # starting accelleration in m/s^2
escape_vel = 5.03e3  # escape velocity of Mars in m/s
start_theta = 0*(np.pi/180)
thetac = 90*(np.pi/180)
thetadc = 0
low_cut_off = -45*(np.pi/180)
high_cut_off = 45*(np.pi/180)
rollover = 0.1


def mdot(T, Isp, g):
    """Mass Flow Rate of fuel being expended by the rocket."""
    md = - (T/(Isp * g))
    return md


def Thrust_vec(beta, md):
    """Thrust Vector as a function of the thrust angle beta."""
    if md != 0:
        Tx = np.cos(beta)
        Ty = -np.sin(beta)
    else:
        Tx = 0
        Ty = 0
    return T*np.asarray([[Tx], [Ty]])


@jit
def theta_dd(beta, J, length, md):
    """Angular Acceleration of the rocket through pitch angle theta."""
    Tvec = Thrust_vec(beta, md)
    theta_dbld = -Tvec[1]*length/(2 * J)
    return theta_dbld


@jit
def T_vec_inert(beta, theta, md):
    """Thrust Vector in the inertial reference frame."""
    Tvec = Thrust_vec(beta, md)
    Rot_Mat = np.asarray([[np.cos(theta), -np.sin(theta)],
                          [np.sin(theta), np.cos(theta)]])
    Tvec_inert = np.dot(Rot_Mat, Tvec)
    return Tvec_inert


@jit
def Gravitational_Force_vec(mM, mR, pos):
    """Gravitational Force Vector."""
    r = np.sqrt(pos[0]**2 + pos[1]**2)
    scalar_term = (G*mM*mR)/(r**3)
    FGvec = scalar_term*pos
    return FGvec


@jit
def acc_vec(beta, theta, mM, mR, pos, md):
    """Acceleration vector."""
    Tvec_inert = T_vec_inert(beta, theta, md)
    FGvec = Gravitational_Force_vec(mM, mR, pos)
    avec = (1/mR)*(Tvec_inert - FGvec)
    return avec


def MoIx(m, r, h):
    """Moment of Inertia about the Yaw Axis."""
    J = (1/4)*m*r**2 + (1/3)*m*h**2
    return J


@jit
def non_linear_derivatives(Z, t):
    """Reduction to system of Equations for odeint."""
    Kp = 0.055
    Kd = 0.11
    Ki = 0.000011
    x = Z[0]
    xd = Z[1]
    y = Z[2]
    yd = Z[3]
    theta = Z[4]
    thetad = Z[5]
    mass = Z[6]
    gamma = Z[7]
    position = np.asarray([[x], [y]])
    if t <= op_time:
        md = mdot(T, Isp, g)
    else:
        md = 0
    J = MoIx(mass, d/2, b)
    e = thetac - theta
    ed = thetadc - thetad
    if t < rollover:
        beta = 0
    else:
        beta = Kp*e + Kd*ed + Ki*gamma
    if beta > high_cut_off:
        beta = high_cut_off
    elif beta < low_cut_off:
        beta = low_cut_off
    else:
        pass
    gammad = e
    thetadd = float(theta_dd(beta, J, b, md))
    avec = acc_vec(beta, theta, Mars_m, mass, position, md)
    xdd = float(avec[0])
    ydd = float(avec[1])
    return [xd, xdd, yd, ydd, thetad, thetadd, md, gammad]


states = odeint(non_linear_derivatives,
                [float(start_pos[0]), 0, float(start_pos[1]), 0, start_theta,
                 0, mi, 0],
                tvec)

xlimmax = max([abs(x) for x in states[:, 0]])
xlimmin = -xlimmax
ylimmax = max([abs(x) for x in states[:, 2]])
ylimmin = -ylimmax


elevation = []
for i in range(len(states[:, 0])):
    r = (states[i, 0]**2 + states[i, 2]**2)**(1/2)
    e = r - r_Mars
    elevation.append(e)


plt.style.use(['dark_background'])

fig = plt.figure()
circle = plt.Circle((0, 0), radius=r_Mars, fc='r')
ax = fig.add_subplot(111, autoscale_on=False,
                     xlim=(xlimmin - 1000, xlimmax + 1000),
                     ylim=(ylimmin - 1000, ylimmax + 1000))
ax.grid(True)
ax.plot(float(start_pos[0]), float(start_pos[1]), 'b.')
ax.add_patch(circle)
line, = ax.plot([], [], 'y', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.8, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


xs = []
ys = []


def animate(i):
    xs.append(states[i, 0])
    ys.append(states[i, 2])
    line.set_data(xs, ys)
    time_text.set_text(time_template % (i*dt))
    return line, time_text


ani = animation.FuncAnimation(fig, animate, np.arange(1, len(states[:, 3])),
                              interval=1, blit=False, init_func=init)

#ani.save('orbit.html', writer=None, fps=1000)
plt.title('Rocket Orbiting Mars 2D')
plt.xlabel('Horizontal')
plt.ylabel('Vertical')
plt.show()

#circle = plt.Circle((0, 0), radius=r_Mars, fc='r')
#plt.figure(figsize=(11, 11))
#ax = plt.gca()
#ax.add_patch(circle)
#plt.title('Rocket Takeoff and Orbit @ Simulation Time of {} seconds'.format(
#        tot_time))
#plt.xlabel('Horizontal Plane (m)')
#plt.ylabel('Vertical Plane (m)')
#plt.plot(states[:, 0], states[:, 2])
#if tot_time == 43:
#    plt.xlim([min(states[:, 0]) - 1000, max(states[:, 0]) + 1000])
#    plt.ylim([min(states[:, 2]) - 1000, max(states[:, 2]) + 1000])
#plt.savefig('orbit_{}_linear.png'.format(tot_time))
#plt.show()
#
#plt.figure()
#plt.plot(tvec, [(states[i, 1]**2 +
#                 states[i, 3]**2)**(1/2) for i in range(len(states[:, 1]))])
#plt.title('Time vs. Velocity')
#plt.xlabel('Time (sec)')
#plt.ylabel(r'$Velocity \, (\frac{m}{sec})$')
#plt.grid(linestyle='--')
#plt.savefig('TvV_orbit_{}_linear.png'.format(tot_time))
#plt.show()
#
#plt.figure()
#plt.plot(tvec, elevation)
#plt.title('Time vs. Elevation from Surface')
#plt.xlabel('Time (sec)')
#plt.ylabel('Elevation (m)')
#plt.grid(linestyle='--')
#plt.savefig('TvE_orbit_{}_linear.png'.format(tot_time))
#plt.show()
#
#plt.figure()
#plt.plot(tvec, states[:, 4])
#plt.title(r'$Time \, vs. \, \theta$')
#plt.xlabel('Time (sec)')
#plt.ylabel(r'$\theta \,\, (rad)$')
#plt.grid(linestyle='--')
#plt.savefig('TvTheta_orbit_{}_linear.png'.format(tot_time))
#plt.show()