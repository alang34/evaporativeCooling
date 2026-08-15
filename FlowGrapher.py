import csv
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.ticker import LogLocator
import scipy.ndimage as ndimage
from pathlib import Path
# csv_files = ['Data/mainData/22.8/40_1.csv',
#              'Data/mainData/22.8/40_2.csv',
#              'Data/mainData/22.8/40_3.csv',
csv_files = ['Data/mainData/setup1/data2.csv']
csv_ambient_50 = ['Data/mainData/ambient-50s/10SCFH.csv',
                'Data/mainData/ambient-50s/20SCFH.csv',
                'Data/mainData/ambient-50s/30SCFH.csv',
                'Data/mainData/ambient-50s/40SCFH.csv',
                'Data/mainData/ambient-50s/50SCFH.csv',
                'Data/mainData/ambient-50s/60SCFH.csv',
                'Data/mainData/ambient-50s/70SCFH.csv']
csv_ambient_180 = ['Data/mainData/ambient-180s/10SCFH.csv',
                   'Data/mainData/ambient-180s/20SCFH.csv',
                   'Data/mainData/ambient-180s/30SCFH.csv',
                   'Data/mainData/ambient-180s/40SCFH.csv',
                   'Data/mainData/ambient-180s/50SCFH.csv',
                   'Data/mainData/ambient-180s/60SCFH.csv',
                   'Data/mainData/ambient-180s/70SCFH.csv']
csv_aggregate = ['Data/mainData/ambient-50s/10SCFH.csv',
                'Data/mainData/ambient-50s/20SCFH.csv',
                'Data/mainData/ambient-50s/30SCFH.csv',
                'Data/mainData/ambient-50s/40SCFH.csv',
                'Data/mainData/ambient-50s/50SCFH.csv',
                'Data/mainData/ambient-50s/60SCFH.csv',
                'Data/mainData/ambient-50s/70SCFH.csv',
                'Data/mainData/ambient-180s/10SCFH.csv',
                'Data/mainData/ambient-180s/20SCFH.csv',
                'Data/mainData/ambient-180s/30SCFH.csv',
                'Data/mainData/ambient-180s/40SCFH.csv',
                'Data/mainData/ambient-180s/50SCFH.csv',
                'Data/mainData/ambient-180s/60SCFH.csv',
                'Data/mainData/ambient-180s/70SCFH.csv']
csv_box_2 = ['Data/mainData/box2/ambient-120s-2/70SCFH.csv',
             'Data/mainData/box2/ambient-120s-2/80SCFH.csv',
             'Data/mainData/box2/ambient-120s-2/90SCFH.csv',
             'Data/mainData/box2/ambient-120s-2/100SCFH.csv',
             'Data/mainData/box2/ambient-120s-2/110SCFH.csv',
             'Data/mainData/box2/ambient-120s-2/120SCFH.csv',
             'Data/mainData/box2/ambient-120s-2/130SCFH.csv',
             'Data/mainData/box2/ambient-120s-2/140SCFH.csv',
             'Data/mainData/box2/ambient-120s-2/150SCFH.csv']
csv_box_3 = ['Data/mainData/box2/ambient-120s-3/160SCFH.csv']

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

def SRintervalPlot(csv_singular, xVal, yVal, subdivisions, start_index, flags):
    plt.figure(figsize=(8,6))
    df = pd.read_csv(csv_singular)
    length = len(df["Timestamp"])
    indexArr = []
    cmap = plt.colormaps["summer"]
    for i in range(start_index, length, length//subdivisions):
        indexArr.append(i)
    for j, index in enumerate(indexArr):
        color = cmap(j / (len(indexArr) - 1))
        # plt.plot(np.array([0,1,2,3,4,5,6,7]),np.array([float(df[f"{yVal}0"].iloc[index]), float(df[f"{yVal}1"].iloc[index]), float(df[f"{yVal}2"].iloc[index]), float(df[f"{yVal}3"].iloc[index]), float(df[f"{yVal}4"].iloc[index]), float(df[f"{yVal}5"].iloc[index]), float(df[f"{yVal}6"].iloc[index]), float(df[f"{yVal}7"].iloc[index])]), color = color)
        plt.plot(np.array([0,1,2,3,4]),np.array([float(df[f"{yVal}0"].iloc[index]), float(df[f"{yVal}1"].iloc[index]), float(df[f"{yVal}2"].iloc[index]), float(df[f"{yVal}3"].iloc[index]), float(df[f"{yVal}4"].iloc[index])]), color = color)
    for flag in flags:
        plt.plot(np.array([0,1,2,3,4,5]),np.array([float(df[f"{yVal}0"].iloc[flag]), float(df[f"{yVal}1"].iloc[flag]), float(df[f"{yVal}2"].iloc[flag]), float(df[f"{yVal}3"].iloc[flag]), float(df[f"{yVal}4"].iloc[flag]), float(df[f"{yVal}A"].iloc[flag])]), color = "red")
    plt.xlabel("Position Index")
    plt.ylabel(yVal)
    plt.title(f'{xVal} vs {yVal} showing space/time progression at '+csv_singular[-10:-5])
    plt.grid(True)
    plt.legend([f"{subdivisions} subdivisions on a {df['Timestamp'].iloc[indexArr[-1]]}s interval"])
    plt.show()

def TRmultiplot(csv_singular, xVal, yVal, list, flags):
    plt.figure(figsize=(8,6))
    for csv in csv_singular:
        df = pd.read_csv(csv)
        for flag in flags:
            plt.axvline(x=flag, color='red', linestyle='--')
        for el in list:
            diff = df[yVal+el]
            smooth = ndimage.gaussian_filter1d(diff, sigma=3)
            diff1 = df[yVal+"1"]
            smooth1 = ndimage.gaussian_filter1d(diff1, sigma=3)
            baseline = smooth[:10].mean()
            
            plot_val = smooth
            plot_val1 = smooth1
            if csv[-11:-10] == "1":
                plt.plot(df['Timestamp'], (plot_val-df["Water"].mean())-(plot_val1-df["Water"].mean()), label=yVal+" "+el+" from "+Path(csv).stem)
            else:
                plt.plot(df['Timestamp'], (plot_val-df["Water"].mean())-(plot_val1-df["Water"].mean()), label=yVal+" "+el+" from "+csv[-10:-5])
    plt.xlabel(xVal)
    plt.ylabel(yVal[0][:-1])
    plt.title(f'{xVal} vs {yVal} showing gap between Sensor6/Water and Sensor 1/Water')
    plt.grid(True)
    plt.legend()
    plt.show()
    
def combine(csv_list):
    for csv in csv_list:
        

def plotMin(csv_singular, var):
    plt.figure(figsize=(8,6))
    for csv in csv_singular:
        df = pd.read_csv(csv)
        list = []
        if var == "Temp":
            list = ["Temp0", "Temp1", "Temp2", "Temp3", "Temp4", "TempA"]
        if var == "RH":
            list = ["RH0", "RH1", "RH2", "RH3", "RH4", "RHA"]
        currentMin = 10000
        impIndex = -1
        for el in list:
            tempMin = df[el].min()
            if tempMin < currentMin:
                currentMin = tempMin
                impIndex = el[-1]
        plt.scatter(int(csv[-10:-8]), currentMin-df[list[int(impIndex)]].head(20).sum()/20)
        plt.annotate(f"{impIndex}", (int(csv[-10:-8]), currentMin-df[list[int(impIndex)]].head(20).sum()/20), textcoords="offset points", xytext=(10,0), ha='center')
    plt.xlabel("Position Index")
    plt.ylabel(var)
    plt.title(f'Minimum {var} values by position')
    plt.grid(True)
    plt.legend()
    plt.show()

TRmultiplot(csv_box_3, "Timestamp", "Temp", ["6"], [10, 30])
# SRintervalPlot('Data/mainData/box2/ambient-120s-2/90SCFH.csv', "Timestamp", "Temp", 30, 0, [])
# plotMin(csv_ambient_50, "Temp")

