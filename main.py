import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl


#Zad1
'''
m1 = np.array([1,2,3])
m2 = np.array([4,5,6])
m3 = m1 * m2
print(m3)
'''
#Zad2
'''
m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
m2 = np.array([[5,8,1,2],[9,3,0,6],[7,2,9,8],[3,4,1,0]])

def MinC(matrix):
    minC = [] #kolumny
    helpdesk = 99
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            if helpdesk > matrix[i][j]:
                helpdesk = matrix[i][j]
        minC.append(helpdesk)
        helpdesk = 99
    return minC
def MinV(matrix):
    minV = []  # wiersze
    helpdesk = 99
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            if helpdesk > matrix[j][i]:
                helpdesk = matrix[j][i]
        minV.append(helpdesk)
        helpdesk = 99
    return minV
def MaxC(matrix):
    maxC = [] #kolumny
    helpdesk = -99
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            if helpdesk < matrix[i][j]:
                helpdesk = matrix[i][j]
        maxC.append(helpdesk)
        helpdesk = -99
    return maxC
def MaxV(matrix):
    maxV = []  # wiersze
    helpdesk = -99
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix)):
            if helpdesk < matrix[j][i]:
                helpdesk = matrix[j][i]
        maxV.append(helpdesk)
        helpdesk = -99
    return maxV

print("Macierz 3x3:")
print("wiersze min:")
MnV =MinV(m1)
print(MnV)
print("kolumny min:")
MnC = MinC(m1)
print(MnC)
print("wiersze max:")
MxV = MaxV(m1)
print(MxV)
print("kolumny max:")
MxC = MaxC(m1)
print(MxC)
print("Macierz 4x4:")
print("wiersze min:")
MnV =MinV(m2)
print(MnV)
print("kolumny min:")
MnC = MinC(m2)
print(MnC)
print("wiersze max:")
MxV = MaxV(m2)
print(MxV)
print("kolumny max:")
MxC = MaxC(m2)
print(MxC)
'''
#Zad3
'''
m1 = np.array([1,2,3])
m2 = np.array([4,5,6])
m3 = m1 * m2
print(m3)
'''
#Zad4
'''
m1 = np.array([1,2,3])
m2 = np.array([4.5,5.7,6.8])
m3 = m1 * m2
print(m3)
'''
#Zad5
'''
m1 = np.array([[1,2,3],[4,5,6]])
def Sinosowanie(matrix):
    helpdesk = []
    for i in matrix:
        for j in i:
             helpdesk.append(np.sin(j))
    return helpdesk
a = Sinosowanie(m1)
print(a)
'''
#Zad6
'''
m1 = np.array([[1,2,3],[4,5,6]])
def Sinosowanie(matrix):
    helpdesk = []
    for i in matrix:
        for j in i:
             helpdesk.append(np.cos(j))
    return helpdesk
b = Sinosowanie(m1)
print(b)
'''
#Zad7
'''
m1 = np.array([[1,2,3],[4,5,6]])
def Sinosowanie(matrix):
    helpdesk = []
    for i in matrix:
        for j in i:
             helpdesk.append(np.sin(j))
    return helpdesk
a = np.array(Sinosowanie(m1))

m1 = np.array([[1,2,3],[4,5,6]])
def Sinosowanie(matrix):
    helpdesk = []
    for i in matrix:
        for j in i:
             helpdesk.append(np.cos(j))

    return helpdesk
b = np.array(Sinosowanie(m1))

c = a + b
print(c)
'''
#Zad8
'''
m1 = np.arange(9).reshape(3,3)
for i in m1:
    print(i)
'''
#Zad9
'''
m1 = np.arange(9).reshape(3,3)
print(m1)
for i in m1.flat:
    print(i)
'''
#Zad10
'''
m1 = np.arange(81).reshape(9,9)
print(m1)
m1 = m1.reshape(27,3)
print(m1)
m1 = m1.reshape(81,1)
print(m1)
# To wszystkie możliwości nie liczą odwróconej liczby kolmun i wersów
# Ogranicza nas liczba elementów macierzy, ponieważ musi bć ona zawsze taka sama
'''
#Zad11
'''
m1 = np.arange(12).reshape(1,12)
print(m1)
for i in m1.flat:
    print(i)
m2 = np.arange(12).reshape(3,4)
print(m2)
for i in m2.flat:
    print(i)
m3 = np.arange(12).reshape(4,3)
print(m3)
for i in m3.flat:
    print(i)
m4 = np.arange(12).reshape(2,6)
print(m4)
for i in m4.flat:
    print(i)
'''