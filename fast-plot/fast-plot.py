import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# test data
x = range(5)
y = [1, 1.5, 1.2, 1.6, 1.6]
df = pd.read_excel('./test_data/data.xlsx')
df_time_series = pd.read_excel('./test_data/time_series_data.xlsx')

def fast_plot(x, y, xlabel = 'x', ylabel = 'y', legend_text = 'y',
              xlimit = None, ylimit = None, grid = True,  legend= True, filename = None):
    '''
    :param x: list, numpy list, iterable - x data
    :param y: list, numpy list, iterable - y data
    :param xlabel: str for x axis name; can use TeX
    :param ylabel: str for y axis name; can use TeX
    :param legend_text: str text for legend
    :param xlimit: tuple of floats (x_min, x_max) - if given sets it as x axis limit - if None auto lim
    :param ylimit: tuple of floats (y_min, y_max)- if given sets it as y axis limit - if None auto lim
    :param grid: bool - if true sets grid
    :param legend: bool - sets legend
    :return: matplotlib figure plot
    '''
    plt.plot(x, y, 'o-', label=legend_text)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    if legend:
        plt.legend()
    if grid:
        plt.grid(ls = '--')
    if xlimit:
        plt.xlim(xlimit)
    if ylimit:
        plt.ylim(ylimit)
    if filename:
        plt.savefig(filename)
    plt.show()

fast_plot(x, y, 'x', 'y [$m^2$]', 'data', filename = 'data')

def df_plot(df, xlabel, ylabel, width = 8, height = 6,
            grid = True, legend = True,  filename = None):
    '''
    :param df: pandas dataframe object with data for x axis in 1st col and data for y in rest
    :param xlabel: str for x axis name; can use TeX
    :param ylabel: str for y axis name; can use TeX
    :param width: float fig width
    :param height: float fig height
    :param grid: bool
    :param legend: bool True - shows legend, False - no legend
    :return: matplotlib figure plot
    '''
    columns_without_first = df.columns[1:]
    fig, ax = plt.subplots()
    for column in columns_without_first:
        ax.plot(df['x'], df[column], label=column)

    fig.set_figwidth(width)
    fig.set_figheight(height)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if legend:
        ax.legend()
    if grid:
        ax.grid(True, ls = '--')
    if filename:
        plt.savefig(filename)
    plt.show()

df_plot(df, 'x', 'y $m / \sqrt{ps}$', filename='1')