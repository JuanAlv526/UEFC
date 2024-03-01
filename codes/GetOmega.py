def GetOmega(UEFC, opt_vars, AR, S):
    
    # YOU SHOULD NOT NEED TO CHANGE THIS FILE FOR THIS PROBLEM
    
    # Calculate the turn rate (in rad/s) from UEFC parameters and (opt_vars, 
    # AR, S)
    
    R = opt_vars[1]
    V = UEFC.flight_velocity(opt_vars, AR, S)
    
    Omega = V / R  # Turn rate (rad/s)
    
    return Omega
