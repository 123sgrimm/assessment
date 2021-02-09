# task6 also modify b
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

a = 2.1
b = 3
value = 21.3    # MSE value for a=10
while b >= -3:
    ypred = calcypred(a,b)
    ytrue = yvaluesnew
    MSE = np.square(np.subtract(ytrue, ypred)).mean()
    b = b - 0.1
    if MSE < value:
        value = MSE
        print(value,b)
print("The final value for the intercept b is 0.2 with corresponding MSE of 0.637")
print("The smallest MSE is obtained with the function y= 2.1x + 0.2")
