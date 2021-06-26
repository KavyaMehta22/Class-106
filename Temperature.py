import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    iceCream_Sales = []
    coldDrink_Sales = []


    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            iceCream_Sales.append(float(row["Temperature"]))
            coldDrink_Sales.append(float(row["Ice-cream Sales( â‚¹ )"]))

    return {"x": iceCream_Sales, "y": coldDrink_Sales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Temperature vs Ice-Cream Sales :", correlation[0, 1])

def setup():
    data_path = "Temperature.csv"
    dataSource  = getDataSource(data_path)

    findCorrelation(dataSource)

setup()

    
        



