import csv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

x = []
y = []
colors = []

color_selection = ['red', 'blue', 'green', 'brown', 'gray', 'violet', 'yellow']
curcolor = 0
sections = []
with open('visitor_counts.csv', 'r') as file:
    reader = csv.reader(file)

    # Get the reference date (midnight of the first date in the dataset)
    first_row = next(reader)
    date_str = first_row[0].split(' ')[0]
    prev_date_str = date_str
    ref_date = datetime.strptime(date_str, '%Y-%m-%d')
    ref_day = timedelta(days=1)

    # Read the rest of the rows and adjust the x-axis values to show only 24 hours
    rowcount = 0
    for row in reader:
        try:
            if len(row)<2: continue  # bypass of empty rows
            date_str = row[0].split(' ')[0]
            date_time = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            date_diff = date_time - ref_date  # Get difference from ref date
            total_seconds = date_diff.total_seconds()
            hours = (total_seconds // 3600) % 24  # Get hours since midnight
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            x.append(timedelta(hours=hours, minutes=minutes, seconds=seconds).seconds)
            y.append(int(row[1]))
            # Use a different color for each day's data
            if prev_date_str != date_str:
                if curcolor == len(color_selection)-1:
                    curcolor = 0
                else:
                    curcolor += 1
                colors.append(color_selection[curcolor])
                sections.append([rowcount,prev_date_str])
                prev_date_str = date_str
            else:
                colors.append(color_selection[curcolor])
            rowcount += 1
        except Exception as err:
            print(err)
            continue
    sections.append([rowcount-1,prev_date_str])
    # print(colors)
    # Plot the graph with overlapping datasets
    beginpref = 0
    for s in sections:
        plt.plot(x[beginpref:s[0]], y[beginpref:s[0]], color=colors[s[0]-1], label=s[1])
        print(f"Section: {s[1]} data entries {s[0]-beginpref}")
        beginpref = s[0]

    # Adjust the x-axis ticks and labels
    plt.xticks([x * 3600 for x in range(0, 24)], [x for x in range(0, 24)])
    plt.xlabel('Time (Hours)')
    plt.ylabel('Visitors')
    plt.title("RESTART's visitors vs Time Graph")
    plt.legend(loc='best')
    plt.gca().xaxis.grid(True, color='darkgrey', linestyle='-')
    plt.gca().yaxis.grid(True, color='darkgrey', linestyle='-')
    plt.show()
