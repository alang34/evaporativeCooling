import csv
import re
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
csv_box_3 = ['Data/mainData/box2/humidityData/extraNew/19.csv',
             'Data/mainData/box2/humidityData/extraNew/20.csv',
             'Data/mainData/box2/humidityData/extraNew/32.csv',
             'Data/mainData/box2/humidityData/extraNew/35.csv',
             'Data/mainData/box2/humidityData/extraNew/37.csv',
             'Data/mainData/box2/humidityData/extraNew/39.csv',
             'Data/mainData/box2/humidityData/extraNew/40.csv',
             'Data/mainData/box2/humidityData/extraNew/51.csv',
             'Data/mainData/box2/humidityData/extraNew/52.csv',
             'Data/mainData/box2/humidityData/extraNew/53.csv',
             'Data/mainData/box2/humidityData/extraNew/62.csv',
             'Data/mainData/box2/humidityData/extraNew/63.csv',
             'Data/mainData/box2/humidityData/extraNew/64.csv',
             ]
csv_70 = ['Data/mainData/box2/humidityData/new/30.csv',
           'Data/mainData/box2/humidityData/new/41.csv',
           'Data/mainData/box2/humidityData/new/55.csv',
           'Data/mainData/box2/ambient-120s-3/70-1.csv',
           'Data/mainData/box2/ambient-120s-3/70-2.csv']

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

def TRmultiplot(csv_singular, xVal, yVal, list, flags, rescale=False,
               reference_sensor=1):
    numbered_files = []
    for csv in csv_singular:
        match = re.match(r"\d+(?:\.\d+)?", Path(csv).stem)
        numbered_files.append((float(match.group()), csv))
    numbered_files.sort(key=lambda item: item[0])
    cmap = plt.colormaps["viridis"]
    if numbered_files:
        minimum = numbered_files[0][0]
        maximum = numbered_files[-1][0]

    plt.figure(figsize=(8,6))
    for value, csv in numbered_files:
        color = cmap((value - minimum) / (maximum - minimum)
                     if maximum > minimum else 0.5)
        df = pd.read_csv(csv)
        reference = df[f"{yVal}{reference_sensor}"]
        if rescale:
            reference_max = reference.max()
        for flag in flags:
            plt.axvline(x=flag, color='red', linestyle='--')
            continue
        for el in list:
            diff = df[yVal+el]
            smooth = ndimage.gaussian_filter1d(diff, sigma=1)
            if rescale:
                plot_val = (smooth - smooth[0]) / reference_max
            else:
                diff1 = reference
                smooth1 = ndimage.gaussian_filter1d(diff1, sigma=1)
                plot_val = smooth-smooth1
            baseline = plot_val[:20].mean()

            plt.plot(df[xVal]/20000, plot_val, color=color, label=yVal + " " + el + " at " + Path(csv).stem + "RH%")
    # plt.xscale("log")
    if rescale:
        plt.xlim(left=None, right = None)
        plt.ylim(bottom=None, top=None)
    plt.ylabel(f"(T(t) - T(0)) / max({yVal}{reference_sensor})" if rescale else yVal[0][:-1])
    plt.title(f'{xVal} vs normalized {yVal}' if rescale
              else f'{xVal} vs {yVal} of sensors {", ".join(map(str, list))} vs. Sensor {reference_sensor}')
    plt.grid(True)
    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.savefig('plot.png', bbox_inches='tight', dpi=300)
    plt.show()
    
    
def plotMaxTemperatureDrop(csv_files, sensor=2, reference_sensor=1):
    results = []
    for csv_path in csv_files:
        match = re.match(r"\d+(?:\.\d+)?", Path(csv_path).stem)
        df = pd.read_csv(csv_path)
        measured = df[f"Temp{sensor}"].to_numpy(dtype=float)
        reference = df[f"Temp{reference_sensor}"].to_numpy(dtype=float)
        drop = (ndimage.gaussian_filter1d(reference, sigma=2)
                - ndimage.gaussian_filter1d(measured, sigma=2))
        results.append({
            "file": str(csv_path),
            "file_number": float(match.group()),
            "mean_temperature_drop": float(drop[-20:].mean()),
        })
    results = pd.DataFrame(results, columns=[
        "file", "file_number", "mean_temperature_drop",
    ]).sort_values("file_number", kind="stable").reset_index(drop=True)

    fig, ax = plt.subplots(figsize=(8,6))
    ax.scatter(results["file_number"], results["mean_temperature_drop"],
               c=results["file_number"], cmap="viridis")
    ax.set_xlabel("Steady-State RH% Value")
    ax.set_ylabel("Mean Cooling Effect (C)")
    ax.set_title("Mean temperature drop over last 5 seconds by inlet RH%")
    ax.grid(True)
    plt.show()
    return results


def Humidity(csv_singular, xVal, yVal, list, flags, rh_ranges=None):
    if rh_ranges is None:
        rh_ranges = [(low, low + 10) for low in range(20, 100, 10)]
    rh_ranges = sorted((float(low), float(high)) for low, high in rh_ranges)
    if not rh_ranges or any(not (0 <= low < high <= 100)
                            for low, high in rh_ranges):
        raise ValueError("Provide RH ranges satisfying 0 <= lower < upper <= 100.")
    if any(right[0] < left[1] for left, right in zip(rh_ranges, rh_ranges[1:])):
        raise ValueError("RH ranges must not overlap.")

    fig, ax = plt.subplots(figsize=(8,6))
    cmap = plt.colormaps["viridis"].resampled(len(rh_ranges))
    trend_data = []
    for flag in flags:
        ax.axvline(x=flag, color='red', linestyle='--')
    for csv in csv_singular:
        df = pd.read_csv(csv)
        baseline_window = df["Timestamp"].between(0, 20)
        if not baseline_window.any():
            raise ValueError(f"No measurements in the first 20 seconds: {csv}")
        for first in range(6):
            later = first + 1
            difference = df[f"Temp{later}"] - df[f"Temp{first}"]
            baseline = difference[baseline_window].mean()
            adjusted = difference - baseline
            points = pd.DataFrame({
                "x": df[xVal], "y": adjusted, "rh": df[f"RH{first}"],
            }).replace([np.inf, -np.inf], np.nan).dropna()
            points["band"] = -1
            for band_index, (low, high) in enumerate(rh_ranges):
                in_range = (points["rh"] >= low) & (points["rh"] < high)
                if high == 100:
                    in_range |= points["rh"] == 100
                points.loc[in_range, "band"] = band_index
            trend_data.append(points)
    if trend_data:
        all_points = pd.concat(trend_data, ignore_index=True)
        total_points = len(all_points)
        # Ten-second windows centered on 0, 10, 20, ... seconds.
        all_points["time_bin"] = np.floor((all_points["x"] + 5) / 10) * 10
        print("RH band point counts (all CSVs and adjacent sensor pairs):")
        for band_index, (low, high) in enumerate(rh_ranges):
            band_points = all_points[all_points["band"] == band_index]
            count = len(band_points)
            fraction = count / total_points if total_points else 0
            status = "no data" if band_points.empty else "plotted"
            print(f"  {low:g}–{high:g}% RH: "
                  f"{count:,} points ({fraction:.1%}) — {status}")
            if band_points.empty:
                continue
            ax.scatter(
                band_points["x"], band_points["y"],
                color=cmap(band_index),
                s=5, linewidths=0, alpha=0.1, zorder=1,
            )
            means = band_points.groupby("time_bin")["y"].mean().sort_index()
            ax.plot(
                means.index, means, "o-", color=cmap(band_index),
                linewidth=3, markersize=5, alpha=1, zorder=3,
                label=f"{low:g}–{high:g}% RH",
            )
        if ax.get_legend_handles_labels()[0]:
            ax.legend(title="Lower-numbered sensor RH (10 s means)")
    ax.set_xlabel(xVal)
    ax.set_ylabel("Temperature difference minus first 20 s mean (°C)")
    ax.set_title(f'Temperature difference vs {xVal} for all sensor pairs')
    ax.grid(True)
    plt.show()
    
def combine(csv_list):
    """Save row-wise numeric averages to combine/<prefix>.csv and return them.

    The combine folder is created in the current working directory.
    Running again replaces output files for the same prefixes.
    """
    groups = {}
    for csv_path in csv_list:
        match = re.match(r"^(\d{2,3})(?!\d)", Path(csv_path).stem)
        if match is None:
            raise ValueError(
                f"CSV filename must start with a two- or three-digit number: {csv_path}"
            )
        prefix = int(match.group(1))
        groups.setdefault(prefix, []).append(pd.read_csv(csv_path))

    combined = {
        prefix: pd.concat(frames).groupby(level=0).mean(numeric_only=True)
        for prefix, frames in groups.items()
    }
    output_dir = Path("combine")
    output_dir.mkdir(parents=True, exist_ok=True)
    for prefix, df in combined.items():
        df.to_csv(output_dir / f"{prefix}.csv", index=False)
    return combined
        
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

TRmultiplot(csv_box_3, "Timestamp", "Temp", ["3"], [10, 30], rescale=False)
plotMaxTemperatureDrop(csv_box_3, sensor=3, reference_sensor=1)
# Humidity(csv_box_3, "Timestamp", "Temp", ["6"], [10, 30], rh_ranges = [(99, 100), (95,99), (85,90), (70,85)])
# combine(csv_hum)
# SRintervalPlot('Data/mainData/box2/ambient-120s-2/90SCFH.csv', "Timestamp", "Temp", 30, 0, [])
# plotMin(csv_ambient_50, "Temp")
