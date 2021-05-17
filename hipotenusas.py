import math
import time
import pickle


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("tempo decorrido = {0}:{1}:{2}".format(int(hours),int(mins),sec))



def hipotenusas(a):
    start_time = time.time()
    try:
        todos_os_numeros = pickle.load(open('arquivo.data', 'rb'))
        ultimo_numero = todos_os_numeros[len(todos_os_numeros) - 1]
    except (OSError, IOError, EOFError) as e:
        todos_os_numeros = []
        escrever_arquivo = open('arquivo.data', 'wb')
        ultimo_numero = 0

    if ultimo_numero >= a:
        end_time = time.time()
        time_lapsed = end_time - start_time
        print(time_convert(time_lapsed))
        while a not in todos_os_numeros:
            a = a-1
        indice_numero = todos_os_numeros.index(a)
        return todos_os_numeros[:indice_numero+1]
    else:
        for num in range(ultimo_numero,a+1):
            for i in range(1,num):
                for j in range(1,num):
                    if math.sqrt(i**2+j**2)%num == 0:
                        if num in todos_os_numeros:
                            break
                        else:
                            todos_os_numeros.append(num)


    end_time = time.time()
    time_lapsed = end_time - start_time
    print(time_convert(time_lapsed))
    escrever_arquivo = open('arquivo.data', 'wb')
    pickle.dump(todos_os_numeros, escrever_arquivo)
    return todos_os_numeros







