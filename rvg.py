import numpy as np
def random_var(ui):
    #np.log is actually ln, there are other ways to do ln if you don't want to use np, so I could change that
    # the function is the inverse of the exponential function in our model
    x = -12 * np.log(1-ui)
    return x;

#this part would be replaced by the random number generator
#print(random_var(generate()))

if __name__=="__main__":
    pass
