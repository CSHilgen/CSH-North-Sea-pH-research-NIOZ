import pandas as pd, numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from scipy.stats import linregress
from scipy.optimize import least_squares
from matplotlib.ticker import FuncFormatter
from matplotlib.dates import MonthLocator, DateFormatter 

#%% # Import datasets

RWSo = pd.read_csv("dataframes_made/RWSo_final.csv")

RWSoCa = RWSo.dropna(axis='rows', how='all', subset=['calcium umol/kg'])

L0 = (RWSoCa.year <= 2014)
L1 = (RWSoCa.year >= 2015) & (RWSoCa.datenum <= 16996.3)
L2 = (RWSoCa.datenum >= 17014.4)  

#%% # Corrected Calcium data based on the methods (Method 1 - 720) - Time - Methods

fig, ax = plt.subplots(dpi=300)

ax = ax
ax.scatter('datenum', 'calcium umol/kg', edgecolors='yellow', facecolors='yellow', data=RWSoCa[L0], s=20, label='Method 1')
ax.scatter('datenum', 'calcium umol/kg', edgecolors='orange', facecolors='orange', data=RWSoCa[L1], s=20, label='Method 2')
ax.scatter('datenum', 'calcium umol/kg', edgecolors='green', facecolors='green', data=RWSoCa[L2], s=20, label='Method 3')

ax.grid(alpha=0.3)
ax.set_xlabel("Time (yrs)")
ax.set_ylabel("Calcium (μmol/kg)")
ax.legend()
# ax.set_ylim(0, 7500)
ax.get_legend().set_title("Dataset")
ax.xaxis.set_major_locator(mdates.YearLocator(1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.YearLocator())

ax.grid(b=True, which='minor', color='grey', linestyle='-', alpha=0.1)
ax.grid(b=True, which='major', color='xkcd:dark grey', linestyle='-', alpha=0.2)
ax.set_title('Calcium RWS - Datasets North Sea')

plt.tight_layout()
plt.savefig("figures/Final_plots/Supplementary_Figure_S2.png")
plt.show()
