import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def odes_double(t, y, rabi, delta, V, tau):
    c11, c1r, cr1, crr = y[0], y[1], y[2], y[3]
    dc11_dt = -1j*(c1r*rabi*(np.sin(t/tau)**2)/2 + cr1*rabi*(np.sin(t/tau)**2)/2)
    dc1r_dt = -1j*(c1r*delta*(np.cos(t/tau)**2) + c11*rabi*(np.sin(t/tau)**2)/2 + crr*rabi*(np.sin(t/tau)**2)/2)
    dcr1_dt = -1j*(cr1*delta*(np.cos(t/tau)**2) + c11*rabi*(np.sin(t/tau)**2)/2 + crr*rabi*(np.sin(t/tau)**2)/2)
    dcrr_dt = -1j*(c1r*rabi*(np.sin(t/tau)**2)/2 + cr1*rabi*(np.sin(t/tau)**2)/2 + crr*(2*delta*(np.cos(t/tau)**2) + V))
    return [dc11_dt, dc1r_dt, dcr1_dt, dcrr_dt]

# Define parameter ranges
rabi = 1
delta_range = np.arange(1, 11, 1)
V_range = np.arange(0, 12, 1)
tau_range = np.arange(0.5*np.pi, 5*np.pi, 0.5*np.pi)

# Iterate over each combination
for delta_val in delta_range:
    for V_val in V_range:
        for tau_val in tau_range:

            initial_conditions_double = [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]
            t_span = (0, 10*np.pi)
            t = np.linspace(t_span[0], t_span[1], 1000)

            solution = solve_ivp(odes_double, t_span, initial_conditions_double, t_eval=t, args=(rabi, delta_val, V_val, tau_val))
            c11_numerical, c1r_numerical, cr1_numerical, crr_numerical = solution.y

            plt.figure(figsize=(15, 8))
            plt.plot(t, np.abs(c11_numerical)**2, 'r', label='|c11(t)|^2 numerical', lw=3)
            plt.plot(t, np.abs(c1r_numerical)**2, 'b', label='|c1r(t)|^2 numerical', lw=3)
            plt.plot(t, np.abs(cr1_numerical)**2, 'g', label='|cr1(t)|^2 numerical', lw=3)
            plt.plot(t, np.abs(crr_numerical)**2, 'm', label='|crr(t)|^2 numerical', lw=3)
            plt.xlabel('Time')
            plt.ylabel('Probability')
            plt.legend()
            plt.title(f'EΔ = {delta_val}, V = {V_val}, tau = {tau_val/np.pi}')
            plt.xticks(np.arange(0, 10*np.pi + np.pi/2, np.pi/2), ['0', '$\\frac{\pi}{2}$', '$\pi$', '$\\frac{3\pi}{2}$', '$2\pi$', '$\\frac{5\pi}{2}$', '$3\pi$', '$\\frac{7\pi}{2}$', '$4\pi$', '$\\frac{9\pi}{2}$', '$5\pi$', '$\\frac{11\pi}{2}$', '$6\pi$', '$\\frac{13\pi}{2}$', '$7\pi$', '$\\frac{15\pi}{2}$', '$8\pi$', '$\\frac{17\pi}{2}$', '$9\pi$', '$\\frac{19\pi}{2}$', '$10\pi$'])
            plt.grid(True)
            plt.savefig(f'{delta_val} | {V_val} | {tau_val/np.pi}.png')
            plt.close()  # Close the figure to prevent it from being displayed