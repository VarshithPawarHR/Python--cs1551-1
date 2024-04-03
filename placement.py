import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('placement_details.csv')
df.set_index('Branch',inplace=True)

brtotal = df.sum(axis=1)
cototal = df.sum(axis=0)

branchtotal = brtotal.idxmax()
companytotal = cototal.idxmax()

print("branch with highest number of placemnets",branchtotal)
print("company with highest placement ",companytotal)

for branch,placement in df.iterrows():
  companytot = placement.idxmax()
  print("branch",branch,"company",companytot)


brtotal.plot(kind="pie",autopct="%1.1f%%")
plt.title("total placement across all departments")
plt.show()


cototal.plot(kind="pie",autopct="%1.1f%%")
plt.title("total placement acrooss all companies")
plt.show()