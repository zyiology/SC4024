import matplotlib.pyplot as plt
import seaborn
import pandas as pd

df = pd.read_csv("hire2FTE.csv", index_col=0)
print(df)

# df_long = df.melt(id_vars="Transactions")
# print(df_long)

# ax = seaborn.barplot(df_long, x="variable", y="value", hue="Transactions")
#
# ax.set(xlabel="Months in 2020", ylabel="Transaction Volume",
#        title="Please approve our request to hire 2 new workers")
#
# plt.axvline(x=4, color="red", linestyle="--")
# plt.text(x=4.1, y=max(df_long['value'])+1, s="Two workers quit", color="red")
#
# plt.show()

ax = seaborn.lineplot(data=df.T)
plt.ylim(0, df.max().max()*1.1)

# print(df.diff().iloc[[1]])
#print(df.diff().iloc[[1]].cumsum(1))
colors = ['orange'] * (len(df.T) - 1) + ['red']
values=-df.diff().iloc[1].cumsum()
categories=df.columns
plt.bar(categories,values, color=colors)
ax.set(xlabel="Months in 2020", ylabel="Transaction Volume",
       title="Please approve our request to hire 2 new workers")
# print(colors)
#seaborn.barplot(data=-df.diff().iloc[[1]].cumsum(axis='columns'), color=colors)

#seaborn.barplot(data=df.T["Shortfall"])
plt.show()
