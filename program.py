# -*- coding: utf-8 -*-
"""
@author: Favas
"""

#Package import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#File read function
def file_read(f_name):
    """
        A function that takes a filename, and reads it and loads it into two dataframes. One normal and one transposed
    """

    df = pd.read_excel(f_name)
    df_transposed = pd.DataFrame.transpose(df)
    return(df, df_transposed)

#Reads the files
df_forest_total,df_forest_countries = file_read("Forest area.xls")
df_pop_total,df_pop_countries = file_read("Population growth.xls")
df_urban_total,df_urban_countries = file_read("Urban population.xls")
df_agri_total,df_agri_countries = file_read("Agricultural Land.xls")


"""

Bar Graph 1
Creating bar graph of energyused by mutiple countries from 1990-2014
"""



#Header
header = df_forest_countries.iloc[0].values.tolist()
df_forest_countries.columns = header

#Data Processing
df_forest_countries = df_forest_countries.iloc[1:]
df_forest_countries = df_forest_countries.iloc[11:55]

#Index Processing
df_forest_countries.index = df_forest_countries.index.astype(int)
df_forest_countries = df_forest_countries[df_forest_countries.index>1989]

#removing empty columns
df_forest_countries = df_forest_countries.dropna(axis = 'columns')

#List of countries to use in the plot
countries =['United Arab Emirates', 'Australia','Spain', 'France', 'United Kingdom', 'India', 'Somalia', 'United States']

df_forest_time = pd.DataFrame.transpose(df_forest_countries)

#These years will be taken for the graphs
years = [1990, 1995, 2000, 2005, 2010, 2014]

#Creating new dataframe with only required data
df_forest_subset_time = df_forest_time[years].copy()
df_forest_subset_time = df_forest_subset_time.loc[df_forest_subset_time.index.isin(countries)]

#Bar Plot
n=8
k=np.arange(n)
width= 0.1
plt.bar(k-0.3, df_forest_subset_time[1990], color = 'indianred',width = width, edgecolor = 'black',label='1990')
plt.bar(k-0.2, df_forest_subset_time[1995], color = 'lightsalmon',width = width, edgecolor = 'black',label='1995')
plt.bar(k-0.1, df_forest_subset_time[2000], color = 'orange',width = width, edgecolor = 'black',label='2000')
plt.bar(k, df_forest_subset_time[2005], color = 'red',width = width, edgecolor = 'black',label='2005')
plt.bar(k+0.1, df_forest_subset_time[2010], color = 'pink',width = width, edgecolor = 'black',label='2010')
plt.bar(k+0.2, df_forest_subset_time[2014], color = 'orange',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("Forest Area")
plt.xticks(width+k, countries, rotation = 70)
plt.legend()
plt.title("Forest area (% of land area)")
plt.savefig("Forest.png", dpi=300, bbox_inches='tight')
plt.show()

"""
Population growth shown through bar graph
Creating bar graph of population growth
"""

header = df_pop_countries.iloc[0].values.tolist()
df_pop_countries.columns = header

#Cleaning the dataframe

df_pop_countries = df_pop_countries.iloc[1:]
df_pop_countries = df_pop_countries.iloc[11:55]

df_pop_countries.index = df_pop_countries.index.astype(int)
df_pop_countries = df_pop_countries[df_pop_countries.index>1989]

df_pop_countries = df_pop_countries.dropna(axis = 'columns')

df_pop_time = pd.DataFrame.transpose(df_pop_countries)
years = [1990, 1995, 2000, 2005, 2010, 2014]
df_pop_subset_time = df_pop_time[years].copy()
df_pop_subset_time = df_pop_subset_time.loc[df_pop_subset_time.index.isin(countries)]

#plotting the data
plt.bar(k-0.3, df_pop_subset_time[1990], color = 'gold',width = width, edgecolor = 'black',label='1990')
plt.bar(k-0.2, df_pop_subset_time[1995], color = 'yellow',width = width, edgecolor = 'black',label='1995')
plt.bar(k-0.1, df_pop_subset_time[2000], color = 'darkkhaki',width = width, edgecolor = 'black',label='2000')
plt.bar(k, df_pop_subset_time[2005], color = 'plum',width = width, edgecolor = 'black',label='2005')
plt.bar(k+0.1, df_pop_subset_time[2010], color = 'fuchsia',width = width, edgecolor = 'black',label='2010')
plt.bar(k+0.2, df_pop_subset_time[2014], color = 'indigo',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("Population growth")
plt.xticks(width+k, countries, rotation = 45)
plt.legend()
plt.title("Population growth (annual %)")
plt.savefig("Population.png", dpi=300, bbox_inches='tight')
plt.show()


"""
Renewable bar graph
Creates a bar chart of renewale energy consumption of multiple countries during 1990-2014
"""


header = df_urban_countries.iloc[0].values.tolist()
df_urban_countries.columns = header

#Cleaning the dataframe

df_urban_countries = df_urban_countries.iloc[1:]
df_urban_countries = df_urban_countries.iloc[11:55]

df_urban_countries.index = df_urban_countries.index.astype(int)
df_urban_countries = df_urban_countries[df_urban_countries.index>1989]

df_urban_countries = df_urban_countries.dropna(axis = 'columns')

df_urban_time = pd.DataFrame.transpose(df_urban_countries)
years = [1990, 1995, 2000, 2005, 2010, 2014]
df_urban_subset_time = df_urban_time[years].copy()
df_urban_subset_time = df_urban_subset_time.loc[df_urban_subset_time.index.isin(countries)]


#plotting the data
plt.bar(k-0.3, df_urban_subset_time[1990], color = 'greenyellow',width = width, edgecolor = 'black',label='1990')
plt.bar(k-0.2, df_urban_subset_time[1995], color = 'teal',width = width, edgecolor = 'black',label='1995')
plt.bar(k-0.1, df_urban_subset_time[2000], color = 'lightseagreen',width = width, edgecolor = 'black',label='2000')
plt.bar(k, df_urban_subset_time[2005], color = 'khaki',width = width, edgecolor = 'black',label='2005')
plt.bar(k+0.1, df_urban_subset_time[2010], color = 'yellow',width = width, edgecolor = 'black',label='2010')
plt.bar(k+0.2, df_urban_subset_time[2014], color = 'greenyellow',width = width, edgecolor = 'black',label='2014')
plt.xlabel("Countries")
plt.ylabel("Urban Population")
plt.xticks(width+k, countries, rotation = 45)
plt.legend()
plt.title("Urban population (% of total population)")
plt.savefig("Urban.png", dpi=300, bbox_inches='tight')
plt.show()



"""
Agricultural land lineplot
A lineplot of agricultural land as a percentage of total land
"""

header = df_agri_countries.iloc[0].values.tolist()
df_agri_countries.columns = header

#Cleaning the dataframe
df_agri_countries = df_agri_countries.iloc[1:]
df_agri_countries = df_agri_countries.iloc[11:55]
df_agri_countries.index = df_agri_countries.index.astype(int)
df_agri_countries = df_agri_countries[df_agri_countries.index>1990]


#plotting the data as line chart
plt.figure()
plt.plot(df_agri_countries.index, df_agri_countries['United Arab Emirates'])
plt.plot(df_agri_countries.index, df_agri_countries['Australia'] )
plt.plot(df_agri_countries.index, df_agri_countries['Spain'])
plt.plot(df_agri_countries.index, df_agri_countries['France'])
plt.plot(df_agri_countries.index, df_agri_countries['United Kingdom'])
plt.plot(df_agri_countries.index, df_agri_countries['India'])
plt.plot(df_agri_countries.index, df_agri_countries['Somalia'])
plt.plot(df_agri_countries.index, df_agri_countries['United States'])
plt.xlim(1990,2014)
plt.xlabel("Year")
plt.ylabel("Forest Area %")
plt.legend(["UAE", "AU", "ESP", "FR", "UK", "IN", "SO", "US"])
plt.title("Agricultural land (% of land area)")
plt.savefig("agricultural_land.png", dpi = 300, bbox_inches='tight')
plt.show()
