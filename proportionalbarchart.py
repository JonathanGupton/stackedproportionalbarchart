import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


FILEPATH = "data.csv"
df = pd.read_csv(FILEPATH)
cmi = df.loc[:, ["Hospital", "RW"]].groupby("Hospital").mean()
cmi.sort_values("RW", inplace=True)
cnt = df.loc[:, ["Hospital", "DRG"]].value_counts().unstack(1)
pct = cnt.div(cnt.sum(axis=1), axis=0)
comb = cmi.join(pct)
comb["M_prop"] = comb["M"] * comb["RW"]
comb["P_prop"] = comb["P"] * comb["RW"]

comb.reset_index(inplace=True)
comb['x_label'] = comb.Hospital + "\n" + comb.RW.apply(lambda x: f"{x:.4f}")
width = 0.5

fix, ax = plt.subplots()
bottom = np.zeros(len(comb))

p = ax.bar(comb.x_label, comb.P_prop, width, label="P", bottom=bottom)
bottom = bottom + comb.P_prop
m = ax.bar(comb.x_label, comb.M_prop, width, label="M", bottom=bottom)
ax.set_title("Hospital CMI - 2022")
ax.legend(loc="upper right")

plt.show()
