x = [2, 10, 15, 35, 42, 52]
y = [3, 18, 16, 30, 27, 42]
n = len(x)
sumX = sum(x)
sumY = sum(y)
sumX2 = sum(map(lambda element: element ** 2, x))
sumYX = sum(map(lambda element1,element2: element1 * element2, x, y))
b0 = (sumY * sumX2 - sumYX * sumX)/(n * sumX2 - sumX * sumX)
b1 = (n * sumYX - sumX * sumY)/(n * sumX2 - sumX * sumX)
print('b0=', b0)
print('b1=', b1)
Ycalc = list(map(lambda element: b0 + b1 * element, x))
sumYYcalc2 = sum(map(lambda element1, element2: (element1 - element2) ** 2, y, Ycalc))
Yaverage = sumY / n
sumYYaverage2 = sum(map(lambda element1: (element1 - Yaverage) ** 2, y))
coefDeter = 1 - sumYYcalc2 / sumYYaverage2
print('coefficient of determination:', coefDeter)