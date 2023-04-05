import csv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

x = []
xstr =[]
y = []

with open('visitor_counts.csv', 'r') as file:
    reader = csv.reader(file)

    # Get the reference date (midnight of the first date in the dataset)
    first_row = next(reader)
    date_str = first_row[0].split(' ')[0]
    ref_date = datetime.strptime(date_str, '%Y-%m-%d')
    ref_day = timedelta(days=1)

    # Read the rest of the rows and adjust the x-axis values to show only 24 hours
    for row in reader:
        try:
            date_time = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            date_diff = date_time - ref_date  # Get difference from ref date
            total_seconds = date_diff.total_seconds()
            hours = (total_seconds // 3600) % 24  # Get hours since midnight
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            x.append(timedelta(hours=hours, minutes=minutes, seconds=seconds))
            y.append(int(row[1]))
            xstr.append(timedelta(hours=hours, minutes=minutes, seconds=seconds).seconds)
        except Exception as err:
            continue

    # Plot the graph with overlapping datasets
    plt.plot(xstr, y, label=date_str)

    # Adjust the x-axis ticks and labels
    plt.xticks([x*3600 for x in range(0, 24)])
    plt.xlabel('Time (hh:mm:ss)')
    plt.ylabel('visitors')
    plt.title("RESTART's Visitors vs Time Graph")
    plt.legend(loc='upper left')
    plt.show()