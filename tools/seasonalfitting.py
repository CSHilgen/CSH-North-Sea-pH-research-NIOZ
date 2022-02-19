# Seasonal curve tools


def seasonalcycle_fit(coeffs, datenum):
    """Function 1 to make the seasonal cycle (sin curve)""" 
    import numpy as np
    
    slope, intercept, sine_stretch, sine_shift = coeffs
    seasonalcycle = datenum * slope + intercept + sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    
    return seasonalcycle

def lsq_seasonalcycle_fit(coeffs, datenum, seasonalcycle):
    """Function 2 to make the seasonal cycle (sin curve)"""
    return seasonalcycle_fit(coeffs, datenum) - seasonalcycle

def seasonalcycle_fit_T(coeffs, datenum):
    """Function 1 to make the seasonal cycle (sin curve) only for temperature""" 
    import numpy as np
        
    slope, intercept, sine_stretch, sine_shift = coeffs
    seasonalcycle = datenum * slope + intercept + sine_stretch * (np.sin((- datenum - sine_shift) * 2 *np.pi / 365.25))
    return seasonalcycle

def lsq_seasonalcycle_fit_T(coeffs, datenum, seasonalcycle):
    """Function 2 to make the seasonal cycle (sin curve) only for temperature""" 
    return seasonalcycle_fit_T(coeffs, datenum) - seasonalcycle

def seasonalcycle_fit_fco2_sea(coeffs, datenum):
    """Function 1 to make the seasonal cycle (sin curve) only for fCO2 sea""" 
    import numpy as np
    
    slope, intercept, sine_stretch, sine_shift = coeffs
    seasonalcycle = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    
    return seasonalcycle

def lsq_seasonalcycle_fit_fco2_sea(coeffs, datenum, seasonalcycle):
    """Functions 2 to make the seasonal cycle (sin curve) only for fCO2 sea""" 
    return seasonalcycle_fit_fco2_sea(coeffs, datenum) - seasonalcycle
