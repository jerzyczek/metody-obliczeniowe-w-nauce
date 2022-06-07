from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


class MSE:
    @classmethod
    def mseError(cls, x1, y1):
        x = x1.reshape(-1,1) #linear regresion
        model_regression = LinearRegression()
        model_regression.fit(x, y1)

        prediction = model_regression.predict(x)
        MSE = mean_squared_error(y1, prediction, squared=True)
        print("------ MSE ------")
        print(MSE.__str__())