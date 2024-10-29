#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.random import multivariate_normal

import matplotlib.colors as mcolors

#def plotResults(Data: pd.DataFrame,):

def simpleStatistics(data: pd.DataFrame, outputFileName: str):
        bins = 8
        fig, ax = plt.subplots(nrows=4, ncols=2, figsize = (6.4 * 2, 4.8 * 4 + 4 * 1))

        write_histogram(ax[0,0], data["length of the sepal(cm)"], "length(cm)", "Numerical Strength", \
                        "Length of the sepal")
        write_histogram(ax[1,0], data["width of the sepal(cm)"], "width(cm)", "Numerical Strength", \
                        "Width of the sepal")
        write_histogram(ax[2,0], data["length of the petal(cm)"], "length(cm)", "Numerical Strength", \
                        "Length of the petal")
        write_histogram(ax[3,0], data["width of the petal(cm)"], "width(cm)", "Numerical Strength", \
                        "Width of the petal")
        write_boxplot(ax[0,1], data, "length of the sepal(cm)", "length(cm)", "Numerical Strength")

        plt.savefig(outputFileName)





def write_histogram(ax: list, data: pd.Series, labelX: str, labelY: str, title: str):
        bins = 8

        ax.hist(data.values, bins = bins, edgecolor = "black")
        ax.set_xlabel(labelX)
        ax.set_ylabel(labelY)
        ax.set_title(title)

def write_boxplot(ax: list, data: pd.DataFrame, dataColumn: str, labelX: str, labelY: str):
        bins = 8
        SETOSA = 0
        VERSICOL = 1
        VIRGI = 2
        TOTAL = 3

        setosa = data[data["type"].isin([SETOSA])][dataColumn].values
        versicolor = data[data["type"].isin([VERSICOL])][dataColumn].values
        virginica = data[data["type"].isin([VIRGI])][dataColumn].values

        specieData = [setosa, versicolor, virginica]
        specieLabels = ["Setosa", "versicolor", "virginica"]


        ax.boxplot(specieData, labels = specieLabels)
