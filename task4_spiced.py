# calculate the MSE of y and ytrue
import numpy as np
import csv
import matplotlib.pyplot as plt

with open("C:\\Users\\Grimmel\\Desktop\\datapoints.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")

    xvalues = []
    yvalues = []

    for row in readCSV:
        xvalue = row[0]
        yvalue = row[1]

        xvalues.append(xvalue)
        yvalues.append(yvalue)

xvaluesnew = xvalues[1:]
yvaluesnew = yvalues[1:]

for i in range(0, len(xvaluesnew),1):
    xvaluesnew[i] = float(xvaluesnew[i])

for j in range(0, len(yvaluesnew),1):
    yvaluesnew[j] = float(yvaluesnew[j])

def calcypred(a,b):
    x = xvaluesnew
    y = [ (a*i +b) for i in x]
    return y

a = 10
b = 0
ypred = calcypred(a,b)
ytrue = yvaluesnew
MSE = np.square(np.subtract(ytrue, ypred)).mean()
print(MSE)
