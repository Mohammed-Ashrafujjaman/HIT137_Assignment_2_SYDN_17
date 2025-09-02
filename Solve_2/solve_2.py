
'''
Group Name: Sydney Group 17
Group Members: 4
Mohammed Ashrafujjaman Hera - 391197
Pujan Dey  - 395076
Shaown Imtiaz - 396121
Al-Amin Dhaly - 395230
'''

import os,glob
import pandas as pd
import matplotlib.pyplot as plt

def reading_dataset(dateset_name):
    # reading current directory of this pyhton file
    cwd = os.path.dirname(__file__)
    # joining the dataset name to the directory path
    path = os.path.join(cwd, dateset_name)
    # reading the dataset and returning it
    return pd.read_csv(path)
    
#Alamin Dhaly --> Preprocessing
def preprocessing_data():
    # defining directory path so that is can be execute from any where but still open the python file directory
    cwd = os.path.dirname(__file__)
    # Joining the "temperatures" folder/directory with the current working file's directory
    path = os.path.join(cwd, "temperatures")
    # Creating list of path for each csv files 
    all_files = glob.glob(os.path.join(path, "stations_group_*.csv"))

    # Combining all the CSVs into one file
    dfs = [pd.read_csv(f) for f in all_files]
    df = pd.concat(dfs, ignore_index=True)
    
    # Checking if there is any Null value
    print("\nCounting Null values in the dataset: \n")
    print(df.isnull().sum())
    

    # Reformating Column Names -- Just capitalizing the coulumn names
    df.columns = [c.strip().capitalize() for c in df.columns]

    # Reshaping the Format
    reshaped_df = df.melt(
        id_vars=["Station_name", "Stn_id", "Lat", "Lon"],
        var_name="Month",
        value_name="Temperature"
    )
    
    # Checking if there is any missing value after reshaping the dataset
    print("\nrecounting Null values in the dataset after reshaping dataset: \n")
    print(reshaped_df.isnull().sum())
    # since there are no null values, we don't need to handle missing value
    # print(df.info())
    # print(df_long.info())

    # #Handlimg Missing Values
    # df_long = df_long.dropna(subset=["Temperature"])


    # Mapping Months to Season
    season_map = {
        "December": "Summer", "January": "Summer", "February": "Summer",
        "March": "Autumn", "April": "Autumn", "May": "Autumn",
        "June": "Winter", "July": "Winter", "August": "Winter",
        "September": "Spring", "October": "Spring", "November": "Spring"
    }

    # Adding new column in the dataset called "Season" according to months
    reshaped_df["Season"] = reshaped_df["Month"].map(season_map)

    # Saving Preprocessed Data to local file
    output_file = os.path.join(cwd,"preprocessed_temperatures.csv")
    reshaped_df.to_csv(output_file, index=False)

    print(f"\nPreprocessed dataset saved to {output_file}\n")
    
    
    # Information of the preprocessed dataset
    print(reshaped_df.info())
    # Display small sample of preprocessed dataset
    print(reshaped_df.head())

    
    
# Imtiaz --> seasonal average findings
def seasonal_average():
    # Reading the preprocessed dataset
    df = reading_dataset("preprocessed_temperatures.csv")

    # Drop missing values if any (important!)
    df = df.dropna(subset=["Temperature"])

    # Grouping by Season and calculating mean temperature
    seasonal_avg = df.groupby("Season")["Temperature"].mean()

    # Reorder seasons to match Australian order (Summer -> Autumn -> Winter -> Spring)
    season_order = ["Summer", "Autumn", "Winter", "Spring"]
    seasonal_avg = seasonal_avg.reindex(season_order)

    # Save results to "average_temp.txt"
    output_file = os.path.join(os.path.dirname(__file__), "average_temp.txt")
    with open(output_file, "w") as f:
        for season, avg_temp in seasonal_avg.items():
            f.write(f"{season}: {avg_temp:.1f}°C\n")

    # Print to console (for checking results)
    print("\nSeasonal Average Temperatures:")
    for season, avg_temp in seasonal_avg.items():
        print(f"{season}: {avg_temp:.1f}°C")


# Pujan --> temperature range findings

def temperature_range():
    df = reading_dataset("preprocessed_temperatures.csv")
    df = df.dropna(subset=["Temperature"])

    station_group = df.groupby("Station_name")["Temperature"]

    # Calculate min, max, and range for each station
    station_stats = station_group.agg(["min", "max"])
    station_stats["range"] = station_stats["max"] - station_stats["min"]

    # Find max range
    max_range = station_stats["range"].max()
    largest_range_stations = station_stats[station_stats["range"] == max_range]

    # Save to file
    output_file = os.path.join(os.path.dirname(__file__), "largest_temp_range_station.txt")
    with open(output_file, "w") as f:
        for station, row in largest_range_stations.iterrows():
            f.write(
                f"{station}: Range {row['range']:.1f}°C "
                f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
            )

    print("✅ Largest temperature range results written to largest_temp_range_station.txt")

# Ashraf --> temperature stability findings
def temperature_stability():
    # reading Preprocessed dataset
    df = reading_dataset("preprocessed_temperatures.csv")
    
    # Group by Station name to 
    station_group = df.groupby("Station_name")

    # only select the 'Temperature' column from each group of stations
    temperature_groups = station_group["Temperature"]
    # print(f"list: {temperature_groups.head()}")

    # getting the standard deviation for each group of stations
    std_deviation = temperature_groups.std()
    # print(f"{std_deviation.head(5)}")
    
    # Finding out the  minimum and maximum standard deviation from the station group
    min_std = std_deviation.min()
    max_std = std_deviation.max()

    
    # Assign colors: default = grey, min = green, max = red
    colors = []
    for val in std_deviation:
        if val == min_std:
            colors.append("green")
        elif val == max_std:
            colors.append("red")
        else:
            colors.append("skyblue")
            
            
    # showing the standerd deviation in a bar chart
    plt.figure(figsize=(18, 6))  
    std_deviation.plot(kind='bar', color=colors)
    
    plt.title("Temperature Standard Deviation by Station Name")
    plt.ylabel("Standard Deviation (in Celsius)")
    plt.xlabel("Stations Name")
    # Rotate station names in vartical order for better readability
    plt.xticks(rotation=90)  
    plt.tight_layout()

    plt.show()

    # Finding out the stations with min and max standard deviation
    stable_station = std_deviation[std_deviation == min_std]
    variable_station = std_deviation[std_deviation == max_std]

    # Writing results into a file
    output_file = os.path.join(os.path.dirname(__file__),"temperature_stability_stations.txt")
    with open(output_file, "w") as f:
        f.write(f"Most Stable: {stable_station.index[0]}: StdDev {stable_station.values[0]:.1f} C\n")
        f.write(f"Most Variable: {variable_station.index[0]}: StdDev {variable_station.values[0]:.1f} C\n")



if __name__ == "__main__":
    # Function calling for different tasks
    preprocessing_data()
    seasonal_average()
    temperature_range()
    temperature_stability()