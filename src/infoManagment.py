#!/usr/bin/env python3
import pandas as pd
import numpy as np

def read_csv(file_name, column_names):
    data = pd.read_csv(file_name, header = None)
    data.columns = column_names
    return data

def writeToHtml(html_table, html_file_name):
    with open(html_file_name, 'w') as f:
        f. write(html_table)
        f.close()
