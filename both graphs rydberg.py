# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:19:00 2024

@author: User
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def odes(t, y):
    c1, cr, c11, c1r, cr1, crr =  y[0], y[1], y[2], y[3], y[4], y[5]
    dc1_dt = (-1j*(rabi*(np.sin(t/tau)**2))/2) * cr
    dcr_dt = -1j* delta*(np.cos(t/tau)**2) * cr + (-1j*(rabi*(np.sin(t/tau)**2))/2) * c1
    dc11_dt = -1j*(c1r*rabi*(np.sin(t/tau)**2)/2 + cr1*rabi*(np.sin(t/tau)**2)/2)
    dc1r_dt = -1j*(c1r*delta*(np.cos(t/tau)**2) + c11*rabi*(np.sin(t/tau)**2)/2 + crr*rabi*(np.sin(t/tau)**2)/2)
    dcr1_dt = -1j*(cr1*delta*(np.cos(t/tau)**2) + c11*rabi*(np.sin(t/tau)**2)/2 + crr*rabi*(np.sin(t/tau)**2)/2)
    dcrr_dt = -1j*(c1r*rabi*(np.sin(t/tau)**2)/2 + cr1*rabi*(np.sin(t/tau)**2)/2 + crr*(2*delta*(np.cos(t/tau)**2) + V))
    return [dc1_dt, dcr_dt, dc11_dt, dc1r_dt, dcr1_dt, dcrr_dt]

#define parameters
rabi = 0.1
delta = 1.8
tau = 154.85/rabi
V = 1.7
initial_conditions = [1.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]
t_span = (0, 500/rabi)
t = np.linspace(t_span[0], t_span[1], 10000)
    

#numerically solve odes using solve_ivp
solution = solve_ivp(odes, t_span, initial_conditions, t_eval=t)
c1_numerical, cr_numerical, c11_numerical, c1r_numerical, cr1_numerical, crr_numerical = solution.y
phasec11 = np.angle(c11_numerical)
    #plots
fig1 = plt.figure(figsize=(16, 9))
ax1 =plt.axes([0.1, 0.08, 0.8, 0.4])
ax2 = plt.axes([0.1, 0.55, 0.8, 0.4])
ax3 = ax1.twinx()
ax3.plot(t, phasec11, 'k', label='c11(t) phase', lw=2)
ax1.plot(t, np.abs(c11_numerical)**2, 'r', label='|c11(t)|^2 numerical', lw=3)
ax1.plot(t, np.abs(c1r_numerical)**2, 'b', label='|c1r(t)|^2 numerical', lw=3)
ax1.plot(t, np.abs(cr1_numerical)**2, 'g', label='|cr1(t)|^2 numerical', lw=3)
ax1.plot(t, np.abs(crr_numerical)**2, 'm', label='|crr(t)|^2 numerical', lw=3)
#ax1.plot(t, np.abs(c11_numerical)**2 + np.abs(c1r_numerical)**2 + np.abs(cr1_numerical)**2 + np.abs(crr_numerical)**2, 'k', label='Total Probability', lw=1.5)
ax2.plot(t, np.abs(c1_numerical)**2, 'r', label='|c1(t)|^2 numerical', lw=3)
ax2.plot(t, np.abs(cr_numerical)**2, 'b', label='|cr(t)|^2 numerical', lw=3)
ax1.set_xlabel('Time')
ax1.set_ylabel('Probability')
ax2.set_ylabel('Probability')
ax3.set_ylabel('Phase')
ax1.legend()
ax2.legend()
ax1.grid(True)
ax2.grid(True)
#plt.savefig(f'graphV={V}.png')
plt.show()