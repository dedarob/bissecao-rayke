import math

errorMarg = 0.01
a = 0.5
b = 1
c = (a + b) / 2

funcA = a ** 2 + math.log(a)
funcB = b ** 2 + math.log(b)

while (b - a) >= errorMarg:
    funcA = a ** 2 + math.log(a)
    funcB = b ** 2 + math.log(b)
    funcC = c ** 2 + math.log(c)
    if funcA * funcC > 0:
        a = c
    if funcB * funcC > 0:
        b = c
    c = (a + b) / 2
result = (a + b) / 2
print("Resultado: {:.4}".format(result))
