import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from datetime import timedelta, datetime

# Defining the data based on the provided image content
data = {
    "Activity": [
        "Get user requirements", "Project planning", "Feasibility Analysis", 
        "Sprint 1", "Sprint 2 & Client update", "Sprint 3", 
        "Sprint 4 & Client update", "Sprint 5", "Sprint 6 & Client update", 
        "Sprint 7", "Deployment & Monitoring", "Handing over"
    ],
    "Duration (weeks)": [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1],
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Setting the start date
start_date = datetime(2024, 9, 9)

# Calculating the start and end dates for each activity
df['Start Date'] = [start_date + timedelta(weeks=sum(df['Duration (weeks)'][:i])) for i in range(len(df))]
df['End Date'] = df['Start Date'] + pd.to_timedelta(df['Duration (weeks)'], unit='W')

# Plotting the Gantt chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting each bar for the Gantt chart
for i, task in df.iterrows():
    ax.barh(task['Activity'], (task['End Date'] - task['Start Date']).days, left=task['Start Date'], color='skyblue')

# Formatting the date on the x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.xticks(rotation=45)

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Activity')
plt.title('Project Gantt Chart')
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Displaying the plot
plt.tight_layout()
plt.show()
