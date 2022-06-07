from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from numpy import poly1d
from scipy.interpolate import lagrange
from scipy.optimize import curve_fit

import mae
import maxerror
import mse


class Approximation:
    @classmethod
    def approximationMethod(self, q, y):
        plt.cla()
        xdata = np.asarray(q)
        ydata = np.asarray(y)
        plt.plot(xdata, ydata, 'o')

        def Gauss(x, A, B):
            y = A * np.exp(-1 * B * x ** 2)
            return y

        parameters, covariance = curve_fit(Gauss, xdata, ydata)

        a = parameters[0]
        b = parameters[1]

        fit_y = Gauss(xdata, a, b)
        print("Współczynnik" + str(fit_y))
        plt.plot(xdata, ydata, 'o', label='data')
        plt.plot(xdata, fit_y, '-', label='fit')

        LagrangeCalculated = lagrange(q, y)
        L = poly1d(LagrangeCalculated)
        print("")
        print("Wielomian: " + str(L))

        print("------Błędy---------")
        mse.MSE.mseError(xdata, ydata)
        mae.MAE.maeError(xdata, ydata)
        maxerror.MaxError.maxError(xdata, ydata)
        plt.savefig("wykres.jpg")
        plt.legend()
        img = Image.open('wykres.jpg')
        img.show()