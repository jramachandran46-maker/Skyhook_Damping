import pandas as pd
import numpy as np
df1 = pd.read_csv("rig_run_1_skyon.csv")
df2 = pd.read_csv("rig_run_2_skyoff.csv")
def rms(df):
    d = df["pos_mm"] - df["pos_mm"].mean()   # subtract the mean
    return np.sqrt(np.mean(d**2))            # calc rms values

rms_on, rms_off = rms(df1), rms(df2)
print(rms_on)
print(rms_off)
