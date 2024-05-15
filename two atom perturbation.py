import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#define odes
def odes(t, y):
    c11, c1r, cr1, crr = y[0], y[1], y[2], y[3]
    dc11_dt = -1j*(c1r*rabi/2 + cr1*rabi/2)
    dc1r_dt = -1j*(c1r*delta + c11*rabi/2 + crr*rabi/2)
    dcr1_dt = -1j*(cr1*delta + c11*rabi/2 + crr*rabi/2)
    dcrr_dt = -1j*(c1r*rabi/2 + cr1*rabi/2 + crr*(2*delta + V))
    return [dc11_dt, dc1r_dt, dcr1_dt, dcrr_dt]

#define parameters
delta = 15
V = 0
rabi = 1
initial_conditions = [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]
t_span = (0, 3*np.pi)
t = np.linspace(t_span[0], t_span[1], 1000)
    
#numerically solve odes using solve_ivpb
solution = solve_ivp(odes, t_span, initial_conditions, t_eval=t)
c11_numerical, c1r_numerical, cr1_numerical, crr_numerical = solution.y
    
#analytical solutions
cr1_squared_analytical = ((rabi**2)/(delta**2))*(np.sin(delta*t/2))**2
c1r_squared_analytical = ((rabi**2)/(delta**2))*(np.sin(delta*t/2))**2
crr_squared_analytical = np.zeros(np.shape(t))
c11_squared_analytical = 1 - cr1_squared_analytical - c1r_squared_analytical

#plots
plt.figure(figsize=(15, 8))
plt.plot(t, np.abs(c11_numerical)**2, 'r', label='|c11(t)|^2 numerical', lw=3)
plt.plot(t, np.abs(c1r_numerical)**2, 'b', label='|c1r(t)|^2 numerical', lw=3)
plt.plot(t, np.abs(cr1_numerical)**2, 'g', label='|cr1(t)|^2  numerical', lw=3)
plt.plot(t, np.abs(crr_numerical)**2, 'm', label='|crr(t)|^2 numerical', lw=3)
plt.plot(t, c11_squared_analytical, 'k', label='|c11(t)|^2 analytical perturbation', lw=3,  linestyle='--')
plt.plot(t, c1r_squared_analytical, 'y', label='|c1r(t)|^2 analytical perturbation', lw=3,  linestyle='dashdot')
plt.plot(t, cr1_squared_analytical, 'purple', label='|cr1(t)|^2 analytical perturbation', lw=3,  linestyle='--')
plt.plot(t, crr_squared_analytical, 'pink', label='|crr(t)|^2 analytical perturbationl', lw=3,  linestyle='--')
plt.xlabel('Time')
plt.ylabel('Probability')
plt.legend()
plt.title(f'Evolution of C1 and Cr: Δ = {delta}, Ω = {rabi}')
plt.xticks(np.arange(0, 3*np.pi + np.pi/2, np.pi/2), ['0', '$\\frac{\pi}{2}$', '$\pi$', '$\\frac{3\pi}{2}$', '$2\pi$', '$\\frac{5\pi}{2}$', '$3\pi$'])
plt.grid(True)
plt.savefig(f'graphdelta={delta}.png')
plt.show()