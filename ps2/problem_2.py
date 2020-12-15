import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, ks_2samp
import os
local_path=os.path.expanduser("~/Downloads")
meters = pd.read_csv("meter-readings-small_DOWNLOADED.csv", thousands=',')

#Part A
'''
diff() function finds first difference across each row. Separates non-numerical information from energy readings and re-concatenates them
'''
houses = meters[meters.columns[:10]][:]
difference = meters[meters.columns[10:]][:].diff(axis = 1) #Find first difference
difference[difference < 0] = np.NaN   #Replaces negative differences with NaN in order to ignore them in future calculations
res = pd.concat([houses, difference], axis = 1)

#Part B
'''
Selects 12-month period and separates building readings, then calculates row means and performs t test and K-S test on means
'''
year_usage = pd.concat([houses, res[res.columns[16:28]][:]], axis = 1)            #Selects 12 month period
saw = year_usage[year_usage['Building'] == "Sawtelle"]
saw_mean = saw[saw.columns[10:22]][:].mean(axis = 1, skipna = True)                #Finds row means for Sawtelle
sepul = year_usage[year_usage['Building'] == "Sepulveda"]
sepul_mean= sepul[sepul.columns[10:22]][:].mean(axis = 1, skipna = True)            #Finds row means for Sepulveda
print("p-value of t-test between Sawtelle and Sepulveda: " + str(ttest_ind(saw_mean, sepul_mean)[1]))                                            #Results of statistical tests
print("p-value of K-S-test between Sawtelle and Sepulveda: " + str(ks_2samp(saw_mean, sepul_mean)[1]))

#Part C
'''
Separates readings by number of maximum occupants now and performs t test
'''
four_occ = res[res['MaxOccupants'] == 4]        #Filters by max occupants
six_occ = res[res['MaxOccupants'] == 6]
f_mean = four_occ[four_occ.columns[10:58]][:].mean(axis = 1, skipna = True)  #Calculates row means
s_mean = six_occ[six_occ.columns[10:58]][:].mean(axis = 1, skipna = True)
print("p-value of t-test between 4 occupant apartments and 6 occupant apartments: " + str(ttest_ind(f_mean, s_mean)[1]))                                                #Performs t-test

#Part D
'''
Separates readings randomly by approximately half and performs t test
'''
msk = np.random.rand(len(year_usage)) <= 0.5                                            #Generates column of values between 0 and 1 and new boolean column that checks whether random values is less than 0.5
control = year_usage[msk]                                                               #Separates based on boolean column
treatment = year_usage[~msk]
control_mean = control[control.columns[10:58]][:].mean(axis = 1, skipna = True)         #Calculates row means
treatment_mean = treatment[treatment.columns[10:58]][:].mean(axis = 1, skipna = True)
print("p-value of t-test of random assignment: " + str(ttest_ind(control_mean, treatment_mean)[1]))                                          #Performs t-test


