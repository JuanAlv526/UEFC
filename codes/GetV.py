import numpy as np

def GetV(UEFC, opt_vars, AR, S):

    # YOU SHOULD NOT NEED TO CHANGE THIS FILE FOR THIS PROBLEM
    
    # Calculate speed from N, g, R during a level turn. 
    # N = load factor = Lift / Weight.
    g = UEFC.g
    N = opt_vars[0]
    R = opt_vars[1]
    
    V = np.sqrt(R*g*np.sqrt(N**2-1))  # Holds in a level turn
    
    return V
