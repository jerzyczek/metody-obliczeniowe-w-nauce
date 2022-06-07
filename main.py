from tkinter import *
from tkinter.filedialog import askopenfilename

import numpy as np
import pandas as pd
import numpy
from numpy import floor
from numpy.lib.npyio import loadtxt

import Approximation
import Interpolation

def menu(menuOption):
    if menuOption == 1:
        return interpolation()
    if menuOption == 2:
        return approximation()
    if menuOption == 5:
        quit()

def interpolation():
    x, y = chooseReading()
    Interpolation.Interpolation.getInterpolation(x, y)
    while True:
        try:
            printMenuText()
            n = int(input("Co chcesz wybrać?: "))
            menu(n)
        except ValueError:
            print("Nie ma takiej opcji")
        else:
            break

def approximation():
    x, y = chooseReading()
    Approximation.Approximation.approximationMethod(x, y)
    while True:
        try:
            printMenuText()
            n = int(input("Co chcesz wybrać?: "))
            menu(n)
        except ValueError:
            print("Nie ma takiej opcji")
        else:
            break

def chooseReadingText():
    print("\r1 - Konsola \n"
          "\r2 - Plik excel \n"
          "\r3 - Plik tekstowy \n")

def chooseReading():
    chooseReadingText()
    while True:
        try:
            choose = int(input("Wybierz z menu: "))
            if choose == 1:
                return consoleType()
            if choose == 2:
                return excelType()
            if choose == 3:
                return txtType()
        except ValueError:
            chooseReadingText()
        except TypeError:
            print("Coś poszło nie tak: ")
            chooseReadingText()
        else:
            break

def consoleType():
    mainArray = []
    n = int(input("Ile wpsółrzędnych chcesz podać?: "))
    for i in range(n):
        res = list(map(float, input("\nPodaj współrzędne punktów " + (i + 1).__str__() + " : ").strip().split()))[:n]
        print(res)
        mainArray.append(res)
    splittedArrayOfPoints = np.array(mainArray)
    print(mainArray)
    try:
        x = splittedArrayOfPoints[:, 0]
        print("Punkty x :" + str(x))
        y = splittedArrayOfPoints[:, 1]
        print("Punkty y :" + str(y))
        return x, y
    except IndexError as error:
        print("Niepoprawnie wpisane dane, spróbuj ponownie: ")

def printMenuText():
    print(" 1. Interpolacja \n"
          " 2. Aproksymacja \n"
          " 3. Zakończ \n")

def excelType():
    global df
    print("Punkty na osi x należy podać w wierszu 1.\n"
          "Punkty na osi y należy podać w wierszu 2\n"
          "Jeśli punkt jest wartością zmiennoprzecinkową to wtedy należy wstawić"
          "np. 2.5, 3.33 itp."
          "UWAGA: W 1 kolumnie może być tylko 1 punkt oraz dane muszą być w formie tekstowej")
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    try:
        filename = askopenfilename()
        print("Otwieranie pliku o nazwie: " + str(filename))
        df = pd.read_excel(filename, header=None)
    except FileNotFoundError:
        print("Nie znaleziono pliku: ")
        printMenuText()
    newArray = df.to_numpy()
    middleIndex = int(floor(len(newArray) / 2))
    x = newArray[:middleIndex]
    y = newArray[middleIndex:]
    print(x)
    print(y)
    return x[0, :], y[0, :]

    while True:
        try:
            print("")
            n = int(input("Wybierz z menu: "))
            menu(n)
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
        else:
            break

def txtType():
    print("Aby pobrac punkty z pliku TXT współrzędne X proszę podać w pierwszej linii odzielone spacją.\n"
          "Punkty Y proszę podać w kolejnej linii, również odzielone spacją\n"
          "Jeżeli są to liczby zmiennoprzecinkowe proszę wstawić kropkę")
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    filename = askopenfilename()
    print("Opening : " + str(filename))
    try:
        with open(filename) as file:
            lines = loadtxt(file, dtype=str, comments="#", delimiter=",", unpack=False)
            print(lines)
    except FileNotFoundError:
        print("Nie znaleziono pliku: ")
        printMenuOnceAgain()
    newArray = np.array(np.split(lines, floor(len(lines))))
    middleIndex = int(floor(len(newArray) / 2))
    firstHalf = numpy.loadtxt(lines[:middleIndex])
    secondHalf = numpy.loadtxt(lines[middleIndex:])
    print(firstHalf)
    print(secondHalf)
    return firstHalf, secondHalf

    while True:
        try:
            print("")
            n = int(input("Wybierz z menu: "))
            menu(n)
        except ValueError:
            print("Nie ma takiej opcji, wybierz ponownie: ")
        except IndexError as error:
            print("Niepoprawnie wpisane dane, spróbuj ponownie: ")
            printMenuOnceAgain()
        except FileNotFoundError as error:
            print("Klikniety przycisk anuluj, spróbuj ponownie: ")
            printMenuOnceAgain()
        else:
            break

def printMenuOnceAgain():
    printMenuText()
    while True:
        try:
            menuOption = int(input("Wybierz pozycje z menu: "))
            menu(menuOption)
        except ValueError:
            print("Pozycja nie istnieje wybierz z istniejących pozycji: ")
        else:
            break

while True:
    try:
        printMenuText()
        menuOption = int(input("Wybierz pozycje z menu: "))
        menu(menuOption)
    except ValueError:
        print("Pozycja nie istnieje wybierz z istniejących pozycji: ")
    else:
        break