import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = 'Traffic.csv' # load file

# reads csv then formats for specific columns
data = pd.read_csv(file, usecols=["Day_of_week", "Time"])
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# clean data, counts occurrences of days in week
data_dayofweek = data["Day_of_week"].value_counts()
data_dayofweek = data_dayofweek.reindex(days, fill_value=0)

# convert time column to max within 30 minutes
data["Time"] = pd.to_datetime(data["Time"], format="%H:%M:%S").dt.round("30min") # round to nearest 30 min interval
data["Time"] = data["Time"].dt.strftime("%H:%M") # just get time from to_datetime

# clean data, count occurrences of each time slot
data_timeofday = data["Time"].value_counts()
data_timeofday = data_timeofday.sort_index()

# put into a dictionary
dayofweek = {
    "x_axis": days,
    "x_axis_title": "Day of the Week (Day)",
    "y_axis": data_dayofweek.values,
    "y_axis_title": "Number of Accidents",
    "graph_title": "Number of Accidents per Day of the Week"
}

timeofday = {
    "x_axis": data_timeofday.index.astype(str),
    "x_axis_title": "Time of Day (Hour:Minutes)",
    "y_axis": data_timeofday.values,
    "y_axis_title": "Number of Accidents",
    "graph_title": "Number of Accidents per Time of Day"
}

# calculate averages
averages = {}
averages["day_mean"] = round(data_dayofweek.mean(),2)
averages["day_median"] = round(data_dayofweek.median(), 2)
averages["time_mean"] = round(data_timeofday.mean(), 2)
averages["time_median"] = round(data_timeofday.median(), 2)  

def graph(dataset):
    plt.plot(dataset["x_axis"], dataset["y_axis"])
    plt.fill_between(dataset["x_axis"], dataset["y_axis"], color="grey", alpha=0.4)

    # formulate line of best fit
    bestfit = np.polyfit(range(len(dataset["x_axis"])), dataset["y_axis"], 1)
    polynomial = np.poly1d(bestfit)
    plt.plot(dataset["x_axis"], polynomial(range(len(dataset["x_axis"]))))

    # styling and labels
    plt.xlabel(dataset["x_axis_title"])
    plt.xticks(rotation=90) 
    plt.ylabel(dataset["y_axis_title"])
    plt.title(dataset["graph_title"])
    plt.grid(axis = "y")
    
    plt.show()

def printCalculations():
    print("Days of Week Occurrences")
    print(data["Day_of_week"].value_counts())
    print("MEAN: " + str(averages["day_mean"]))
    print("MEDIAN: " + str(averages["day_median"]))
    print()
    print("Time of Day Occurrences")
    print(data["Time"].value_counts())
    print("MEAN: " + str(averages["time_mean"]))
    print("MEDIAN: " + str(averages["time_mean"]))

graph(timeofday)
graph(dayofweek)
printCalculations()