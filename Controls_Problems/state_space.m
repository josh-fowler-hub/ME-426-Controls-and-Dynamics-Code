clear
clc
close all

[tout,xout] = ode45(@Derivatives,[0 20],[0 0 0]');

A = [0 1 0;0 0 1;0 -2 -3];
C = [1 0 0];

y = C*xout';

plot(tout,y)