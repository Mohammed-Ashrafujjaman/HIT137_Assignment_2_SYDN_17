'''
Create a program that analyses temperature data collected from multiple weather 
stations in Australia. The data is stored in multiple CSV files under a "temperatures" 
folder, with each file representing data from one year. Process ALL .csv files in the 
temperatures folder. Ignore missing temperature values (NaN) in calculations. 

Main Functions to Implement: 

    Seasonal Average: Calculate the average temperature for each season across ALL 
    stations and ALL years. Save the results to "average_temp.txt". 
        • Use Australian seasons: Summer (Dec-Feb), Autumn (Mar-May), Winter (Jun
        Aug), Spring (Sep-Nov) 
        • Output format example: "Summer: 28.5°C" 
    
    Temperature Range: Find the station(s) with the largest temperature range (difference 
    between the highest and lowest temperature ever recorded at that station). Save the 
    results to "largest_temp_range_station.txt". 
        • Output format example: "Station ABC: Range 45.2°C (Max: 48.3°C, Min: 3.1°C)" 
        • If multiple stations tie, list all of them 
    Temperature Stability: Find which station(s) have the most stable temperatures 
    (smallest standard deviation) and which have the most variable temperatures (largest 
    standard deviation). Save the results to "temperature_stability_stations.txt". 

• Output format example:  
o "Most Stable: Station XYZ: StdDev 2.3°C" 
o "Most Variable: Station DEF: StdDev 12.8°C" 
• If multiple stations tie, list all of them

'''

'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''

#Alamin Dhaly_Preprocessing

import os,glob
import pandas as pd


#Combining the CSVs

path = "temperatures"
all_files = glob.glob(os.path.join(path, "stations_group_*.csv"))

dfs = [pd.read_csv(f) for f in all_files]
df = pd.concat(dfs, ignore_index=True)

#Standardize Column Names

df.columns = [c.strip().capitalize() for c in df.columns]

#Reshaping the Format

df_long = df.melt(
    id_vars=["Station_name", "Stn_id", "Lat", "Lon"],
    var_name="Month",
    value_name="Temperature"
)

#Handlimg Missing Values

df_long = df_long.dropna(subset=["Temperature"])


#Mapping Months to Season

season_map = {
    "December": "Summer", "January": "Summer", "February": "Summer",
    "March": "Autumn", "April": "Autumn", "May": "Autumn",
    "June": "Winter", "July": "Winter", "August": "Winter",
    "September": "Spring", "October": "Spring", "November": "Spring"
}

df_long["Season"] = df_long["Month"].map(season_map)

#Storing Preprocessed Data

output_file = "preprocessed_temperatures.csv"
df_long.to_csv(output_file, index=False)

print(f"Preprocessing complete! Cleaned data saved to {output_file}")

#Display
print(df_long.head())

#End of Data Preprocessing