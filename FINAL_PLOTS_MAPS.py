import pandas as pd, numpy as np, xarray as xr
from matplotlib import pyplot as plt
from cartopy import crs as ccrs, feature as cfeature
import cmocean
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

#%% # Import datasets

RWSo = pd.read_csv("dataframes_made/RWSo_final.csv")
RWSn = pd.read_csv("dataframes_made/RWSn_final.csv")
D366 = pd.read_csv("dataframes_made/D366_final.csv")
Cefas = pd.read_csv("dataframes_made/Cefas_final.csv")
socatns = pd.read_csv("dataframes_made/socatns_final.csv")
glodapns = pd.read_csv("dataframes_made/glodapns_final.csv")

#%% # Plotting NS longitude latitude and bathymetry DATASETS

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")
fvarr = [Cefas, D366, glodapns, RWSn, RWSo, socatns]
colourr = ["xkcd:greenish", "xkcd:neon pink", "xkcd:blue", "xkcd:dark aqua", "xkcd:aqua", "xkcd:goldenrod"]
datasett = ['CEFAS', 'D366', 'GLODAP', 'RWS (2018-2021)', 'RWS (1975-2018)', 'SOCAT']

for fvar, colour, dataset in zip(fvarr, colourr, datasett): 

    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))
    
    ax.coastlines()
    
    ax.scatter("longitude", "latitude", data=fvar, facecolors=colour, 
               edgecolors='xkcd:dark grey', linewidth=0.08, s=35, 
               transform=ccrs.PlateCarree(), label=dataset)
    
    # Plot bathymetry from data
    gmin = -100
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
    # ax.add_feature(cfeature.NaturalEarthFeature("physical", "land", "10m"), facecolor="xkcd:light orange", edgecolor='black')
    ax.add_feature(cfeature.NaturalEarthFeature("cultural", "admin_0_countries_nld", "10m"), facecolor='xkcd:dark grey', edgecolor="xkcd:black")
    ax.add_feature(cfeature.NaturalEarthFeature("physical", "lakes", "10m"), facecolor=cmap(1.0))
    ax.add_feature(cfeature.NaturalEarthFeature("physical", "minor_islands", "10m"), facecolor="k", edgecolor='black')
    # ax.add_feature(cfeature.NaturalEarthFeature("cultural", "urban_areas", "10m"), facecolor="xkcd:dark orange")
    ax.add_feature(cfeature.NaturalEarthFeature("physical", "rivers_lake_centerlines", "10m"), edgecolor=cmap(0.5), facecolor="none")
    
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
    ax.set_extent((0, 8, 51, 57))  # west, east, south, north limits
    # ax.gridlines(alpha=0.3, draw_labels=True)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig("figures/Final_plots/Maps_" + dataset + ".png")
    
#%% # Plotting NS longitude latitude and bathymetry DATASETS MEAN

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")
fvarr = [Cefasmean, D366mean, glodapnsmean, RWSnmean, RWSomean, socatnsmean]
colourr = ["xkcd:greenish", "xkcd:neon pink", "xkcd:blue", "xkcd:dark aqua", "xkcd:aqua", "xkcd:goldenrod"]
datasett = ['CEFAS$_{mean}$', 'D366$_{mean}$', 'GLODAP$_{mean}$', 'RWS$_{mean}$ (2018-2021)', 'RWS$_{mean}$ (1975-2018)', 'SOCAT$_{mean}$']

for fvar, colour, dataset in zip(fvarr, colourr, datasett): 

    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))
    
    ax.coastlines()
    
    ax.scatter("longitude", "latitude", data=fvar, facecolors=colour, 
               edgecolors='xkcd:dark grey', linewidth=0.08, s=35, 
               transform=ccrs.PlateCarree(), label=dataset)
    
    # Plot bathymetry from data
    gmin = -100
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
    # ax.add_feature(cfeature.NaturalEarthFeature("physical", "land", "10m"), facecolor="xkcd:light orange", edgecolor='black')
    ax.add_feature(cfeature.NaturalEarthFeature("cultural", "admin_0_countries_nld", "10m"), facecolor='xkcd:dark grey', edgecolor="xkcd:black")
    ax.add_feature(cfeature.NaturalEarthFeature("physical", "lakes", "10m"), facecolor=cmap(1.0))
    ax.add_feature(cfeature.NaturalEarthFeature("physical", "minor_islands", "10m"), facecolor="k", edgecolor='black')
    # ax.add_feature(cfeature.NaturalEarthFeature("cultural", "urban_areas", "10m"), facecolor="xkcd:dark orange")
    ax.add_feature(cfeature.NaturalEarthFeature("physical", "rivers_lake_centerlines", "10m"), edgecolor=cmap(0.5), facecolor="none")
    
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
    ax.set_extent((0, 8, 51, 57))  # west, east, south, north limits
    # ax.gridlines(alpha=0.3, draw_labels=True)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig("figures/Final_plots/Maps_mean_" + dataset + ".png")