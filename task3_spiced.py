# linear function y=a*x + b
# set the slope a to 10 and the intercept b to 0
# calculate y for every value of x

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

def plot_linear(a,b):
    x = xvaluesnew
    y = [ (a*i +b) for i in x]
    plt.plot(x,y, "ob")

a = 10
b = 0
plot_linear(a,b)
plt.show()
