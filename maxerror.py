from sklearn.linear_model import LinearRegression
from sklearn.metrics import max_error


class MaxError:
    @classmethod
    def maxError(cls, x1, y1):
        x = x1.reshape(-1, 1)  # linear regresion
        model_regression = LinearRegression()
        model_regression.fit(x, y1)

        prediction = model_regression.predict(x)
        MAX = max_error(y1, prediction)
        print("------ MAX ERROR ------")
        print(MAX.__str__())