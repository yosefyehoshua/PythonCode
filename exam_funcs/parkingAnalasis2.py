import numpy as np

from lmfit import minimize, Parameters
from matplotlib.pyplot import plot, hold

s = np.float_(np.array(range(0,1201,1200//8)))
v = np.round(120*s/(171+s) + np.random.uniform(size=9), 2)

def residual(p, x, data):
    vmax = p['vmax'].value
    km = p['km'].value
    model = vmax * x / (km + x)
    return (data - model)

p = Parameters()
p.add('vmax', value=1., min=0.)
p.add('km', value=1., min=0.)

out = minimize(residual, p, args=(s, v))

plot(s, v, 'bo')
hold(True)

ss = np.float_(np.array(range(0,1201,1200//100)))
y = p['vmax'].value * ss / (p['km'].value + ss)
plot(ss, y, 'r-')
hold(False)