import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('placement.csv')

df.set_index('Branch', inplace=True)

brtotal = df.sum(axis=1)
cototal = df.sum(axis=0)

branchtotal = brtotal.idxmax()
companytotal = cototal.idxmax()

print("branch name with highest number o placement", branchtotal)
print("company name with highes no of placements is", companytotal)


for branch, placement in df.iterrows():
    comptot = placement.idxmax()
    print("branch", branch, "company", comptot)

brtotal.plot(kind='pie', autopct="%1.1f%%")
plt.title("total placements across all branches")
plt.show()

cototal.plot(kind='pie', autopct="%1.1f%%")
plt.title("total placement across all company")
plt.show()
