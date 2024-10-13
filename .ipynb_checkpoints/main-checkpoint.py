import pandas as pd
import matplotlib.pyplot as plt
# does the day of the week affect how many accidents occur on a given day?

class DataCleanser:
    def __init__(self, file):
        self.file = file
        self.loadfile()

    def loadfile(self):
        # reads csv then formats for specific columns
        self.data = pd.read_csv(self.file, usecols=['Day_of_week'])

        # clean data
        self.data = self.data['Day_of_week'].value_counts()
        self.data = self.data.sort_index()

        # break up into x and y components of bar graph
        self.x = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        self.y = self.data.values

    def graph(self):
        plt.bar(self.x, self.y)
        plt.xlabel('Day of the Week')
        plt.ylabel('Number of Accidents')
        plt.title('Number of Accidents per Day of the Week')
        plt.show()

if __name__ == "__main__":
    data = DataCleanser("Traffic.csv")
    data.graph()