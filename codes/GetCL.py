def GetCL(UEFC, opt_vars, AR, S):

    # YOU SHOULD NOT NEED TO CHANGE THIS FILE FOR THIS PROBLEM
    
    # Calculate the lift coefficient from UEFC parameters and opt_vars, AR, S    
    rho = UEFC.rho
    N   = opt_vars[0]
    
    V  = UEFC.flight_velocity(opt_vars, AR, S)
    W  = UEFC.weight(opt_vars, AR, S)["Total"]
    CL = (N*W) / (0.5*rho*S*V**2)
    
    return CL
