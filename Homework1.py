#import numpy as np
import cupy as cp
#import matplotlib as mlt

with cp.cuda.Device(0):
    x = cp.array([1, 2, 3, 4, 5])
print(x)
