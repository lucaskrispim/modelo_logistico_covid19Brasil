# -*- coding: utf-8 -*-
"""modelo_logistico.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vxcApOMDt_JlQG_HUV7W8Sq3z6oAHOcJ
"""

#
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import linalg
from scipy.optimize import fsolve

xdata = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]) # último 29/03
ydata = np.array([1,1,1,2,2,2,2,3,8,13,25,25,25,34,52,77,98,98,98,234,291,428,621,978,1178,1604,1960,2271,2555,2988,3477,3866,4233]) # infectados
mortos =np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,7,11,18,25,34,47,59,77,93,113,137]) # mortos
t = np.linspace(start = 1, stop = 33, num = 33)
t2 = np.linspace(start = 1, stop = 90, num = 90)

def exp_model(x,a,b,c,d):
  return a*np.exp(b*(x-c)) + d

def logistic_model(x,a,b,c):
    return c/(1+np.exp(-(x-b)/a))

popt, pcov = curve_fit(exp_model, xdata, ydata)
popt2, pcov2 = curve_fit(logistic_model,xdata,ydata)

popt

popt2

a,b,c = popt2
sol = int(fsolve(lambda x : logistic_model(x,a,b,c) - int(c),b))
fit = curve_fit(logistic_model,xdata,ydata)
errors = [np.sqrt(fit[1][i][i]) for i in [0,1,2]]
print()
print(sol,errors,*popt2)
print(logistic_model(54,*popt2))

print(linalg.norm(exp_model(xdata, *popt)-ydata))
print(linalg.norm(logistic_model(xdata, *popt2)-ydata))

print( logistic_model(34,*popt2),logistic_model(35,*popt2),logistic_model(36,*popt2) )
print( exp_model(34,*popt),exp_model(35,*popt),exp_model(36,*popt) )

plt.plot(xdata, exp_model(xdata, *popt), 'r-',label='exponencial')
plt.plot(xdata, logistic_model(xdata, *popt2), 'g-',label='logistico')
#plt.plot(xdata, func(xdata, *popt), 'r-',label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
plt.plot(xdata, ydata, 'b-', label='nº de casos de covid-19')
plt.xlabel('Dias')
plt.ylabel('nº de casos de covid-19')
plt.legend()
plt.show()

