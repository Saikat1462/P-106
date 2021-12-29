import plotly.express as px
import csv 
import numpy as np 

with open("data2.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Size of TV",y="Time")
    fig.show()

def getdatasource(dp):
    size=[]
    time=[]
    with open(dp) as g:
        reader=csv.DictReader(g)
        for r in reader:
            size.append(float(r["Size of TV"]))
            time.append(float(r["Time"]))
    return{"x":size,"y":time}
def findcorrelation(ds):
    cl=np.corrcoef(ds["x"],ds["y"])
    print("correalation between size v/s time :",cl[0,1])
def setup():
    dp="data2.csv"
    ds=getdatasource(dp)
    findcorrelation(ds)
setup()