import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.ticker import LogLocator
# csv_files = ['Data/mainData/22.8/40_1.csv',
#              'Data/mainData/22.8/40_2.csv',
#              'Data/mainData/22.8/40_3.csv',
csv_files = ['Data/mainData/setup1/data2.csv']
csv_singular = ['Data/mainData/setup1/data3.csv']


def plot_all(csv_files, x, y, log):
    plt.figure(figsize=(8,6))
    for csv in csv_files:
        df = pd.read_csv(csv)
        for i in range(0,8,1):
            plt.scatter(i, df[f"{y}{i}"].iloc[-1], label = f"{y}{i}", color = "red")
            plt.scatter(i, df[f"{y}{i}"].iloc[-10], label = f"{y}{i}", color = "blue")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(f'{x} vs {y} showing spatial progression')
    plt.grid(True)
    # plt.legend()
    if log:
        plt.xscale('log')
    plt.show()

def intervalPlot(csv_singular, xVal, yVal, subdivisions, start_index, flags):
    plt.figure(figsize=(8,6))
    df = pd.read_csv(csv_singular[0])
    length = len(df["Timestamp"])
    indexArr = []
    cmap = plt.colormaps["summer"]
    for i in range(start_index, length, length//subdivisions):
        indexArr.append(i)
    for j, index in enumerate(indexArr):
        color = cmap(j / (len(indexArr) - 1))
        # for flag in flags:
            # if abs(flag-index) < length//subdivisions
        # plt.plot(np.array([0,1,2,3,4,5,6,7]),np.array([float(df[f"{yVal}0"].iloc[index]), float(df[f"{yVal}1"].iloc[index]), float(df[f"{yVal}2"].iloc[index]), float(df[f"{yVal}3"].iloc[index]), float(df[f"{yVal}4"].iloc[index]), float(df[f"{yVal}5"].iloc[index]), float(df[f"{yVal}6"].iloc[index]), float(df[f"{yVal}7"].iloc[index])]), color = color)
        plt.plot(np.array([0,1,2,3,4,5]),np.array([float(df[f"{yVal}0"].iloc[index]), float(df[f"{yVal}1"].iloc[index]), float(df[f"{yVal}2"].iloc[index]), float(df[f"{yVal}3"].iloc[index]), float(df[f"{yVal}4"].iloc[index]), float(df[f"{yVal}A"].iloc[index])]), color = color)
    plt.xlabel(xVal)
    plt.ylabel(yVal)
    plt.title(f'{xVal} vs {yVal} showing space/time progression')
    plt.grid(True)
    plt.legend([f"{subdivisions} subdivisions on a {df['Timestamp'].iloc[indexArr[-1]]}s interval"])
    plt.show()
# plot_all(csv_files, "Timestamp", "RH", False)
intervalPlot(csv_singular, "Timestamp", "RH", 100, 0, 99)
