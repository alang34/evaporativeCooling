import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator
from scipy.optimize import curve_fit
# csv_files = ['Data/mainData/22.8/40_1.csv',
#              'Data/mainData/22.8/40_2.csv',
#              'Data/mainData/22.8/40_3.csv',
csv_files = [
             'Data/mainData/testData/long4.csv'
             ]


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

def plot_special(csv_files, x, y, log, overlay):
    fig, ax1 = plt.subplots(figsize=(8,3))
    for csv in csv_files:
        df = pd.read_csv(csv)
        initX = df[x][0]
        ax1.plot((df[x]-initX)/19531.25, (df[y]-24.09967)/24.09967, label = f'Run {csv[-5]}', marker='o', markersize=2)
        if overlay:
            # ax2 = ax1.twinx()  # Create a second y-axis
            x_values = np.linspace(0, 0.003976704, 1000)  # Example x values for fitting
            params, __ = fit_exp_curve((df[x]-initX)/19531.25, (df[y]-24.09967)/24.09967)
            ax1.plot(x_values, expFnt(x_values, params[0], params[1], params[2], params[3]), color='tab:red', label='Fitted Curve')
            print(params)
    ax1.set_xlabel(x)
    ax1.set_ylabel(y)
    ax1.set_xlim(left=10**-6, right=10**3)
    plt.title(f'{x} vs {y}')
    plt.grid(True)
    plt.legend()
    if log:
        plt.xscale('log')
    plt.show()
    
def plot_all(csv_files, x, y, log):
    plt.figure(figsize=(8,6))
    for csv in csv_files:
        df = pd.read_csv(csv)
        if y == "Bed" or y == "Water":
            plt.plot(df[x], avg(csv_files, y), label = f'Run {csv[-5]}')
        else:
            plt.plot(df[x], df[y], label = f'Run {csv[-5]}')
        plt.plot(df[x], df["Temp"], label = f'Run {csv[-5]} - Inside {y}')
        # plt.plot(df[x], df["TempR"], label = f'Run {csv[-5]} - Room {y}')
    plt.xlabel(x)
    plt.ylabel(y)
    # plt.axvline(x=450, color='r', linestyle='--')
    # plt.text(0.52, 0.67, 'Box & Interior opened', transform=plt.gca().transAxes, fontsize=8, verticalalignment='top', horizontalalignment='center', color='r')
    # plt.axvline(x=90, color='black', linestyle='--')
    # plt.text(0.2, 0.1, 'Compressor Ends', transform=plt.gca().transAxes, fontsize=8, verticalalignment='top', horizontalalignment='center', color='black')
    plt.title(f'{x} vs {y}')
    plt.grid(True)
    plt.legend()
    if log:
        plt.xscale('log')
    plt.show()    

def expFnt(x,a,b,h,k):
    return a * np.exp(b * (x - h)) + k

def fit_exp_curve(x, y):
    initial_guess = [0.0013, -0.2, 0, 0]  # Initial guess for the parameters
    params, covariance = curve_fit(expFnt, x, y, p0=initial_guess)
    return params, covariance

def avg(csv_files, x, window=240, min_periods=1):
    series_list = []
    for csv in csv_files:
        df = pd.read_csv(csv)
        if x in df.columns:
            s = pd.to_numeric(df[x], errors='coerce')
            ma = s.rolling(window=window, min_periods=min_periods).mean().reset_index(drop=True)
            series_list.append(ma)

    if not series_list:
        return pd.Series(dtype=float)

    df_ma = pd.concat(series_list, axis=1)
    mean_ma = df_ma.mean(axis=1)  # mean across files, ignoring NaNs
    return mean_ma

# plot(csv_files[0], "Timestamp", "RH", False)
# plot(csv_files[0], "Timestamp", "Temp", False)
# plot_special(csv_files, "Timestamp", "Bed", True, True)
plot_all(csv_files, "Timestamp", "Bed", False)
# print(avg(csv_files, "Bed"))
