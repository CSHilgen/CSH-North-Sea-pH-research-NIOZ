# Seasonal curve tools

# Functions to make the seasonal cycle (sin curve)
def seasonalcycle_fit(coeffs, datenum):
    import numpy as np
    
    slope, intercept, sine_stretch, sine_shift = coeffs
    seasonalcycle = datenum * slope + intercept + sine_stretch * np.abs(np.sin((datenum - sine_shift) * np.pi / 365.25))
    
    return seasonalcycle

def lsq_seasonalcycle_fit(coeffs, datenum, seasonalcycle):
    
    return seasonalcycle_fit(coeffs, datenum) - seasonalcycle

# Functions to make the seasonal cycle (sin curve) - only for temperature
def seasonalcycle_fit_T(coeffs, datenum):
    import numpy as np
        
    slope, intercept, sine_stretch, sine_shift = coeffs
    seasonalcycle = datenum * slope + intercept + sine_stretch * (np.sin((- datenum - sine_shift) * 2 *np.pi / 365.25))
    return seasonalcycle

def lsq_seasonalcycle_fit_T(coeffs, datenum, seasonalcycle):
    return seasonalcycle_fit_T(coeffs, datenum) - seasonalcycle

def seasonalcycle_fit_fco2_sea(coeffs, datenum):
    import numpy as np
    
    slope, intercept, sine_stretch, sine_shift = coeffs
    seasonalcycle = datenum * slope + intercept + sine_stretch * np.abs(np.sin((- datenum - sine_shift) * np.pi / 365.25))
    
    return seasonalcycle

def lsq_seasonalcycle_fit_fco2_sea(coeffs, datenum, seasonalcycle):
    
    return seasonalcycle_fit_fco2_sea(coeffs, datenum) - seasonalcycle
