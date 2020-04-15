# Multiproceso_Fibonacci
import random # Para generar num. aleatorios en la A y B 
import math
import multiprocessing as mp # Para trabajar en paralelo
import time

def sec_fib(n): # f() que calcula la mult. en secuencial, pero NO de manera recursiva  
    a = 0
    b = 1

    for k in range(n):
        c = a+b
        a = b
        b = c

    return b

def par_fib(n): # f() que prepara el reparto de trabajo para la mult. en paralelo
    
    n_cores = mp.cpu_count() # Obtengo los cores de mi pc
    size_fib = math.ceil( n /n_cores) # Fibonacci a procesar 
    
    print("Numero de cores que tiene el pc: ", n_cores)
    

    MC = mp.RawArray('i', n) # Array MC de memoria compartida donde se almacenaran los resultados
    cores = [] # Array para guardar los cores y su trabajo
    for core in range(n_cores):# Asigno a cada core el trabajo que le toca
        i_MC = min(core * size_fib, n) # Calculo i para marcar inicio del trabajo del core 
        f_MC = min((core + 1) * size_fib, n) # Calculo f para marcar fin del trabajo del core
        cores.append(mp.Process(target=par_core, args=(n, MC, i_MC, f_MC)))# Añado al Array los cores y su trabajo
    for core in cores:
        core.start()# Arranco y ejecuto el trabajo para c/ uno de los cores que tenga mi equipo
    for core in cores:
        core.join()# Bloqueo cualquier llamada hasta que terminen su trabajo todos los cores

def par_core(n, MC, i_MC, f_MC): # La tarea que hacen todos los cores
    for i in range(i_MC, f_MC): 
        for k in range(n): 
               #MC[i*n] += n 
               #MC[i] = sec_fib(i)
              MC[i] += n # Guarda resultado en MC[] de cada core


if __name__ == '__main__':
    n = 21514845 #se llego a probar hasta 215148, por que tardaba mucho en compilar

    a = 0
    b = 1
    c = a+b
    a = b
    b = c
    
    inicioS = time.time()
    print(sec_fib(n-1)) #Ejecuto el fibonacci de n
    finS = time.time()

    inicioP = time.time()
    par_fib(n)
    finP = time.time()
    print('Tiempo de ejecucion SECUENCIAL = ', finS-inicioS)
    print('Tiempo de ejecucion en PARALELO = ', finP-inicioP)
