from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


class MAE:
    @classmethod
    def maeError(cls, x1, y1):
        x = x1.reshape(-1, 1)  # linear regresion
        model_regression = LinearRegression()
        model_regression.fit(x, y1)

        prediction = model_regression.predict(x)
        MAE = mean_absolute_error(y1, prediction)
        print("------ MAE ------")
        print(MAE.__str__())