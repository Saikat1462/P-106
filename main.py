import plotly.express as px
import csv 
import numpy as np 

with open("data1.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Temperature",y="Ice-cream Sales")
    fig.show()

def getdatasource(dp):
    temperature=[]
    ice_cream=[]
    with open(dp) as g:
        reader=csv.DictReader(g)
        for r in reader:
            ice_cream.append(float(r["Ice-cream Sales"]))
            temperature.append(float(r["Temperature"]))
    return{"x":temperature,"y":ice_cream}
def findcorrelation(ds):
    cl=np.corrcoef(ds["x"],ds["y"])
    print("correalation between temperature v/s ice cream :",cl[0,1])
def setup():
    dp="data1.csv"
    ds=getdatasource(dp)
    findcorrelation(ds)
setup()