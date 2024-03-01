import numpy as np

def GetCD(UEFC, opt_vars, AR, S):

    # YOU SHOULD NOT NEED TO CHANGE THIS FILE FOR THIS PROBLEM
    tau      = UEFC.tau
    dihedral = (np.pi/180) * UEFC.dihedral  # Convert to radians
    
    # Determine profile drag (function of CL, tau, Re)
    cd0    = 0.020*(1+tau**2)
    cd1    = -0.005/(1+6*tau)
    cd2    = 0.160/(1+60*tau)
    cd8    = 1.0
    cl0    = 1.25 - 3*tau
    Re_ref = 1E5
    Re_a   = -0.75
    
    CL   = UEFC.lift_coefficient(opt_vars, AR, S)
    V    = UEFC.flight_velocity(opt_vars, AR, S)
    cbar = UEFC.wing_dimensions(AR, S)["Mean chord"]
    Re   = (UEFC.rho * V * cbar) / UEFC.mu  # Reynolds number
    
    cl2d   = CL/np.cos(dihedral)
    cdpfac = cd0 + cd1*(cl2d-cl0) + cd2*(cl2d-cl0)**2 + cd8*(cl2d-cl0)**8
    CDp    = (cdpfac*(Re/Re_ref)**Re_a)/np.cos(dihedral)
    
    # Fuselage drag model including S-dependence (calibrated to Plane Vanilla)
    SPV       = 0.225
    CDA_fuse0 = 0.002
    CDA_fuseS = 0.002
    
    CDA0   = CDA_fuse0 + CDA_fuseS*S/SPV
    CDfuse = CDA0/S
    
    # Calculate induced drag coefficient
    e   = UEFC.span_efficiency(opt_vars, AR, S)
    CDi = (CL**2)/(np.pi*AR*e)
    
    # Calculate payload drag coefficient increment
    CDpay = UEFC.payload_drag_coefficient(opt_vars, AR, S)
    
    # Total drag coefficient
    CD = CDfuse + CDp + CDi + CDpay
    
    return {
            "Total": CD,
            "Breakdown": {
                    "Fuselage": CDfuse,
                    "Wing":     CDp,
                    "Payload":  CDpay,
                    "Induced":  CDi,
                    }
            }
            