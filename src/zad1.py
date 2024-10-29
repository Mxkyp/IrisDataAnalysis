#!/usr/bin/env python3
import numpy as np
import pandas as pd
import infoManagment as im
import matplotlib.pyplot


def getIrisPopulationInfo(data):
    """get iris population and % values per type"""
    setosa = data[data["type"].isin([0])].copy()
    versicolor = data[data["type"].isin([1])].copy()
    virginica = data[data["type"].isin([2])].copy()

    totalSize = len(setosa) + len(versicolor) + len(virginica)

    return totalSize, len(setosa), len(versicolor), len(virginica)

def getPopulationStats(populationStats):
    """format to for display in table"""
    totalSize = populationStats[0]
    setosaNumber = populationStats[1]
    versicolorNumber = populationStats[2]
    virginicaNumber = populationStats[3]

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



def main():
    DATA_LOC = '../resources/data1.csv'
    DATA_COL_NAMES = (["length of the sepal(cm)", "width of the sepal(cm)", "length of the petal(cm)",
                    "width of the petal(cm)", "type"])
    RESULTS_FILE_NAMES = (["populationTable.html", "characteristics.html", ])

    data = im.read_csv(DATA_LOC, DATA_COL_NAMES)
    popStats = getIrisPopulationInfo(data)
    popStatsFormated = formatPopulationStats(popStats)

    im.writeToHtml(popStatsFormated, 'table.html')
    return data

main()
