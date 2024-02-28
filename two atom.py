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
rabi = 1
delta = 1
tau = 1
V = 1
initial_conditions = [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]
t_span = (0, 3*np.pi)
t = np.linspace(t_span[0], t_span[1], 1000)
    
#numerically solve odes using solve_ivp
solution = solve_ivp(odes, t_span, initial_conditions, t_eval=t)
c11_numerical, c1r_numerical, cr1_numerical, crr_numerical = solution.y
    
#analytical solutions
c1_squared_analytical = 1/(delta**2+rabi**2)*(delta**2+(np.cos(0.5*np.sqrt(delta**2+rabi**2)*t)**2))
cr_squared_analytical = rabi**2/(delta**2+rabi**2)*(np.sin(0.5*np.sqrt(delta**2+rabi**2)*t)**2)

#plots
plt.figure(figsize=(15, 8))
plt.plot(t, np.abs(c11_numerical)**2, 'r', label='|c11(t)|^2 numerical', lw=3)
plt.plot(t, np.abs(c1r_numerical)**2, 'b', label='|c1r(t)|^2 numerical', lw=3)
plt.plot(t, np.abs(cr1_numerical)**2, 'g', label='|cr1(t)|^2 numerical', lw=3)
plt.plot(t, np.abs(crr_numerical)**2, 'm', label='|crr(t)|^2 numerical', lw=3)
plt.plot(t, np.abs(c11_numerical)**2 + np.abs(c1r_numerical)**2 + np.abs(cr1_numerical)**2 + np.abs(crr_numerical)**2, 'k', label='Total Probability', lw=1.5)
plt.xlabel('Time')
plt.ylabel('Probability')
plt.legend()
plt.title(f'Evolution of C1 and Cr: Δ = {delta}, Ω = 1')
plt.xticks(np.arange(0, 3*np.pi + np.pi/2, np.pi/2), ['0', '$\\frac{\pi}{2}$', '$\pi$', '$\\frac{3\pi}{2}$', '$2\pi$', '$\\frac{5\pi}{2}$', '$3\pi$'])
plt.grid(True)
plt.savefig(f'graphdelta={delta}.png')
plt.show()