import pandas as pd
import tools as HM16_tools
import tools.plots_drivers_pH_seasonality as HM16_plots

#%% # Import dataframes

resultsRWSo = pd.read_csv("dataframes_made/resultsRWSo_final.csv")
resultscombined = pd.read_csv("dataframes_made/resultscombined_final.csv")
resultsRWSn = pd.read_csv("dataframes_made/resultsRWSn_final.csv")

#%% # Getting the mean of the entire period (2000 - 2021)

timeperiod = '2000_2021'
print(timeperiod)
LR = (resultsRWSo['year'] >= 2000)
LC = (resultscombined['year'] >= 2000)

# Function for pH predicted
allparameters = HM16_tools.get_pH_predicted(LR, LC, resultsRWSo, resultscombined)

# Function for cyclic curve
resultsRWSodubbel, allparametersdubbel = HM16_tools.cycliccurve_2000_2021(allparameters, resultsRWSo, LR)

# Function to get the ΔpH winter-to-summer for each individual parameter
HM16_tools.deltapH_winter_summer(allparametersdubbel, resultsRWSodubbel)

# Function to get plot of lines pH predicted, pH fitted, pH due to T, DIC and TA
HM16_plots.get_curve_parameters(allparametersdubbel, resultsRWSodubbel, timeperiod)

# Function to get plot of T, DIC and TA data
Tdata, DICdata, TAdata = HM16_plots.get_T_DIC_TA_curves(allparametersdubbel, allparameters, timeperiod)

# Function to get plot of pH predicted and pH fitted
pH_preddata, pH_fitdata = HM16_plots.get_pHpred_pHfit(allparameters, allparametersdubbel, resultsRWSodubbel, resultsRWSo, LR, timeperiod)

#%% # Getting the mean of the period 2000-2005

timeperiod = '2000_2005'
print(timeperiod)
LR = (resultsRWSo['year'] >= 2000) & (resultsRWSo['year'] <= 2005) 
LC = (resultscombined['year'] >= 2000) & (resultscombined['year'] <= 2005) 

# Function for pH predicted
allparameters = HM16_tools.get_pH_predicted(LR, LC, resultsRWSo, resultscombined)

# Function for cyclic curve
resultsRWSodubbel, allparametersdubbel = HM16_tools.cycliccurve_2000_2005(allparameters, resultsRWSo, LR)

# Function to get the ΔpH winter-to-summer for each individual parameter
HM16_tools.deltapH_winter_summer(allparametersdubbel, resultsRWSodubbel)

# Function to get plot of lines pH predicted, pH fitted, pH due to T, DIC and TA
HM16_plots.get_curve_parameters(allparametersdubbel, resultsRWSodubbel, timeperiod)

# Function to get plot of T, DIC and TA data
Tdata, DICdata, TAdata = HM16_plots.get_T_DIC_TA_curves(allparametersdubbel, allparameters, timeperiod)

# Function to get plot of pH predicted and pH fitted
pH_preddata, pH_fitdata = HM16_plots.get_pHpred_pHfit(allparameters, allparametersdubbel, resultsRWSodubbel, resultsRWSo, LR, timeperiod)

#%% # Getting the mean of the period 2005-2010

timeperiod = '2005_2010'
print(timeperiod)
LR = (resultsRWSo['year'] >= 2005) & (resultsRWSo['year'] <= 2010) 
LC = (resultscombined['year'] >= 2005) & (resultscombined['year'] <= 2010) 

# Function for pH predicted
allparameters = HM16_tools.get_pH_predicted(LR, LC, resultsRWSo, resultscombined)

# Function for cyclic curve
resultsRWSodubbel, allparametersdubbel = HM16_tools.cycliccurve_2005_2010(allparameters, resultsRWSo, LR)

# 'x' must contain at least 2 elements. 

# Function to get the ΔpH winter-to-summer for each individual parameter
# HM16_tools.deltapH_winter_summer(allparametersdubbel, resultsRWSodubbel)

# Function to get plot of lines pH predicted, pH fitted, pH due to T, DIC and TA
# HM16_plots.get_curve_parameters(allparametersdubbel, resultsRWSodubbel, timeperiod)

# Function to get plot of T, DIC and TA data
# Tdata, DICdata, TAdata = HM16_plots.get_T_DIC_TA_curves(allparametersdubbel, allparameters, timeperiod)

# Function to get plot of pH predicted and pH fitted
# HM16_plots.get_pHpred_pHfit(allparameters, allparametersdubbel, resultsRWSodubbel, resultsRWSo, LR, timeperiod)

#%% # Getting the mean of the period 2010-2015

timeperiod = '2010_2015'
print(timeperiod)
LR = (resultsRWSo['year'] >= 2010) & (resultsRWSo['year'] <= 2015) 
LC = (resultscombined['year'] >= 2010) & (resultscombined['year'] <= 2015) 

# Function for pH predicted
allparameters = HM16_tools.get_pH_predicted(LR, LC, resultsRWSo, resultscombined)

# Function for cyclic curve
resultsRWSodubbel, allparametersdubbel = HM16_tools.cycliccurve_2010_2015(allparameters, resultsRWSo, LR)

# Function to get the ΔpH winter-to-summer for each individual parameter
HM16_tools.deltapH_winter_summer(allparametersdubbel, resultsRWSodubbel)

# Function to get plot of lines pH predicted, pH fitted, pH due to T, DIC and TA
HM16_plots.get_curve_parameters(allparametersdubbel, resultsRWSodubbel, timeperiod)

# Function to get plot of T, DIC and TA data
Tdata, DICdata, TAdata = HM16_plots.get_T_DIC_TA_curves(allparametersdubbel, allparameters, timeperiod)

# Function to get plot of pH predicted and pH fitted
pH_preddata, pH_fitdata = HM16_plots.get_pHpred_pHfit(allparameters, allparametersdubbel, resultsRWSodubbel, resultsRWSo, LR, timeperiod)

#%% # Getting the mean of the period 2015-2018

timeperiod = '2015-2018'
print(timeperiod)
LR = (resultsRWSo['year'] >= 2015) & (resultsRWSo['year'] <= 2018) 
LC = (resultscombined['year'] >= 2015) & (resultscombined['year'] <= 2018)  

# Function for pH predicted
allparameters = HM16_tools.get_pH_predicted(LR, LC, resultsRWSo, resultscombined)

# # Function for cyclic curve
resultsRWSodubbel, allparametersdubbel = HM16_tools.cycliccurve_2015_2018(allparameters, resultsRWSo, LR)

# Function to get the ΔpH winter-to-summer for each individual parameter
HM16_tools.deltapH_winter_summer(allparametersdubbel, resultsRWSodubbel)

# Function to get plot of lines pH predicted, pH fitted, pH due to T, DIC and TA
HM16_plots.get_curve_parameters(allparametersdubbel, resultsRWSodubbel, timeperiod)

# Function to get plot of T, DIC and TA data
Tdata, DICdata, TAdata = HM16_plots.get_T_DIC_TA_curves(allparametersdubbel, allparameters, timeperiod)

# Function to get plot of pH predicted and pH fitted
pH_preddata, pH_fitdata = HM16_plots.get_pHpred_pHfit(allparameters, allparametersdubbel, resultsRWSodubbel, resultsRWSo, LR, timeperiod)

#%% # Getting the mean of the period 2018-2021

timeperiod = '2018-2021'
print(timeperiod)
LR = (resultsRWSo['year'] >= 2018)
LC = (resultscombined['year'] >= 2018) 

# Function for pH predicted
allparameters = HM16_tools.get_pH_predicted_RWSn(LR, LC, resultsRWSo, resultscombined, resultsRWSn)

# Function for cyclic curve
resultsRWSodubbel, allparametersdubbel, resultsRWSndubbel = HM16_tools.cycliccurve_2018_2021(allparameters, resultsRWSo, LR, resultsRWSn)

# Function to get the ΔpH winter-to-summer for each individual parameter
HM16_tools.deltapH_winter_summer_RWSn(allparametersdubbel, resultsRWSodubbel, resultsRWSndubbel)

# Function to get plot of lines pH predicted, pH fitted, pH due to T, DIC and TA
HM16_plots.get_curve_parameters_2018_2021(allparametersdubbel, resultsRWSodubbel, resultsRWSndubbel)

# Function to get plot of T, DIC and TA data
Tdata, DICdata, TAdata = HM16_plots.get_T_DIC_TA_curves(allparametersdubbel, allparameters, timeperiod)

# Function to get plot of pH predicted and pH fitted
pH_preddata, pH_fitdata = HM16_plots.get_pHpred_pHfit_2018_2021(allparametersdubbel, resultsRWSndubbel, allparameters, resultsRWSn, timeperiod)


#%% # Getting the column figure of the quantitatitve contribution of drivers of pH seasonal variability

HM16_plots.get_quantitative_contribution()

