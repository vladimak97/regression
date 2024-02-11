
# Implement a simple linear regression model in Python to predict a target variable based on a single feature.

import numpy as np

def simple_linear_regression(X, y):
    X_mean = np.mean(X)
    y_mean = np.mean(y)
    numerator = sum((X[i] - X_mean) * (y[i] - y_mean) for i in range(len(X)))
    denominator = sum((X[i] - X_mean) ** 2 for i in range(len(X)))
    slope = numerator / denominator
    intercept = y_mean - slope * X_mean
    return slope, intercept

X = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
slope, intercept = simple_linear_regression(X, y)
print(f"Linear Regression Equation: y = {slope} * x + {intercept}")