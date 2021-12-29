import plotly.express as px
import csv 
import numpy as np 

with open("data3.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
    fig.show()

def getdatasource(dp):
    marks=[]
    days=[]
    with open(dp) as g:
        reader=csv.DictReader(g)
        for r in reader:
            marks.append(float(r["Marks In Percentage"]))
            days.append(float(r["Days Present"]))
    return{"x":marks,"y":days}
def findcorrelation(ds):
    cl=np.corrcoef(ds["x"],ds["y"])
    print("correalation between marks v/s days :",cl[0,1])
def setup():
    dp="data3.csv"
    ds=getdatasource(dp)
    findcorrelation(ds)
setup()