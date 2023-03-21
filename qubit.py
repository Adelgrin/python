import os

valor = 77
g = 8
r = 1


def fator(a):
    dividendo = g ** (r / 2) + a
    divisor = valor
    while not dividendo % divisor == 0:
        resultado = dividendo % divisor
        dividendo = divisor
        divisor = resultado
    return divisor

while not g ** r % valor == 1:
    r += 1
    print("running {}".format(r))
os.system('cls')
print("resultado({})".format(g ** r))
print("resto({})".format(g ** r % valor))
print("fatores ({}^{}/2+1)={}X({}^{}/2-1){}".format(g, r, fator(1), g, r, fator(-1)))
fator1 = fator(1)
fator2 = fator(-1)
if fator1 * fator2 == valor:
    print("{}X{}={}".format(fator1, fator2, valor))
else:
    print("incorreto")
