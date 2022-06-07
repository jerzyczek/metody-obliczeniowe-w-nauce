from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from scipy.interpolate import lagrange

import mae
import maxerror
import mse


class Interpolation:
    @classmethod
    def getInterpolation(self, x, y):
        plt.cla()
        plt.plot(x, y, 'o')

        #  Calculate the polynomial coefficients
        LagrangeCalculated = lagrange(x, y)
        L = Polynomial(LagrangeCalculated).coef
        print("Współczynniki wielomianu: " + str(L))
        new_y = np.poly1d(L)
        print("------- Wielomian : -------\n"
              "\n"
              "" + str(new_y))
        print("------Błędy---------")
        mse.MSE.mseError(x, y)
        mae.MAE.maeError(x, y)
        maxerror.MaxError.maxError(x, y)
        X = np.linspace(x[0], x[-1])

        # Preparing a plot with values from polyval
        plt.plot(X, np.polyval(L, X))
        plt.savefig("wykres.jpg")
        plt.grid(True)
        img = Image.open('wykres.jpg')
        img.show()