import pandas as pd, numpy as np, xarray as xr
from matplotlib import pyplot as plt
import koolstof as ks
import pickle
import PyCO2SYS as pyco2
import matplotlib.dates as mdates
from cartopy import crs as ccrs, feature as cfeature
import cmocean
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

#%% # Import dataframs

# Initial dataframes are in study area, the wrong data points are dropped
# datetime is created, and distance_to_shore is included
glodapns = pd.read_csv("dataframes_made/glodapns.csv")
socatns = pd.read_csv("dataframes_made/socatns.csv")
mss = pd.read_csv("dataframes_made/mss.csv")
Cefas = pd.read_csv("dataframes_made/Cefas.csv")
D366 = pd.read_csv("dataframes_made/D366.csv")
RWSn = pd.read_csv("dataframes_made/RWSn.csv")
RWSo = pd.read_csv("dataframes_made/RWSo.csv")

# Results are the dataframes of pyCO2sys (all data points)
resultsglodapns = pd.read_csv("dataframes_made/resultsglodapns.csv")
resultssocatnsair = pd.read_csv("dataframes_made/resultssocatnsair.csv")
resultssocatns = pd.read_csv("dataframes_made/resultssocatns.csv")
#resultsmss = pd.read_csv("dataframes_made/resultsmss.csv")
resultsCefas = pd.read_csv("dataframes_made/resultsCefas.csv")
resultsD366 = pd.read_csv("dataframes_made/resultsD366.csv")
resultsD366 = pd.read_csv("dataframes_made/resultsD366.csv")
resultsRWSn = pd.read_csv("dataframes_made/resultsRWSn.csv")
resultsRWSo = pd.read_csv("dataframes_made/resultsRWSo.csv")

# Mean are the dataframes of pyCO2sys (mean per month)
glodapnsmean = pd.read_csv("dataframes_made/glodapnsmean.csv")
socatnsairmean = pd.read_csv("dataframes_made/socatnsairmean.csv")
socatnsmean = pd.read_csv("dataframes_made/socatnsmean.csv")
#mssmean = pd.read_csv("dataframes_made/mssmean.csv")
Cefasmean = pd.read_csv("dataframes_made/Cefasmean.csv")
D366mean = pd.read_csv("dataframes_made/D366mean.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean.csv")
RWSomean = pd.read_csv("dataframes_made/RWSomean.csv")

combined = pd.read_csv("dataframes_made/combined.csv")
resultscombined = pd.read_csv("dataframes_made/resultscombined.csv")
combinedmean = pd.read_csv("dataframes_made/combinedmean.csv")

#%% # Plotting NS longitude latitude and bathymetry

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")

# fvar = socatns

# for fvar in ["Cefas", "D366", "glodapns", "RWSn," "RWSo", "socatns"]: 
    
fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))

ax.coastlines()

ax.scatter("longitude", "latitude", data=RWSo, c='xkcd:aqua',
    transform=ccrs.PlateCarree())

# Plot bathymetry from data
gmin = -150
gmax = 0
cmap = cmocean.cm.topo
cmap = cmocean.tools.crop(cmap, gmin, gmax, 0)

gplot = (gebco.elevation  # take the elevation data
    .coarsen(lon=5, lat=5, boundary="trim").mean()  # reduce its resolution
    .plot(add_colorbar=False, ax=ax, 
        cmap=cmap, transform=ccrs.PlateCarree(), 
        vmin=gmin, vmax=gmax, zorder=-5))

gcbar = plt.colorbar(gplot)
gcbar.set_label("Depth (m)")
gcbar.set_ticks(np.arange(gmin, gmax + 1, 25))
gcbar.set_ticklabels(-gcbar.get_ticks())

# Add more detailed features from NaturalEarthData.com
ax.add_feature(cfeature.NaturalEarthFeature("physical", "land", "10m"), facecolor="k")
ax.add_feature(cfeature.NaturalEarthFeature("physical", "lakes", "10m"), facecolor=cmap(1.0))
ax.add_feature(cfeature.NaturalEarthFeature("physical", "minor_islands", "10m"), facecolor="k")

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.2)#, linestyle='--')
gl.top_labels = False
gl.right_labels = False
# gl.xlines = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
# gl.xlabel_style = {'size': 15, 'color': 'gray'}
# gl.xlabel_style = {'color': 'red', 'weight': 'bold'}

# Plot settings
# ax.set_global()
ax.set_extent((2, 7 , 51, 56.5))  # west, east, south, north limits
# ax.gridlines(alpha=0.3, draw_labels=True)
ax.set_title("RWSo data North Sea")
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.tight_layout()
plt.savefig("figures/Maps/Map_datapoints_and_bathymetry_RWSo.png")
plt.show()

#%% # Plotting NS longitude latitude and bathymetry

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")

fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))

ax.coastlines()

# Scatter northsea from data
smin=0
smax=300

splot = ax.scatter("longitude", "latitude", data=resultssocatns
                   , c='distance_to_shore', cmap='plasma_r',
    transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
scbar = plt.colorbar(splot)
scbar.set_label("Km to shore")
scbar.set_ticks(np.arange(smin, smax + 1, 50))
scbar.set_ticklabels(scbar.get_ticks())
#ax.text(0, 1.05, "(a)", transform=ax.transAxes)

# Plot bathymetry from data
gmin = -150
gmax = 0
cmap = cmocean.cm.topo
cmap = cmocean.tools.crop(cmap, gmin, gmax, 0)

gplot = (gebco.elevation  # take the elevation data
    .coarsen(lon=5, lat=5, boundary="trim").mean()  # reduce its resolution
    .plot(add_colorbar=False, ax=ax, 
        cmap=cmap, transform=ccrs.PlateCarree(), 
        vmin=gmin, vmax=gmax, zorder=-5))

gcbar = plt.colorbar(gplot)
gcbar.set_label("Depth (m)")
gcbar.set_ticks(np.arange(gmin, gmax + 1, 25))
gcbar.set_ticklabels(-gcbar.get_ticks())

# Add more detailed features from NaturalEarthData.com
ax.add_feature(cfeature.NaturalEarthFeature("physical", "land", "10m"), facecolor="k")
ax.add_feature(cfeature.NaturalEarthFeature("physical", "lakes", "10m"), facecolor=cmap(1.0))
ax.add_feature(cfeature.NaturalEarthFeature("physical", "minor_islands", "10m"), facecolor="k")

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.2)#, linestyle='--')
gl.top_labels = False
gl.right_labels = False
# gl.xlines = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
# gl.xlabel_style = {'size': 15, 'color': 'gray'}
# gl.xlabel_style = {'color': 'red', 'weight': 'bold'}

# Plot settings
# ax.set_global()
ax.set_extent((2, 7, 51, 56.5))  # west, east, south, north limits
# ax.gridlines(alpha=0.3, draw_labels=True)
ax.set_title("D366 data North Sea")
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# plt.tight_layout()
#plt.savefig("figures/Maps/Map_datapoints_Km_and_bathymetry_D366.png")


#%% # Plotting NS longitude latitude and bathymetry

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")

fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))

ax.coastlines()

# Scatter northsea from data
smin=6
smax=20

splot = ax.scatter("longitude", "latitude", data=RWSo
                   , c='temperature', cmap='coolwarm',
    transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
scbar = plt.colorbar(splot)
scbar.set_label("Temperature")
scbar.set_ticks(np.arange(smin, smax + 1, 2))
scbar.set_ticklabels(scbar.get_ticks())
#ax.text(0, 1.05, "(a)", transform=ax.transAxes)

# Plot bathymetry from data
gmin = -150
gmax = 0
cmap = cmocean.cm.topo
cmap = cmocean.tools.crop(cmap, gmin, gmax, 0)

gplot = (gebco.elevation  # take the elevation data
    .coarsen(lon=5, lat=5, boundary="trim").mean()  # reduce its resolution
    .plot(add_colorbar=False, ax=ax, 
        cmap=cmap, transform=ccrs.PlateCarree(), 
        vmin=gmin, vmax=gmax, zorder=-5))

gcbar = plt.colorbar(gplot)
gcbar.set_label("Depth (m)")
gcbar.set_ticks(np.arange(gmin, gmax + 1, 25))
gcbar.set_ticklabels(-gcbar.get_ticks())

# Add more detailed features from NaturalEarthData.com
ax.add_feature(cfeature.NaturalEarthFeature("physical", "land", "10m"), facecolor="k")
ax.add_feature(cfeature.NaturalEarthFeature("physical", "lakes", "10m"), facecolor=cmap(1.0))
ax.add_feature(cfeature.NaturalEarthFeature("physical", "minor_islands", "10m"), facecolor="k")

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.2)#, linestyle='--')
gl.top_labels = False
gl.right_labels = False
# gl.xlines = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
# gl.xlabel_style = {'size': 15, 'color': 'gray'}
# gl.xlabel_style = {'color': 'red', 'weight': 'bold'}

# Plot settings
# ax.set_global()
ax.set_extent((2, 7 , 51, 56.5))  # west, east, south, north limits
# ax.gridlines(alpha=0.3, draw_labels=True)
ax.set_title("RWSo data North Sea")
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# plt.tight_layout()
plt.savefig("figures/Maps/Map_datapoints_T_and_bathymetry_RWSo.png")


#%% # pH plots


resultsmss['latitude'] = mss['latitude']
resultsmss['longitude'] = mss['longitude']
resultsD366['latitude'] = D366['latitude']
resultsD366['longitude'] = D366['longitude']
resultsCefas['latitude'] = Cefas['latitude']
resultsCefas['longitude'] = Cefas['longitude']
resultsRWSn['latitude'] = RWSn['latitude']
resultsRWSn['longitude'] = RWSn['longitude']
resultsglodapns['latitude'] = glodapns['latitude']
resultsglodapns['longitude'] = glodapns['longitude']

fig = plt.figure(dpi=300)
ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))

ax.coastlines()

# Scatter northsea from data
smin=7.5
smax=8.5

splot = ax.scatter("longitude", "latitude", data=resultsmss, c='pH', cmap='magma_r',
    transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
splot = ax.scatter("longitude", "latitude", data=resultsD366, c='pH', cmap='magma_r',
    transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
splot = ax.scatter("longitude", "latitude", data=resultsCefas, c='pH', cmap='magma_r',
    transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
splot = ax.scatter("longitude", "latitude", data=resultsRWSn, c='pH', cmap='magma_r',
    transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
splot = ax.scatter("longitude", "latitude", data=resultsglodapns, c='pH', cmap='magma_r',
    transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)

scbar = plt.colorbar(splot)
scbar.set_label("pH")
scbar.set_ticks(np.arange(smin, smax + 1, 0.5))
scbar.set_ticklabels(scbar.get_ticks())
#ax.text(0, 1.05, "(a)", transform=ax.transAxes)

# Add more detailed features from NaturalEarthData.com
ax.add_feature(cfeature.NaturalEarthFeature("physical", "land", "10m"), facecolor="k")
ax.add_feature(cfeature.NaturalEarthFeature("physical", "lakes", "10m"), facecolor="w")
ax.add_feature(cfeature.NaturalEarthFeature("physical", "minor_islands", "10m"), facecolor="k")

gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.2)#, linestyle='--')
gl.top_labels = False
gl.right_labels = False
# gl.xlines = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
# gl.xlabel_style = {'size': 15, 'color': 'gray'}
# gl.xlabel_style = {'color': 'red', 'weight': 'bold'}

# Plot settings
# ax.set_global()
ax.set_extent((-10, 8, 48, 63))  # west, east, south, north limits
# ax.gridlines(alpha=0.3, draw_labels=True)
ax.set_title("pH")
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# plt.tight_layout()
#plt.savefig("figures/Maps/Map_datapoints_S_and_bathymetry_RWSo.png")
