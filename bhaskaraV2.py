import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk


def gerar_grafico(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("esta equação não possui raízes reais")
        input("enter para sair")
    if delta == 0:
        raizunica = (-b) / (2 * a)
        print("a raiz desta equação é", raizunica)
        input("enter para sair")
    if delta > 0:
        d = math.sqrt(delta)
        raiz1 = (-b + d) / (2 * a)
        raiz2 = (-b - d) / (2 * a)
        labelr['text'] = ('as raízes da equação são', raiz2, 'e', raiz1)
        if a > 0:
            x = np.linspace(raiz2, raiz1)
            y = []
            for i in range(len(x)):
                y.append(a * x[i] ** 2 + b * x[i] + c)
        else:
            if a < 0:
                x = np.linspace(-raiz2, -raiz1)
                y = []
                for i in range(len(x)):
                    y.append(a * x[i] ** 2 - b * x[i] + c)
        plt.title("gráfico de {0}x^2 + {1}x + {2}".format(a, b, c))
        plt.xlabel("eixo x (abscissas)")
        plt.ylabel("eixo y (ordenadas)")
        plt.grid()
        plt.plot(x, y)
        plt.show()


root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=500, bg='grey')
canvas.pack()

label = tk.Label(root, bg='grey', text='insira os valores equivalentes a uma equação de segundo grau (ax^2+bx+c)')
label.place(relx=0.1, rely=0)

labelr = tk.Label(root)
labelr.place(relx=0.05, rely=0.6)

entrya = tk.Entry(root, bg='white', bd=2)
entrya.place(relx=0.30, rely=0.15)
labela = tk.Label(root, text='valor de A', bg='white')
labela.place(relx=0.05, rely=0.15)

entryb = tk.Entry(root, bg='white', bd=2)
entryb.place(relx=0.30, rely=0.28)
labelb = tk.Label(root, text='valor de B', bg='white')
labelb.place(relx=0.05, rely=0.28)

entryc = tk.Entry(root, bg='white', bd=2)
entryc.place(relx=0.30, rely=0.4)

labelc = tk.Label(root, text='valor de C', bg='white')
labelc.place(relx=0.05, rely=0.4)

button = tk.Button(root, text='verificar valores', bg='#404040', fg='white',
                   command=lambda: gerar_grafico(int(entrya.get()), int(entryb.get()), int(entryc.get())))
button.place(relx=0.05, rely=0.52)

root.mainloop()
