from rng import generate
from rng import set_seed
from rvg import random_var
from call_timer import call_customer
from bisect import bisect_left

def get_sample(n):
    '''
    Generate n independent realizations of W, the call time
    '''
    set_seed(1000)
    ret = []
    for i in range(0,n):
        ret.append(call_customer())
    return ret

def distribution(sample, x): #P[sample <= x]
    i = int(bisect_left(sample, x))
    return (i+1)/len(sample) #probability = occurences/all events

def print_stats(sample): #mean and quartiles of sorted sample x
    sz = len(sample)
    mean = sum(sample)/sz
    median = mean
    if sz % 2 == 0:
        median = (sample[int(sz/2)]+sample[int(sz/2-1)])/2
    else:
        median = sample[int(sz/2)[0]]

    q1 = sample[int(sz/4)]
    q3 = sample[int(sz*3/4)]

    print(f"Mean:{mean}\nMedian:{median}\n1st quartile:{q1}\n3rd quartile:{q3}")

vals = get_sample(1000)
sorted = list(vals)
sorted.sort()
print_stats(sorted)
print(f"P[W<=15]={distribution(sorted, 15)}")
print(f"P[W<=20]={distribution(sorted, 20)}")
print(f"P[W<=30]={distribution(sorted, 30)}")
print(f"P[W>40]={1-distribution(sorted, 40)}")
print(f"P[W>60]={1-distribution(sorted, 60)}")
print(f"P[W>80]={1-distribution(sorted, 80)}")
print(f"P[W>90]={1-distribution(sorted, 90)}")
