# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 13:17:07 2021

CZ4124 Data Visualisation (Tutorial 1 Template)
@author: Chia Zhi Yi
 
"""
from typing import Any

import matplotlib.pyplot as plt
import pandas
import pandas as pd

PlotWithPandas: bool = True  # you can plot either with Pandas or Matplotlib
#---------------------------------------------------------------------
# Read in Daily Temperature datafile into dataframe Temp
#---------------------------------------------------------------------
Temp = pd.read_csv('Daily_Temperature.csv')  # change to your directory
print('\nTable read in\n', Temp, '\n')

#---------------------------------------------------------------------
# Use MELT to covert to long form and apply column names
#---------------------------------------------------------------------
# put in your code here

meltedTemp = Temp.melt(id_vars="Name", var_name="Day", value_name="Temperature")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
meltedTemp["Day"] = pandas.Categorical(meltedTemp["Day"],days)
meltedTemp.sort_values("Day")


# daylist = tempplot['day'].unique()

#---------------------------------------------------------------------
# Use PIVOT to convert to wide form with Names in each column
#---------------------------------------------------------------------
# put in your code here

pivotedTemp = meltedTemp.pivot(index="Day", columns="Name", values="Temperature")



#-------------------------------
# Use Pandas to plot line chart
#-------------------------------
if PlotWithPandas:
    print('\nPlotting with Pandas')
    # put your Pandas plotting code here

    Fig1 = pivotedTemp.plot.line()#x="Day", y="Temperature")
    Fig1.axhline(y=38., xmin=-1, xmax=1, color='r', linestyle='--',lw=2)
    Fig1.axhline(y=37., xmin=-1, xmax=1, color='y', linestyle='--', lw=2)
    plt.show()

    
#----------------------------------
# Use Matplotlib to plot line chart
#----------------------------------
else:  
    print('\nPlotting with Matplotlib')
    # Alternatively, you can do the plot using Matplotlib or 
    # any other Python plotting library

