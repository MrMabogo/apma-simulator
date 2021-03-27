import time
import numpy as np

seed = 1000
prev = 0

mult = 24693
inc = 1753
modu = np.power((2,),(15,))

def set_seed(in_seed):
    global seed
    seed = in_seed

def generate():
    global seed
    seed = (mult*seed+inc)%modu
    next = seed/modu
    return next

if __name__ == "__main__()":
    pass
