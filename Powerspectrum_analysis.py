# from scipy import signal
# import pywt
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq
from scipy.fft import irfft
import numpy as np
import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

#%% # Import datasets

sunspot = pd.io.json.read_json('data_sun_spots/observed-solar-cycle-indices-1.json')
RWStotal = pd.read_csv("dataframes_made/RWStotal_final.csv")
RWSo = pd.read_csv("dataframes_made/RWSo_final.csv")
combined = pd.read_csv("dataframes_made/combined_final.csv")
socatns = pd.read_csv("dataframes_made/socatns_final.csv")

#%% # For RWS dataset 1975-2018

variable = 'pH'

for variable in ['pH', 'aou', 'oxygen umol/kg', 'chlorophyll', 'ammonia', 'phosphate', 'silicate', 'nitrate', 'calcium']:

    selecteddf = RWSo.dropna(axis='rows', how='all', subset=[variable])
    
    x = selecteddf['datenum']
    y = selecteddf[variable]
    
    plt.plot(x, y)
    plt.show()
    
    duration = (x.max() - x.min()) # RWSomean # Days between datenum end - datenum start
    sample_rate = (y.size/duration) # RWSomean # Size of rows (dataframe) / duration
    
    N = int(sample_rate * duration)
    normalized_y = np.int16((y / y.max()) * 32767) # Why 16 bit integer? And why 32767?
    
    plt.plot(normalized_y[:1000])
    plt.show()

    yf = fft(normalized_y)
    xf = fftfreq(N, 1 / sample_rate)
    
    plt.plot(xf, np.abs(yf))
    plt.show()
    
    yf = rfft(normalized_y)
    xf = rfftfreq(N, 1 / sample_rate)
    
    plt.plot(xf, np.abs(yf))
    plt.show()
    
    df = pd.DataFrame(data=xf, columns=['peak'])
    df['y'] = np.abs(yf)
    df['period_days'] = (1 / df['peak']) 
    df['period_years'] = (df['period_days'] / 365)
    
    print(str(variable))
    df.sort_values(by='y', inplace=True, ascending=False)
    print(df['period_years'].head(5))

#%% # For RWS dataset 1975-2021

variable = 'temperature'

for variable in ['temperature', 'salinity']:
    
    selecteddf = RWStotal.dropna(axis='rows', how='all', subset=[variable])
    
    x = selecteddf['datenum']
    y = selecteddf[variable]
    
    plt.plot(x, y)
    plt.show()
    
    duration = (x.max() - x.min()) # RWSomean # Days between datenum end - datenum start
    sample_rate = (y.size/duration) # RWSomean # Size of rows (dataframe) / duration
    
    N = int(sample_rate * duration)
    normalized_y = np.int16((y / y.max()) * 32767) # Why 16 bit integer? And why 32767?
    
    plt.plot(normalized_y[:1000])
    plt.show()

    yf = fft(normalized_y)
    xf = fftfreq(N, 1 / sample_rate)
    
    plt.plot(xf, np.abs(yf))
    plt.show()

    yf = rfft(normalized_y)
    xf = rfftfreq(N, 1 / sample_rate)
    
    plt.plot(xf, np.abs(yf))
    plt.show()
    
    df = pd.DataFrame(data=xf, columns=['peak'])
    df['y'] = np.abs(yf)
    df['period_days'] = (1 / df['peak']) 
    df['period_years'] = (df['period_days'] / 365)
    
    print(str(variable))
    df.sort_values(by='y', inplace=True, ascending=False)
    print(df['period_years'].head(5))
    
#%% # For combined dataset 

variable = 'alkalinity'

for variable in ['TA', 'DIC']:
    
    selecteddf = combined.dropna(axis='rows', how='all', subset=[variable])
    
    x = selecteddf['datenum']
    y = selecteddf[variable]
    
    plt.plot(x, y)
    plt.show()
    
    duration = (x.max() - x.min()) # RWSomean # Days between datenum end - datenum start
    sample_rate = (y.size/duration) # RWSomean # Size of rows (dataframe) / duration
    
    N = int(sample_rate * duration)
    normalized_y = np.int16((y / y.max()) * 32767) # Why 16 bit integer? And why 32767?
    
    plt.plot(normalized_y[:1000])
    plt.show()

    yf = fft(normalized_y)
    xf = fftfreq(N, 1 / sample_rate)
    
    plt.plot(xf, np.abs(yf))
    plt.show()

    yf = rfft(normalized_y)
    xf = rfftfreq(N, 1 / sample_rate)
    
    plt.plot(xf, np.abs(yf))
    plt.show()
    
    df = pd.DataFrame(data=xf, columns=['peak'])
    df['y'] = np.abs(yf)
    df['period_days'] = (1 / df['peak']) 
    df['period_years'] = (df['period_days'] / 365)
    
    print(str(variable))
    df.sort_values(by='y', inplace=True, ascending=False)
    print(df['period_years'].head(5))
    
#%% # For SOCAT dataset

variable = 'gvco2'

for variable in ['gvco2', 'fco2_recommended']:
    
    selecteddf = socatns.dropna(axis='rows', how='all', subset=[variable])
    
    x = selecteddf['datenum']
    y = selecteddf[variable]
    
    plt.plot(x, y)
    plt.show()
    
    duration = (x.max() - x.min()) # RWSomean # Days between datenum end - datenum start
    sample_rate = (y.size/duration) # RWSomean # Size of rows (dataframe) / duration
    
    N = int(sample_rate * duration)
    normalized_y = np.int16((y / y.max()) * 32767) # Why 16 bit integer? And why 32767?
    
    plt.plot(normalized_y[:1000])
    plt.show()

    yf = fft(normalized_y)
    xf = fftfreq(N, 1 / sample_rate)
    
    plt.plot(xf, np.abs(yf))
    plt.show()

    yf = rfft(normalized_y)
    xf = rfftfreq(N, 1 / sample_rate)
    
    plt.plot(xf, np.abs(yf))
    plt.show()
    
    df = pd.DataFrame(data=xf, columns=['peak'])
    df['y'] = np.abs(yf)
    df['period_days'] = (1 / df['peak']) 
    df['period_years'] = (df['period_days'] / 365)
    
    print(str(variable))
    df.sort_values(by='y', inplace=True, ascending=False)
    print(df['period_years'].head(5))

#%% # For NOAA Sunspot cycle

sunspot['datetime'] = pd.to_datetime(sunspot['time-tag'])
sunspot['datenum'] = mdates.date2num(sunspot.datetime)

variable = 'ssn'

for variable in ['ssn']:
    
    selecteddf = sunspot.dropna(axis='rows', how='all', subset=[variable])
    
    x = selecteddf['datenum']
    y = selecteddf[variable]
    
    plt.plot(x, y)
    plt.show()
    
    duration = (x.max() - x.min()) # RWSomean # Days between datenum end - datenum start
    sample_rate = (y.size/duration) # RWSomean # Size of rows (dataframe) / duration
    
    N = int(sample_rate * duration)
    normalized_y = np.int16((y / y.max()) * 32767) # Why 16 bit integer? And why 32767?
    
    plt.plot(normalized_y[:1000])
    plt.show()

    yf = fft(normalized_y)
    xf = fftfreq(N, 1 / sample_rate)
    
    plt.plot(xf, np.abs(yf))
    plt.show()

    yf = rfft(normalized_y)
    xf = rfftfreq(N, 1 / sample_rate)
    
    plt.plot(xf, np.abs(yf))
    plt.show()
    
    df = pd.DataFrame(data=xf, columns=['peak'])
    df['y'] = np.abs(yf)
    df['period_days'] = (1 / df['peak']) 
    df['period_years'] = (df['period_days'] / 365)
    
    print(str(variable))
    df.sort_values(by='y', inplace=True, ascending=False)
    print(df['period_years'].head(5))
