import pandas as pd
import matplotlib.pyplot as plt
# does the day of the week affect how many accidents occur on a given day?

class DataCleanser:
    def __init__(self, file):
        self.file = file
        self.averages = {}
        self.loadfile()

    def loadfile(self):
        # reads csv then formats for specific columns
        self.data = pd.read_csv(self.file, usecols=["Day_of_week", "Time"])
        self.days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        # clean data, counts occurrences of days in week
        self.data_dayofweek = self.data["Day_of_week"].value_counts()
        self.data_dayofweek = self.data_dayofweek.reindex(self.days, fill_value=0)

        # convert time column to max within 30 minutes
        self.data["Time"] = pd.to_datetime(self.data["Time"], format="%H:%M:%S").dt.round("30min") # round to nearest 30 min interval
        self.data["Time"] = self.data["Time"].dt.strftime("%H:%M") # just get time from to_datetime
 
        # clean data, count occurrences of each time slot
        self.data_timeofday = self.data["Time"].value_counts()
        self.data_timeofday = self.data_timeofday.sort_index()
        
        # put into a dictionary
        self.dayofweek = {
            "type": "bar",
            "x_axis": self.days,
            "x_axis_title": "Day of the Week (Day)",
            "y_axis": self.data_dayofweek.values,
            "y_axis_title": "Number of Accidents",
            "graph_title": "Number of Accidents per Day of the Week"
        }
        
        self.timeofday = {
            "type": "line",
            "x_axis": self.data_timeofday.index.astype(str),
            "x_axis_title": "Time of Day (Hour:Minutes)",
            "y_axis": self.data_timeofday.values,
            "y_axis_title": "Number of Accidents",
            "graph_title": "Number of Accidents per Time of Day"
        }

        # calculate averages
        self.averages["day_mean"] = round(self.data_dayofweek.mean(),2)
        self.averages["day_median"] = round(self.data_dayofweek.median(), 2)

        self.averages["time_mean"] = round(self.data_timeofday.mean(), 2)
        self.averages["time_median"] = round(self.data_timeofday.median(), 2)
        
    def graph(self, dataset):
        # change plot type based on type
        match dataset["type"]:
            case "bar":
                plt.bar(dataset["x_axis"], dataset["y_axis"])

            case "line":
                plt.plot(dataset["x_axis"], dataset["y_axis"])

            case _:
                raise "Invalid Option"

        # styling and labels
        plt.xlabel(dataset["x_axis_title"])
        plt.xticks(rotation=90) 
        plt.ylabel(dataset["y_axis_title"])
        plt.title(dataset["graph_title"])
        plt.show()

    def __str__(self):
        print("Days of Week Occurrences")
        print(self.data["Day_of_week"].value_counts())
        print("MEAN: " + str(self.averages["day_mean"]))
        print("MEDIAN: " + str(self.averages["day_median"]))
        print()
        print("Time of Day Occurrences")
        print(self.data["Time"].value_counts())
        print("MEAN: " + str(self.averages["time_mean"]))
        print("MEDIAN: " + str(self.averages["time_mean"]))
        return ""

if __name__ == "__main__":
    data = DataCleanser("Traffic.csv")
    #data.graph(data.timeofday)
    #data.graph(data.dayofweek)
    print(data)