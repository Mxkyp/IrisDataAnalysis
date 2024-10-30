#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as sp

def specificStatisics(data: pd.DataFrame, outputFileName: str):
        fig1, ax1 = plt.subplots(nrows=3, ncols=2, figsize = (6.4 * 2, 4.8 * 4 + 4))
        writePointChart(ax1[0,0], data["length of the sepal(cm)"], data["width of the sepal(cm)"], "length of the sepal(cm)", "width of the sepal(cm)")
        writePointChart(ax1[1,0], data["length of the sepal(cm)"], data["width of the petal(cm)"], "length of the sepal(cm)", "width of the petal(cm)")
        writePointChart(ax1[2,0], data["width of the sepal(cm)"], data["width of the petal(cm)"], "width of the sepal(cm)", "width of the petal(cm)")
        writePointChart(ax1[0,1], data["length of the sepal(cm)"], data["length of the petal(cm)"], "length of the sepal(cm)", "length of the petal(cm)")
        writePointChart(ax1[1,1], data["width of the sepal(cm)"], data["length of the petal(cm)"], "length of the sepal(cm)", "length of the petal(cm)")
        writePointChart(ax1[2,1],  data["length of the petal(cm)"], data["width of the petal(cm)"],"length of the sepal(cm)", "length of the petal(cm)")
        plt.savefig(outputFileName)

def simpleStatistics(data: pd.DataFrame, outputFileName: str):
        fig, ax = plt.subplots(nrows=4, ncols=2, figsize = (6.4 * 2, 4.8 * 4 + 4))

        writeHistogram(ax[0,0], data["length of the sepal(cm)"], "length(cm)", "Numerical Strength", \
                        "Length of the sepal")
        writeHistogram(ax[1,0], data["width of the sepal(cm)"], "width(cm)", "Numerical Strength", \
                        "Width of the sepal")
        writeHistogram(ax[2,0], data["length of the petal(cm)"], "length(cm)", "Numerical Strength", \
                        "Length of the petal")
        writeHistogram(ax[3,0], data["width of the petal(cm)"], "width(cm)", "Numerical Strength", \
                        "Width of the petal")

        writeBoxPlot(ax[0,1], data, "length of the sepal(cm)", "length(cm)", "Numerical Strength")
        writeBoxPlot(ax[1,1], data, "width of the sepal(cm)", "width(cm)", "Numerical Strength")
        writeBoxPlot(ax[2,1], data, "length of the petal(cm)", "length(cm)", "Numerical Strength")
        writeBoxPlot(ax[3,1], data, "width of the petal(cm)", "width(cm)", "Numerical Strength")

        plt.savefig(outputFileName)





def writeHistogram(ax: list, data: pd.Series, labelX: str, labelY: str, title: str):
        #bins = 8

        ax.hist(data.values, edgecolor = "black")
        setAxesLabels(ax, labelX, labelY)
        ax.set_title(title)


def writeBoxPlot(ax: list, data: pd.DataFrame, dataColumn: str, labelX: str, labelY: str):
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

def writePointChart(ax: list, dataX: pd.Series, dataY: pd.Series, labelX: str, labelY: str):
        results = sp.linregress(dataX.values, dataY.values)
        ax.plot(dataX.values, dataY.values, 'o');
        ax.plot(dataX.values, results.intercept + results.slope * dataX.values);
        setAxesLabels(ax, labelX, labelY)
        #add title here

def setAxesLabels(ax: list, labelX: str, labelY: str):
        ax.set_xlabel(labelX)
        ax.set_ylabel(labelY)
