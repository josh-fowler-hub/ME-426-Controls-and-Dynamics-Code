# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:10:22 2018

@author: jfowl
"""
import numpy as np
import scipy.linalg as lin

rho = (2.7*100**3)/1000
b = 1*0.0254  # width m
h = (1/8)*0.0254  # thickness m
ltot = 12*0.0254  # total length m
vol = ltot*b*h  # volume m^3
A = b*h  # Cross Sectional Area m^2
L = 10.8125*0.0254
I = (b*h**3)/12
num_elems = 3
E = 69e9

m = ((rho*A*L)/420)
mmat = np.asarray([[156, 22*L, 54, -13*L],
                   [22*L, 4*L**2, 13*L, -3*L**2],
                   [54, 13*L, 156, -22*L],
                   [-13*L, -3*L**2, -22*L, 4*L**2]])
mmat = m*mmat

k = (E*I)/L**3
kmat = np.asarray([[12, 6*L, -12*L, 6*L],
                   [6*L, 4*L**2, -6*L, 2*L**2],
                   [-12, -6*L, 12, -6*L],
                   [6*L, 2*L**2, -6*L, 4*L**2]])
kmat = k*kmat

M = np.zeros([2*num_elems + 2, 2*num_elems + 2])
K = np.zeros([2*num_elems + 2, 2*num_elems + 2])

for i in range(num_elems):
    M[2*i:2*i + 4, 2*i:2*i + 4] = mmat
    K[2*i:2*i + 4, 2*i:2*i + 4] = kmat

assembled_matrix = K - M
eigvals, eigvecs = lin.eigh(assembled_matrix)

print('Eigenvalues and Eigenvectors:')
print(eigvals, eigvecs)
print('\n\n')
print('Natural Frequencies:')
print([np.sqrt(w) for w in eigvals])
