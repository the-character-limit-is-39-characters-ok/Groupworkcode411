#!/usr/bin/env python3

import fileinput
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.widgets import Slider
import pandas as pd


filenamec = 'Crash_Information_dataset.csv'

def add_data(filename):
    dfv =''
    df = pd.read_csv(filename)

    return df

def update_grid(indx):
    ax.clear()
    for x in range(N + 1):
        ax.axhline(x, lw=2, color='k', zorder=5)
        ax.axvline(x, lw=2, color='k', zorder=5)
    # draw the boxess
    if indx == 2013: 
        data = data1
    elif (indx == 2014):
        data = data2
    elif (indx == 2015):
        data = data3    
    ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)
    # turn off the axis labels
    ax.axis('off')


def compute(df):
    x = dict()
    y = dict()
    z = dict()



    return x, y, z

def normalize(df):
    df = df.loc[df['Collision Type'] == "Bicyclist"]
    print(df)
    
    df.drop("Crash Configuration",inplace=True, axis=1)
    df.drop("Total Casualty",inplace=True, axis=1)
    df.drop("Total Vehicles Involved",inplace=True, axis=1)
    df.drop("Crash Count", inplace=True, axis=1)
    return df
    
def plot(df):
    fig, ax = plt.subplots(1, 1)#, tight_layout=True)
# make color map
    my_cmap = mpl.colors.ListedColormap(['r', 'g', 'b'])
# set the 'bad' values (nan) to be white and transparent
    my_cmap.set_bad(color='w', alpha=0)
# draw the grid
    for x in range(len(df)):
        ax.axhline(x, lw=2, color='k', zorder=5)
        ax.axvline(x, lw=2, color='k', zorder=5)
# draw the boxes
    ax.imshow(df, interpolation='none', cmap=my_cmap, zorder=0)
# turn off the axis labels
    ax.axis('off')

    plt.subplots_adjust(bottom=0.25)
    ax_slider = plt.axes([0.1, 0.1, 0.8, 0.05])

    slider = Slider(ax_slider, "year", valmin=2013, valmax=2015, valstep=1)
    slider.on_changed(update_grid)



def main():

    df = add_data(filenamec)

    df = normalize(df)

    x, y, z = compute(df)


    plot(df)




    plt.show()



if __name__=='__main__':
    main()


