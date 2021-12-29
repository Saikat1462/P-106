import plotly.express as px
import csv 
import numpy as np 

with open("data4.csv") as e:
    df=csv.DictReader(e)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()

def getdatasource(dp):
    coffee=[]
    sleep=[]
    with open(dp) as g:
        reader=csv.DictReader(g)
        for r in reader:
            coffee.append(float(r["Coffee in ml"]))
            sleep.append(float(r["sleep in hours"]))
    return{"x":coffee,"y":sleep}
def findcorrelation(ds):
    cl=np.corrcoef(ds["x"],ds["y"])
    print("correalation between coffee v/s sleep :",cl[0,1])
def setup():
    dp="data4.csv"
    ds=getdatasource(dp)
    findcorrelation(ds)
setup()