import numpy as np
import matplotlib.pyplot as plt
NA = 50 # Number of oscillators in Crystal A
NB = 100 # Number of oscillators in Crystal B
qA = 100 # Initial energy of Crystal A
qB = 50 # Initial energy of Crystal B
q = qA + qB # Total energy
N = NA + NB # Total oscillators
state = np.zeros(N, int) # Microstate of the system
# Initial state
state[:qA] = 1 # Crystal A starts with qA energy
state[NA:NA + qB] = 1 # Crystal B starts with qB energy
# Simulate state development
nstep = 1000
EA = np.zeros(nstep, float)
EB = np.zeros(nstep, float)
for istep in range(nstep):
  i1 = np.random.randint(0, N) # Select random oscillator i1
  if state[i1] > 0: # Does it have any energy?
    i2 = np.random.randint(0, N) # Select random oscillator i2
    state[i2] = state[i2] + 1 # Transfer energy
    state[i1] = state[i1] - 1
  # Calculate and store average energies
  EA[istep] = np.sum(state[:NA]) / NA
  EB[istep] = np.sum(state[NA:]) / NB
# Plot the time development
plt.plot(np.arange(nstep), EA, label='Crystal A')
plt.plot(np.arange(nstep), EB, label='Crystal B')
plt.xlabel('Time t')
plt.ylabel('Average Energy per Oscillator \n q_A/N_A , q_B/N_B')
plt.title('Time Development of Two Einstein Crystals in Thermal Contact \n for NA = 50,NB= 100, qA = 100, qB = 50')
plt.legend()
plt.show()


