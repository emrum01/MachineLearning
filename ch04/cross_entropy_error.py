import numpy as np

def cross(y,t):
    if y.ndim==1:
        t=t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    delta = 1e-7
    batch_size = y.shape[0]
    print(y.shape[0])
    return -np.sum(t*np.log(y+delta))/batch_size

t = [0,0,1,0,0,0,0,0,0,0]
y = [0.1,0.05,0.6,0.0,0.0,0.0,0.0,0.0,0.0,0.0]

print(cross(np.array(y),np.array(t)))

def mean_squared_error(y,t):
    return 0.5*np.sum((y-t)**2)
    

print(mean_squared_error(np.array(y),np.array(t)))