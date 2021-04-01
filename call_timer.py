from rng import generate
from rng import set_seed
from rvg import random_var

def call_customer():
    time = 0
    success = False
    calls = 0
    while(not success and calls != 4):
        time += 6
        calls += 1
        cran = generate()
        if cran <= .2: #.2 busy probability
            time += 4
        elif cran > .2 and cran <= .5: #.3 unavailable probability
            time += 26
        else: #available
            x = random_var(generate())
            if x >= 25: #doesn't answer in time
                time += 26
            else: #answers in time
                time += x
                success = True
    return time
