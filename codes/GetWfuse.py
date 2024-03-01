def GetWfuse(UEFC, AR, S):

    # YOU MAY NEED TO ADJUST THE CONSTANTS TO BETTER FIT YOUR ESTIMATED
    # AIRPLANE.  PROBABLY, THIS WOULD INVOLVE SETTING NEW VALUES OF
    # mfusel, mfuseS, b0, and S0
    
    # Calculate fuselage weight from UEFC parameters and S and AR
    mfuse0 = 0.185  # fixed mass (kg)
    mfusel = 0.060  # span (length) dependent mass (kg)
    mfuseS = 0.045  # wing area dependent mass (kg)
    
    S0 = 0.225  # Wing area for which mfusel and mfuseS were calculated (m^2)
    b0 = 1.5    # Wingspan for which mfusel and mfuseS were calculated (m)
    
    b = UEFC.wing_dimensions(AR, S)["Span"]
    
    Wfuse = (mfuse0 + mfusel*b/b0 + mfuseS*S/S0) * UEFC.g
    
    return Wfuse

