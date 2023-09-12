import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

tempWeek1 = pd.read_csv("Temp_Week_1.csv")
tempWeek2 = pd.read_csv("Temp_Week_2.csv")

# tempWeek1['Temp'].fillna(tempWeek1['Temp'].mean(), inplace=True)

tempWeek1['Temp'].interpolate(method='linear', inplace=True)

# tempWeek1 = tempWeek1.pivot(index='')

ax = tempWeek1.plot.line(x='Day', y='Temp')  # type:plt.Axes
tempWeek2.plot.line(x='Day', y='Temp', ax=ax)

ax.set_xlabel("Day of Week")
ax.set_ylabel("Temperature (Celsius)")
ax.set_title("Average Daily Temperature Changes")
ax.legend(["#1", "#2"], loc='lower left', title='Week')

tempWeeks = pd.concat([tempWeek1, tempWeek2])
tempWeeks["DayWeek"] = tempWeeks["Day"] + tempWeeks["Week"]

ax2: plt.Axes = tempWeeks.plot.line(x="DayWeek",y="Temp")
ax2.set_title("Average Daily Temperature over 2 Weeks")
ax2.set_xlabel("Day of Week")
ax2.set_ylabel("Temperature (Celsius)")

plt.show()
