import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#define odes
def odes(t, y):
    c1, cr = y[0], y[1]
    dc1_dt = (-1j*(rabi*(np.sin(t/tau)**2))/2) * cr
    dcr_dt = -1j* delta*(np.cos(t/tau)**2) * cr + (-1j*(rabi*(np.sin(t/tau)**2))/2) * c1
    return [dc1_dt, dcr_dt]

#define parameters
rabi = 1
delta = 1
tau = 1000
initial_conditions = [1.0 + 0.0j, 0.0 + 0.0j]
t_span = (0, 3*np.pi)
t = np.linspace(t_span[0], t_span[1], 1000)
    
#numerically solve odes using solve_ivp
solution = solve_ivp(odes, t_span, initial_conditions, t_eval=t)
c1_numerical, cr_numerical = solution.y

delta_new = delta * (np.cos(t/tau))**2
rabi_new = rabi * (np.sin(t/tau))**2
    
#analytical solutions
c1_squared_analytical = (1/(delta_new**2+rabi_new**2))*(delta_new**2+rabi_new**2*(np.cos(0.5*np.sqrt(delta_new**2+rabi_new**2)*t)**2))
cr_squared_analytical = rabi_new**2*(1/(delta_new**2+rabi_new**2))*(np.sin(0.5*np.sqrt(delta_new**2+rabi_new**2)*t)**2)

#plots
plt.figure(figsize=(15, 8))
plt.plot(t, np.abs(c1_numerical)**2, 'r', label='|c1(t)|^2 numerical', lw=3)
plt.plot(t, np.abs(cr_numerical)**2, 'b', label='|cr(t)|^2 numerical', lw=3)
plt.plot(t, c1_squared_analytical, color=(1.0, 1.0, 0.0), label='|c1(t)|^2 analytical', lw=1.5, linestyle='--')
plt.plot(t, cr_squared_analytical, 'lime', label='|cr(t)|^2 analytical',lw=1.5, linestyle='--')
#plt.plot(t, np.abs(cr_numerical)**2 + np.abs(c1_numerical)**2, 'k', label='Total Probability', lw=1.5)
plt.xlabel('Time')
plt.ylabel('Probability')
plt.legend()
plt.title(f'Evolution of C1 and Cr: Δ = {delta}, Ω = {rabi}, tau = {tau}')
plt.xticks(np.arange(0, 3*np.pi + np.pi/2, np.pi/2), ['0', '$\\frac{\pi}{2}$', '$\pi$', '$\\frac{3\pi}{2}$', '$2\pi$', '$\\frac{5\pi}{2}$', '$3\pi$'])
plt.grid(True)
plt.savefig(f'graphtau={tau}.png')
plt.show()