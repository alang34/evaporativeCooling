import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator
# csv_files = ['Data/mainData/22.8/40_1.csv',
#              'Data/mainData/22.8/40_2.csv',
#              'Data/mainData/22.8/40_3.csv',
csv_files = ['Data/mainData/testData/long1pt2.csv']


def plot(csv, x, y, log):
    df = pd.read_csv(csv)
    plt.figure(figsize=(8,6), label = f'Run {csv[-5]}')
    plt.plot(df[x], df[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{x} vs {y} for Run {csv[-5]}')
    plt.grid(True)
    plt.legend()
    if log:
        plt.xscale('log')
    plt.show()

def plot_all(csv_files, x, y, log):
    plt.figure(figsize=(8,6))
    for csv in csv_files:
        df = pd.read_csv(csv)
        plt.plot(df[x], df[y]-df["TempI"], label = f'Run {csv[-5]}')
        # plt.plot(df[x], df["TempI"], label = f'Run {csv[-5]} - Inside Temp')
        # plt.plot(df[x], df["TempR"], label = f'Run {csv[-5]} - Room Temp')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{x} vs {y} for All Runs')
    plt.grid(True)
    plt.legend()
    if log:
        plt.xscale('log')
    plt.show()



# plot(csv_files[0], "Timestamp", "RH", False)
# plot(csv_files[0], "Timestamp", "Temp", False)
plot_all(csv_files, "Timestamp", "Temp", False)