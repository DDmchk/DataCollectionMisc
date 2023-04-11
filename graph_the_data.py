"""
graph_the_data.py

make a graph on timeline of visitors in a row

"""
#TODO: overlap the week data

import csv
import matplotlib.pyplot as plt
from datetime import datetime

x = []
y = []

with open('visitor_counts.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        try:
            date_time_obj = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            x.append(date_time_obj)
            y.append(int(row[1]))
        except Exception as err:
            print(str(err))
            continue
plt.plot(x, y)
plt.gca().xaxis.grid(True, color='darkgrey', linestyle='-')
plt.gca().yaxis.grid(True, color='darkgrey', linestyle='-')
plt.xlabel('Time')
plt.ylabel('Visitors')
plt.title("Restart's visitors vs Time Graph")
plt.show()