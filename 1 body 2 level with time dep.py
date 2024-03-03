# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:48:50 2024

@author: rolan
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#define odes
def odes1(ti, y):
    c1, cr = y[0], y[1]
    dc1_dt = (-1j*rabi_0*(np.sin(ti/tauc)**2)/2)*cr
    dcr_dt = -1j*delta_0*(np.cos(ti/tauc)**2)*cr + (-1j*rabi_0*(np.sin(ti/tauc)**2)/2)*c1
    return [dc1_dt, dcr_dt]

def odes(ti, y):
    c1, cr = y[0], y[1]
    dc1_dt = (-1j*rabi_0/2)*cr
    dcr_dt = -1j*delta_0*cr + (-1j*rabi_0/2)*c1
    return [dc1_dt, dcr_dt]

#define parameters
rabi_0 = 1
delta_0 = rabi_0*0
tau = [1*np.pi, 3*np.pi, 9*np.pi, 100*np.pi, 1000*np.pi, 1000000*np.pi]
initial_conditions = [1.0 + 0.0j, 0.0 + 0.0j]
t_span = (0, 3*np.pi)
t = np.linspace(t_span[0], t_span[1], 1000)
#rabi = rabi_0*(np.sin(t/tau))**2
#delta = delta_0*(np.cos(t/tau))**2
#numerically solve odes using solve_ivp
#solutiont = solve_ivp(odes1, t_span, initial_conditions, t_eval=t)
#c1_numericalt, cr_numericalt = solutiont.y

solution = solve_ivp(odes, t_span, initial_conditions, t_eval=t)
c1_numerical, cr_numerical = solution.y
   
#analytical solutions
#c1_squared_analytical = 1/(delta**2+rabi**2)*(delta**2+(np.cos(0.5*np.sqrt(delta**2+rabi**2)*t)**2))
#cr_squared_analytical = rabi**2/(delta**2+rabi**2)*(np.sin(0.5*np.sqrt(delta**2+rabi**2)*t)**2)
#c1_numericalt = 0
#plots
plt.figure(figsize=(15, 8))
#plt.plot(t, np.abs(c1_numerical)**2, 'r', label='|c1(t)|^2 numerical', lw=3)
for n in tau:
    tauc = n
    solutiont = solve_ivp(odes1, t_span, initial_conditions, t_eval=t)
    c1_numericalt, cr_numericalt = solutiont.y
    plt.plot(t, np.abs((np.abs(cr_numericalt)**2)-np.abs(cr_numerical)**2), label = f'τ = {tauc/np.pi}$\pi$', lw=3)

#plt.plot(t, c1_squared_analytical, color=(1.0, 1.0, 0.0), label='|c1(t)|^2 analytical', lw=1.5, linestyle='--')
#plt.plot(t, cr_squared_analytical, 'lime', label='|cr(t)|^2 analytical',lw=1.5, linestyle='--')
#plt.plot(t, np.abs(cr_numerical)**2 + np.abs(c1_numerical)**2, 'k', label='Total Probability', lw=1.5)
plt.xlabel('Time')
plt.ylabel('Probability difference')
plt.legend()
plt.title('difference of $|C1|^2$ between when Δ and Ω are time-dependent and when they are time-independent')
#plt.xticks(np.arange(0, 3*np.pi + np.pi/2, np.pi/2), ['0', '$\\frac{\pi}{2}$', '$\pi$', '$\\frac{3\pi}{2}$', '$2\pi$', '$\\frac{5\pi}{2}$', '$3\pi$'])
plt.grid(True)
#plt.savefig(f'graphdelta={delta}.png')
plt.show()