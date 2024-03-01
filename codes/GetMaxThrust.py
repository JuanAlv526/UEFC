import numpy as np

def GetMaxThrust(UEFC, V):

    # YOU SHOULD NOT NEED TO CHANGE THIS FILE FOR THIS PROBLEM
    rho = UEFC.rho
    
    ct0 =  0.2093
    ct1 = -0.2484
    ct2 = -0.1386
    
    Tmax_static = 1               # Maximum thrust desired at static conditions
    Rprop       = 0.1016          # Propeller radius (m)
    Aprop       = np.pi*Rprop**2  # Propeller disk area
    
    Omega  = np.sqrt(Tmax_static/(0.5*rho*Rprop**2*Aprop*ct0))
    Lambda = V/(Omega*Rprop)  # Advance ratio
    
    CT = ct0 + ct1*Lambda + ct2*Lambda**2 # Thrust coefficient
    
    Tmax = 0.5*rho*(Omega*Rprop)**2*Aprop*CT

    return Tmax
