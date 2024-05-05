import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('placement.csv')
df.set_index('Branch', inplace=True)

brtotal = df.sum(axis=1)
cototal = df.sum(axis=0)

branchtotal = brtotal.idxmax()
companytotal = cototal.idxmax()

print("branch with highest number of placement is", branchtotal)
print("company name with highest number of placements ", companytotal)

for branch, placement in df.iterrows():
    companytot = placement.idxmax()
    print("branch", branch, "company", companytot)

brtotal.plot(kind='pie', autopct="%1.1f%%")
plt.title("total placements across all branches")
plt.show()

cototal.plot(kind='pie', autopct="%1.1f%%")
plt.title("total placements across all companies")
plt.show()
