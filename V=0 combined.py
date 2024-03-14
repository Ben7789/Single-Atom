import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#define odes
def odes_single(t, y):
    c1, cr = y[0], y[1]
    dc1_dt = -1j*rabi/2 * cr
    dcr_dt = -1j* delta * cr + -1j*rabi/2 * c1
    return [dc1_dt, dcr_dt]


def odes_double(t, y):
    c11, c1r, cr1, crr = y[0], y[1], y[2], y[3]
    dc11_dt = -1j*(c1r*rabi/2 + cr1*rabi/2)
    dc1r_dt = -1j*(c1r*delta + c11*rabi/2 + crr*rabi/2)
    dcr1_dt = -1j*(cr1*delta + c11*rabi/2 + crr*rabi/2)
    dcrr_dt = -1j*(c1r*rabi/2 + cr1*rabi/2 + crr*(2*delta + V))
    return [dc11_dt, dc1r_dt, dcr1_dt, dcrr_dt]


#define parameters
rabi = 1
delta = 1
V = 0
initial_conditions_single = [1.0 + 0.0j, 0.0 + 0.0j]
initial_conditions_double = [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]
t_span = (0, 3*np.pi)
t = np.linspace(t_span[0], t_span[1], 1000)

#numerically solve odes using solve_ivp
solution = solve_ivp(odes_single, t_span, initial_conditions_single, t_eval=t)
c1_numerical, cr_numerical = solution.y

solution = solve_ivp(odes_double, t_span, initial_conditions_double, t_eval=t)
c11_numerical, c1r_numerical, cr1_numerical, crr_numerical = solution.y

#plots
plt.figure(figsize=(15, 8))
plt.plot(t, np.abs(c1_numerical)**2, 'r', label='|c1(t)|^2', lw=3)
plt.plot(t, np.abs(cr_numerical)**2, 'b', label='|cr(t)|^2', lw=3)
plt.plot(t, np.abs(c11_numerical)**2 + np.abs(c1r_numerical)**2, color=(1.0, 1.0, 0.0), label='|c11(t)|^2 + |c1r(t)|^2', lw=1.5, linestyle='--')
plt.plot(t, np.abs(crr_numerical)**2 + np.abs(cr1_numerical)**2, 'lime', label='|crr(t)|^2 + |cr1(t)|^2', lw=1.5, linestyle='--')
plt.xlabel('Time')
plt.ylabel('Probability')
plt.legend()
plt.title(f'Comparison of Single and Two atom cases for V = {0}: Δ = {delta}, Ω = {rabi}')
plt.xticks(np.arange(0, 3*np.pi + np.pi/2, np.pi/2), ['0', '$\\frac{\pi}{2}$', '$\pi$', '$\\frac{3\pi}{2}$', '$2\pi$', '$\\frac{5\pi}{2}$', '$3\pi$'])
plt.grid(True)
plt.savefig(f'graphcombineddelta={delta}.png')
plt.show()