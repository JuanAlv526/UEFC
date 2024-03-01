#  YOU SHOULD NOT NEED TO CHANGE THIS FILE FOR THIS PROBLEM
from GetUEFC import UEFC
from opt_obj import opt_obj

def report_opt_obj(UEFC, AR, S):
    
    # This function is a wrapper for opt_obj. Calling it will print out the 
    # optimized performance, operating conditions, etc found after running 
    # opt_obj.  It calls opt_obj and then prints out useful information.
    
    opt_vars, obj, success = opt_obj(UEFC, AR, S)
    
    if success:
        
        wing_dimensions = UEFC.wing_dimensions(AR, S)
        
        N    = opt_vars[0]
        R    = opt_vars[1]
        mpay = opt_vars[2]
        
        V     = UEFC.flight_velocity(opt_vars, AR, S)
        Omega = UEFC.turn_rate(opt_vars, AR, S)
        
        print()
        print("Results Summary from opt_obj\n")
        print("obj          = %0.0f g/s/m" % obj)
        print("mpay         = %0.0f g"     % mpay)
        print("R            = %0.2f m"     % R)
        print("V            = %0.2f m/s"   % V)
        print("Omega        = %0.2f rad/s" % Omega)
        print()
        
        print("Geometry")
        print("----------------------------------------------\n")
        print("AR      = %5.3f"       % AR)
        print("S       = %5.3f sq. m" % S)
        print("b       = %5.3f m"     % wing_dimensions["Span"])
        print("cbar    = %5.3f m"     % wing_dimensions["Mean chord"])
        print("cr      = %5.3f m"     % wing_dimensions["Root chord"])
        print("ct      = %5.3f m"     % wing_dimensions["Tip chord"])
        print("lambda  = %5.3f"       % UEFC.taper)
        print("tau     = %5.3f"       % UEFC.tau)
        print("eps     = %5.3f\n"     % UEFC.max_camber())
        
        mass_data = UEFC.mass(opt_vars,AR, S)
        
        print("Masses")
        print("----------------------------------------------\n")
        print("W/g     = %4.0f g"   % mass_data["Total"])
        print("Wfuse/g = %4.0f g"   % mass_data["Breakdown"]["Fuselage"])
        print("Wwing/g = %4.0f g"   % mass_data["Breakdown"]["Wing"])
        print("Wpay/g  = %4.0f g\n" % mass_data["Breakdown"]["Payload"])
        
        CL      = UEFC.lift_coefficient(opt_vars, AR, S)
        CD_data = UEFC.drag_coefficient(opt_vars, AR, S)
        e       = UEFC.span_efficiency( opt_vars, AR, S)
        
        print("Aerodynamic performance")
        print("----------------------------------------------")
        print("N       = %5.3f"   % N)
        print("CL      = %5.3f"   % CL)
        print("CLdes   = %5.3f"   % UEFC.CLdes)
        print("CD      = %5.3f"   % CD_data["Total"])
        print("CDfuse  = %5.3f"   % CD_data["Breakdown"]["Fuselage"])
        print("CDp     = %5.3f"   % CD_data["Breakdown"]["Wing"])
        print("CDi     = %5.3f"   % CD_data["Breakdown"]["Induced"])
        print("CDpay   = %5.3f"   % CD_data["Breakdown"]["Payload"])
        print("e0      = %5.3f"   % UEFC.e0)
        print("e       = %5.3f\n" % e)
    
        T_req = UEFC.required_thrust(opt_vars, AR, S)
        T_max = UEFC.maximum_thrust(V)
        
        print("Thrust")
        print("----------------------------------------------\n")
        print("T       = %5.3f N"   % T_req)   
        print("Tmax    = %5.3f N\n" % T_max)
        
        db = UEFC.wing_tip_deflection(opt_vars, AR, S)
        
        print("Bending")
        print("----------------------------------------------\n")    
        print("d/b     = %5.3f" % db)
        print("d/bmax  = %5.3f" % UEFC.dbmax)
    
    else:
        
        print("\nError in opt_V: success = " + str(success))
        print("  Usually this is because the airplane could not fly while " +
              "meeting all constraints.\n")
    
    return
        

if __name__ == "__main__":
    
    # Simple test case. Feel free to modify this part of the file.
    aircraft = UEFC()

    #AR = 10.1
    #S  = 0.228  # m^2

    AR = 11
    S  = 0.3  # m^2

    report_opt_obj(aircraft, AR, S)
