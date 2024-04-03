import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('placement_details.csv')
df.set_index('branch',inplace=True)

brtotal = df.sum(axis=1)
cototal = df.sum(axis=0)

branchtotal = brtotal.idxmax()
companytotal = cototal.idxmax()

print("branch with highest number of placemnets",branchtotal)
print("company with highest placement ",companytotal)