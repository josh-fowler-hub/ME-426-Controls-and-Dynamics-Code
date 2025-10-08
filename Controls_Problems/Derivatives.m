function dzdt = Derivatives(t,z)

A = [0 1 0;0 0 1;0 -2 -3];

B = [0 0 1]';
C = [1 0 0];
Cshifted = [0 1 0];

%%%No control
%u = 0;

%%%Step response
%u = 5;

%%%Proportional Control
%y_command = 360*pi/180;
%y = C*z;
%kp = -1;
%u = kp*(y-y_command);

%%%%Derivative Control and Proportional Control
y_command = 360*pi/180;
y = C*z;
ydot = Cshifted*z;
kp = 1;
kd = 1;
u = kp*(y_command-y) - kd*ydot;

dzdt = A*z + B*u;