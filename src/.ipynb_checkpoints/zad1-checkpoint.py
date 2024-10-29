#!/usr/bin/env python3
import numpy as np
import pandas as pd
import infoManagment as im
import plotInfo as pl

SETOSA = 0
VERSICOL = 1
VIRGI = 2
TOTAL = 3

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

    return data

def getIrisPopulationInfo(data: pd.DataFrame):
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

def getCharacteristics(data: pd.DataFrame):
    getSepalLengthStats(data)
    getSepalWidthStats(data)
    getPetalLengthStats(data)
    getPetalWidthStats(data)

def getSepalLengthStats(data: pd.DataFrame):
    """get the minimum, maximum, arithmetic mean, median"""
    lengthCol= "length of the sepal(cm)"
    typeCol = "type"
    lengthData = data[[lengthCol, typeCol]]

    total = getInformation(lengthData[lengthCol])

    s = lengthData[typeCol].isin([SETOSA]) #  only data about setosa's length
    setosa = getInformation(lengthData[s][lengthCol])

    ve = lengthData[typeCol].isin([VERSICOL]) #  only data about versicolor's length
    versicolor = getInformation(lengthData[ve][lengthCol])

    vi = lengthData[typeCol].isin([VIRGI]) #  only data about virginica's length
    virginica = getInformation(lengthData[vi][lengthCol])

    return  setosa, versicolor, virginica, total


def getInformation(specificData: pd.Series):
    """specificData == singular numeric column"""
    informationSet = {
        "min":   np.min(specificData),
        "mean":  np.mean(specificData),
        "std":   np.std(specificData),
        "median":np.median(specificData),
        "mQ1":   np.percentile(specificData, 25),
        "mQ3":   np.percentile(specificData, 75)
    }

    return informationSet




main()
