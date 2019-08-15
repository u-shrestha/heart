import pandas as pd
from matplotlib import pyplot as plt

y=[40, 50, 80, 78] #att
x=['2019-01-11', '2019-02-23', '2019-03-12', '2019-04-05']

df = pd.DataFrame(data={"date": x, "att_val": y})
df.to_csv("./history.csv", sep=',',index=False)

df = pd.read_csv('history.csv', parse_dates=True, index_col='date', sep=",")
df.plot( color='blue', marker='o', linestyle='dashed', linewidth=0.8, markersize=3)
plt.title("History")
plt.ylabel("Values")
plt.xlabel("Dates")
plt.legend(["att1"])
plt.savefig('..\.\static\graph\chol.png')
plt.show()
plt.close()



