def GetRequiredThrust(UEFC, opt_vars, AR, S):

    # YOU SHOULD NOT NEED TO CHANGE THIS FILE FOR THIS PROBLEM
    
    # Calculate the required thrust from UEFC parameters and opt_vars, AR, S
    rho = UEFC.rho
    
    # Calculate CD
    CD = UEFC.drag_coefficient(opt_vars, AR, S)["Total"]
    
    # Calculate q (dynamic pressure)
    V = UEFC.flight_velocity(opt_vars, AR, S)
    q = 0.5*rho*V**2
    
    # Calculate required thrust from CD, q, S
    T = CD*q*S
    
    return T



