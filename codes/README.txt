This file describes how to use the Python aircraft sizing for the UEFC Project. While you can certainly look at any of the provided Python functions, the functions you are most likely to use are briefly described below.

GetUEFC: Contains the class definition for the UEFC aircraft. Most of its attached methods take in a 3-element array called opt_vars, which represents the optimization variables.
	opt_vars[0]: Load factor (-)
	opt_vars[1]: Turn radius (meters)
	opt_vars[2]: Payload mass (grams)

GetCDpay: Sets the payload-dependent drag coefficient increment.  Currently, this is set to zero (i.e. there is no drag caused by the payload).  Clearly, this is almost certainly incorrect and you can include a payload drag increment here.

GetWfuse: Calculates fuselage weight. The constants in here may need to be adjusted to fit your estimated airplane. 

scan_ARS:  This script will search over (AR,S) to determine optimal designs (maximum payload mass x turn rate / b) for each AR,S considered.  Then, it plots contours of obj, mpay, Omega, b, R, CL, T, Tmax, and d/b. An asterick (*) is placed at the location in (AR,S) which has the highest obj.  Finally, scan_ARS also prints out what the performance, operating conditions, weight breakdowns, etc are for this highest obj aircraft.

opt_obj(UEFC,AR,S): this function determines the maximum objective (payload mass x turn rate / wingspan) achievable for an airplane with the inputted values of AR, S.  This function is called repeatedly by scan_ARS as it scans over (AR,S).

report_opt_mO3(UEFC,AR,S): this function is a wrapper for opt_obj.  Calling it will printout the optimized performance, operating conditions, etc found after running opt_obj.  It calls opt_obj for you and then prints out useful information.
