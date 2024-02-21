from pylab import *
from matplotlib.pyplot import *
from numpy import *

Nvalues = [50,100,250,500,800,1000,1500]
walkdev = zeros(len(Nvalues))
for i in range(len(Nvalues)):
    N = Nvalues[i]
    M = 100000
    for im in range(N):
        x = cumsum(2*random.randint(0,2,size=N)-1)
        xdev = std(x)**2
        walkdev[i]= walkdev[i]+ xdev
    walkdev[i]=walkdev[i]/(N)
plot(Nvalues,walkdev,'-o'),xlabel('N'),ylabel('$dx^2(N)$')
show()

from pylab import *
M = 10000  # number of walkers
L = 100    # max size of lattice
# each time step - move walkers and propagate diffusion solution
p = 0.1    # prob for motion
pinv = 1.0 - p
nsteps = 3001  # number of steps
# initializing walkers
x = zeros(M)  # init posn of walkers
edges = array(range(-L, L + 1)) - 0.5
xc = 0.5 * (edges[:-1] + edges[1:])
# init concentrations
c = zeros((2 * L + 1, 2))
i0 = 0
i1 = 1
c[L] = M  # c[L] corresponds to x = 0
cx = range(-L, L + 1)
D = p
ion()
noutput = 10

for it in range(nsteps):
    # first update posn of all random walkers
    for iw in range(M):
        rnd = rand(1)
        dx = -1 * (rnd < p) + 1 * (rnd > pinv)
        x[iw] = x[iw] + dx

    # perform explicit step for diffusion equation
    for ix in range(1, len(c) - 1):
        # use i0 and generate i1
        c[ix, i1] = c[ix, i0] + D * (c[ix - 1, i0] - 2 * c[ix, i0] + c[ix + 1, i0])
    # flip i0 and i1
    ii = i1
    i1 = i0
    i0 = ii
    # plot the two concentrations now
    if mod(it, noutput) == 0:
        Nx, e = histogram(x, edges)
        clf()
        plot(cx, c[:, i0], '-r', xc, Nx, '-b')
        xlabel('x'), ylabel('N'), pause(0.001)
