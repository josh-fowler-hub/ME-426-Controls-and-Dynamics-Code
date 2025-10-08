###Integrate an ordinary differential equation
#in MATLAB that's using the function ode45.
#in Python we're going to use the Scipy toolbox and odeint
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as I
import control as ctl
import scipy.signal as S
import scipy.linalg as slin

##Create a function
def Derivatives(z,t):
    x = z[0] #Oh btw array start with 0 in python not 1 like MATLAb 
    xdot = z[1]
    xdbldot = -8.0*xdot - 25.0*x + 10
    zdot = np.asarray([xdot,xdbldot])

    return zdot #zdot is my output
    
##Create a function
def DerivativesSS(z,t):
    f = 10
    A = np.asarray([[0.0,1.0],[-25.0,-8.0]])
    B = np.asarray([0.0,1.0])
    zdot = np.matmul(A,z) + B*f ##This is where MATLAB is better. No need for matmul. Matrix Laboratory ftw.
    return zdot #zdot is my output

##Main script
plt.close("all")

#integrate for 10 seconds
tout = np.linspace(0,10,10000)
zinitial = np.asarray([0,0])
zout = I.odeint(Derivatives,zinitial,tout)

xout = zout[:,0]
xdotout = zout[:,1]

plt.plot(tout,xout,label='Scipy Toolbox')

##Analytic Solution
x_analytic = np.exp(-4.0*tout)*(-2.0/5.0*np.cos(3.0*tout) - 8.0/15.0*np.sin(3.0*tout)) + 2.0/5.0
plt.plot(tout,x_analytic,'r--',label='Analytic Solution')

###Zeros poles and gains
# X = 10 / (s * (s^2 + 8s + 25) )
N,D = S.zpk2tf([],[0,-4+3j,-4-3j],10)
sys = ctl.tf(N,D)
print(sys)
tout,yout = ctl.impulse_response(sys,tout)
plt.plot(tout,yout,'g--',label='Control Toolbox')

##Analytic Solution using Inverse Laplace
A = 2.0/5.0
B = -2.0/5.0
C = -16.0/5.0
#print (C-4.0*B)/3.0,-8.0/15.0
x_analytic_laplace = A + B*np.exp(-4.0*tout)*np.cos(3.0*tout) + ((C-4.0*B)/3.0)*np.exp(-4.0*tout)*np.sin(3.0*tout)
plt.plot(tout,x_analytic_laplace,'k--',label='Inverse Laplace')

###Integrate using State Space
zoutSS = I.odeint(DerivativesSS,zinitial,tout)
xoutSS = zout[:,0]
plt.plot(tout,xoutSS,'y--',label='Scipy State Space')

##Analytically Solve for SS
A = np.asarray([[0.0,1.0],[-25.0,-8.0]])
B = np.asarray([0.0,1.0])
f = 10
D = -np.matmul(np.linalg.inv(A),B)*f
xoutSS_Analytic = []
for t in tout:
    zi = -np.matmul(slin.expm(A*t),D) + D
    xoutSS_Analytic.append(zi[0])

plt.plot(tout,xoutSS_Analytic,'m--',label='State Space Analytic')

plt.grid()
plt.legend()
plt.show()