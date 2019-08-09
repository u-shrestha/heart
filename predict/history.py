import matplotlib.dates as dates
import matplotlib.pyplot as plt

y=[40, 50, 80, 78] #att1
x=['02/09/2018', '11/10/2018', '12/11/2018', '14/12/2018'] #date
# z=[34, 44, 56, 78] #att2

fig = plt.figure()
ax = plt.axes()
ax.set( xlabel='date', ylabel='att_value', title='History')
new_x = dates.datestr2num(x)
ax.plot_date(new_x, y, color='red', marker='o', linestyle='dashed', linewidth=0.8, markersize=3, label='att1', xdate=True)
# ax.plot_date(new_x, z, color='blue', marker='o', linestyle='dashed', linewidth=0.8, markersize=3, label='att2', xdate=True)

plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()