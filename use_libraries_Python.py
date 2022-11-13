import numpy as np
from sklearn.linear_model import LinearRegression
x = np.array([2, 10, 15, 35, 42, 52]).reshape((-1, 1))
y = np.array([3, 18, 16, 30, 27, 42])
model = LinearRegression().fit(x, y)
print('b0=', model.intercept_)
print('b1=', model.coef_[0])
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)