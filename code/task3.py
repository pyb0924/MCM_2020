import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

# define time, constants and initial statess
N1 = 4977  # initial N
P_env = 500  # initial P_env
E = [115, 130, 98, 95]  # E
alpha = 0.13  # N1:amount of waste
lamda = 0.15
r = 1000
beta = 3e-4
t_range = np.arange(0, 50)
INPUT = []
for i in range(4):  # for each E, create input series
    INPUT.append([N1, P_env, E[i]])


def diff_eqs(INP, t):
    y = np.zeros(3)
    v = INP
    y[0] = v[2] - alpha * v[1]
    K = lamda * v[0] - np.exp(beta * v[0])
    y[1] = r * v[1] * (1 - v[1] / K)
    y[2] = 0
    return y


# run and ploting (for each different E)
style = ['-r', '-g', '-y', '-b']
for i in range(4):
    RES = spi.odeint(diff_eqs, INPUT[i], t_range)
    if i == 0:
        plt.plot(RES[:, 0], style[i], label="E=" + str(E[i]) + "(now)")
    else:
        plt.plot(RES[:, 0], style[i], label="E=" + str(E[i]))

plt.legend(loc="best")
# plt.title('Influence of different initial E')
plt.xlabel('Time(year)')
plt.ylabel('N(10^6t)')
plt.savefig('figure\Estimation of minimal achievable level plastic.png', dpi=900)
plt.show()
