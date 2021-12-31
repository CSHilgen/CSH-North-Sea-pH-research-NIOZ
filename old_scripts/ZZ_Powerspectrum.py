# from scipy import signal
# import pywt
from scipy.fft import fft, fftfreq
from scipy.fft import rfft, rfftfreq
from scipy.fft import irfft
import numpy as np

#%%
x = RWSomean['datenum']
y = RWSomean['chlorophyll']

plt.plot(x, y)
plt.show()

#%% 
duration = 15920 # RWSomean # Days between datenum end - datenum start
sample_rate = 0.03242 # RWSomean # Size of rows (dataframe) / duration

N = int(sample_rate * duration)
normalized_y = np.int16((y / y.max()) * 32767) # Why 16 bit integer? And why 32767?

plt.plot(normalized_y[:1000])
plt.show()

#%%
yf = fft(normalized_y)
xf = fftfreq(N, 1 / sample_rate)

plt.plot(xf, np.abs(yf))
plt.show()

#%%
yf = rfft(normalized_y)
xf = rfftfreq(N, 1 / sample_rate)

plt.plot(xf, np.abs(yf))
plt.show()

#%% # For total_silicate
points_per_freq = len(xf) / (sample_rate / 2)

#Chlorophyll
peak1 = 0.0027 # 370.3703703703703 days
peak1 = 0.0023
peak1= 0.005
peak1=0.0055
peak1=0.0007

#Silicate
#peak1 = 0.0027 # So peak is at 0.0027 Hz 
#peak2 = 0.0028 # 
#peak3 = 0.0055 # 

target_idx = int(points_per_freq * peak1)

#Silicate
# period1 = 1/peak1 # 370.3703703703703 days
# period2 = 1/peak2 # 357.14285714285717 days
# period3 = 1/peak3 # 181.81818181818184 days

yf[target_idx - 1 : target_idx + 2] = 0

plt.plot(xf, np.abs(yf))
plt.show()

#%% # Taking out the peak - filtering

new_sig = irfft(yf)

plt.plot(new_sig[:1000])
plt.show()

# Normalize it - why?
norm_new_sig = np.int16(new_sig * (32767 / new_sig.max())) 