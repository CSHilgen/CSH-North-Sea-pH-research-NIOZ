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

RWSomean = pd.read_csv("dataframes_made/RWSomean_final.csv")
RWSnmean = pd.read_csv("dataframes_made/RWSnmean_final.csv")
D366mean = pd.read_csv("dataframes_made/D366mean_final.csv")
Cefasmean = pd.read_csv("dataframes_made/Cefasmean_final.csv")
socatnsmean = pd.read_csv("dataframes_made/socatnsmean_final.csv")
glodapnsmean = pd.read_csv("dataframes_made/glodapnsmean_final.csv")

resultsRWSo = pd.read_csv("dataframes_made/resultsRWSo_final.csv")
resultsRWSn = pd.read_csv("dataframes_made/resultsRWSn_final.csv")
resultsD366 = pd.read_csv("dataframes_made/resultsD366_final.csv")
resultsCefas = pd.read_csv("dataframes_made/resultsCefas_final.csv")
resultsglodapns = pd.read_csv("dataframes_made/resultsglodapns_final.csv")

#%% # Plotting NS longitude latitude and bathymetry DATASETS

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")
fvarr = [Cefas, D366, glodapns, RWSn, RWSo, socatns]
colourr = ["xkcd:greenish", "xkcd:neon pink", "xkcd:blue", "xkcd:dark aqua", "xkcd:aqua", "xkcd:goldenrod"]
datasett = ['CEFAS data', 'D366 data', 'GLODAP data', 'RWSn data', 'RWSo data', 'SOCAT data']

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
    ax.set_title(dataset + " North Sea")
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    
    plt.tight_layout()
    plt.savefig("figures/Maps/Maps_" + dataset + ".png")

#%% # Plotting NS longitude latitude and bathymetry REGIONS

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")
fvarr = [Cefasmean, D366mean, glodapnsmean, RWSnmean, RWSomean, socatnsmean]
datasett = ['CEFAS data', 'D366 data', 'GLODAP data', 'RWSn data', 'RWSo data', 'SOCAT data']

for fvar, dataset in zip(fvarr, datasett): 
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))
    
    ax.coastlines()
    
    # Scatter northsea from data
    smin=0
    smax=300
    
    splot = ax.scatter("longitude", "latitude", data=fvar, edgecolors='xkcd:dark grey', 
                       linewidth=0.001, s=35, c='distance_to_shore', cmap='viridis_r',
        transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
    scbar = plt.colorbar(splot)
    scbar.set_label("Km to shore")
    scbar.set_ticks(np.arange(smin, smax + 1, 50))
    scbar.set_ticklabels(scbar.get_ticks())
    #ax.text(0, 1.05, "(a)", transform=ax.transAxes)
    
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
    ax.set_title(dataset + " Mean North Sea")
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    
    plt.tight_layout()
    plt.savefig("figures/Maps/Maps_mean_regions_" + dataset + ".png")

#%% # Plotting NS longitude latitude and bathymetry TEMPERATURE

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")
fvarr = [D366mean, glodapnsmean, RWSnmean, RWSomean, socatnsmean]
datasett = ['D366 data', 'GLODAP data', 'RWSn data', 'RWSo data', 'SOCAT data']

for fvar, dataset in zip(fvarr, datasett): 
    
    fig = plt.figure(dpi=300)
    
    ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))
    
    ax.coastlines()
    
    # Scatter northsea from data
    smin=6
    smax=20
    
    splot = ax.scatter("longitude", "latitude", data=fvar, edgecolors='none', 
                       linewidth=0.01, s=35, c='temperature', cmap='coolwarm',
        transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
    scbar = plt.colorbar(splot)
    scbar.set_label("Temperature (°C)")
    scbar.set_ticks(np.arange(smin, smax + 1, 2))
    scbar.set_ticklabels(scbar.get_ticks())
    #ax.text(0, 1.05, "(a)", transform=ax.transAxes)
    
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
    ax.set_title(dataset + " Mean North Sea")
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    
    plt.tight_layout()
    plt.savefig("figures/Maps/Maps_mean_temperature_" + dataset + ".png")

#%% # Plotting NS longitude latitude and bathymetry SALINITY

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")
fvarr = [D366mean, glodapnsmean, RWSnmean, RWSomean, socatnsmean]
datasett = ['D366 data', 'GLODAP data', 'RWSn data', 'RWSo data', 'SOCAT data']

for fvar, dataset in zip(fvarr, datasett): 
    
    fig = plt.figure(dpi=300)
    
    ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))
    
    ax.coastlines()
    
    # Scatter northsea from data
    smin=31
    smax=36
    
    splot = ax.scatter("longitude", "latitude", data=fvar, edgecolors='none', 
                       linewidth=0.01, s=35, c='salinity', cmap='magma_r',
        transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
    scbar = plt.colorbar(splot)
    scbar.set_label("Salinity")
    scbar.set_ticks(np.arange(smin, smax + 1, 1))
    scbar.set_ticklabels(scbar.get_ticks())
    #ax.text(0, 1.05, "(a)", transform=ax.transAxes)
    
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
    ax.set_title(dataset + " Mean North Sea")
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    
    plt.tight_layout()
    plt.savefig("figures/Maps/Maps_mean_salinity_" + dataset + ".png")
    
#%% # Plotting NS longitude latitude and bathymetry pH 

gebco = xr.open_dataset("data_North_Sea/gebco_2020_noordzee.nc")
fvarr = [resultsCefas, resultsD366, resultsglodapns, resultsRWSn, resultsRWSo]
datasett = ['CEFAS data', 'D366 data', 'GLODAP data', 'RWSn data', 'RWSo data']

for fvar, dataset in zip(fvarr, datasett): 
    
    fig = plt.figure(dpi=300)
    ax = fig.add_subplot(projection=ccrs.Robinson(central_longitude=0))
    
    ax.coastlines()
    
    # Scatter northsea from data
    smin=7.8
    smax=8.4
    
    splot = ax.scatter("longitude", "latitude", data=fvar, c='pH_total', cmap='plasma_r',
          transform=ccrs.PlateCarree(), vmin=smin, vmax=smax, zorder=10)
    
    scbar = plt.colorbar(splot)
    scbar.set_label("pH")
    scbar.set_ticks(np.arange(smin, smax + 1, 0.2))
    scbar.set_ticklabels(scbar.get_ticks())
    #ax.text(0, 1.05, "(a)", transform=ax.transAxes)

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
    ax.set_title(dataset + " North Sea")
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    
    plt.tight_layout()
    plt.savefig("figures/Maps/Maps_pH_" + dataset + ".png")
