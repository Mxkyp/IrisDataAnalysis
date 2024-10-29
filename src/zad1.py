#!/usr/bin/env python3
import numpy as np
import pandas as pd
import infoManagment as im
import plotInfo as pl
import matplotlib.pyplot

SETOSA = 0
VERSICOL = 1
VIRGI = 2
TOTAL = 3


def getIrisPopulationInfo(data):
    """get iris population and % values per type"""
    setosa = data[data["type"].isin([SETOSA])].copy()
    versicolor = data[data["type"].isin([VERSICOL])].copy()
    virginica = data[data["type"].isin([VIRGI])].copy()

    totalSize = len(setosa) + len(versicolor) + len(virginica)

    return  len(setosa), len(versicolor), len(virginica), totalSize

def getPopulationStats(populationStats):
    """format to for display in table"""
    setosaNumber = populationStats[SETOSA]
    versicolorNumber = populationStats[VERSICOL]
    virginicaNumber = populationStats[VIRGI]
    totalSize = populationStats[TOTAL]

    ratio0 = setosaNumber/totalSize * 100;
    ratio1 = versicolorNumber/totalSize * 100;
    ratio2 = virginicaNumber/totalSize * 100;

    populationInfo = {
        'Specie': ["Setosa", "Versicolor", "Virginica", "Total"],
        'Numerical Strength' : [setosaNumber, versicolorNumber , virginicaNumber, totalSize],
        'Numerical Strength%': [ratio0, ratio1, ratio2, 100.00]
    }

    df = pd.DataFrame(populationInfo)

    formated_table = df.style \
      .format(precision=2, thousands=".", decimal=",") \

    return formated_table.to_html()

def getCharacteristics(data):
    getSepalLengthStats(data)
    getSepalWidthStats(data)
    getPetalLengthStats(data)
    getPetalWidthStats(data)


def getSepalLengthStats(data):
    """get the minimum, maximum, arithmetic mean, median"""
    lengthCol= "length of the sepal(cm)"
    typeCol = "type"
    lengthData = data[[lengthCol, typeCol]]


    total = {
        "min":   np.min(lengthData[lengthCol]),
        "mean":  np.mean(lengthData[lengthCol]),
        "std":   np.std(lengthData[lengthCol]),
        "median":np.median(lengthData[lengthCol]),
        "mQ1":   np.percentile(lengthData[lengthCol], 25),
        "mQ3":   np.percentile(lengthData[lengthCol], 75)
    }

    s = lengthData[typeCol].isin([SETOSA]) #  only data about setosa's length
    setosa = {
        "min":   np.min(lengthData[s][lengthCol]),
        "mean":  np.mean(lengthData[s][lengthCol]),
        "std":   np.std(lengthData[s][lengthCol]),
        "median":np.median(lengthData[s][lengthCol]),
        "mQ1":   np.percentile(lengthData[s][lengthCol], 25),
        "mQ3":   np.percentile(lengthData[s][lengthCol], 75)
    }

    ve = lengthData[typeCol].isin([VERSICOL]) #  only data about versicolor's length
    versicolor = {
        "min":   np.min(lengthData[ve][lengthCol]),
        "mean":  np.mean(lengthData[ve][lengthCol]),
        "std":   np.std(lengthData[ve][lengthCol]),
        "median":np.median(lengthData[ve][lengthCol]),
        "mQ1":   np.percentile(lengthData[ve][lengthCol], 25),
        "mQ3":   np.percentile(lengthData[ve][lengthCol], 75)
    }

    vi = lengthData[typeCol].isin([VIRGI]) #  only data about virginica's length
    virginica = {
        "min":   np.min(lengthData[vi][lengthCol]),
        "mean":  np.mean(lengthData[vi][lengthCol]),
        "std":   np.std(lengthData[vi][lengthCol]),
        "median":np.median(lengthData[vi][lengthCol]),
        "mQ1":   np.percentile(lengthData[vi][lengthCol], 25),
        "mQ3":   np.percentile(lengthData[vi][lengthCol], 75)
    }

    return  setosa, versicolor, virginica, total





def main():
    DATA_LOC = '../resources/data1.csv'
    DATA_COL_NAMES = (["length of the sepal(cm)", "width of the sepal(cm)", "length of the petal(cm)",
                    "width of the petal(cm)", "type"])
    RESULTS_FILE_NAMES = (["populationTable.html", "characteristics.html", ])

    data = im.read_csv(DATA_LOC, DATA_COL_NAMES)

    popStats = getIrisPopulationInfo(data)
    popStatsFormated = getPopulationStats(popStats)

    im.writeToHtml(popStatsFormated, 'table.html')
    lengthInformation = getSepalLengthStats(data)
    print(lengthInformation[3])
    return data

main()
