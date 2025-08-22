#E1: Crea una función recursiva que calcule el factorial de un número.
def factorial(n):
    if n==0:
        return 1
    else:
        resultado = n*factorial(n-1)
    return resultado
    
print(factorial(4))

#E2: Implementa una función recursiva que sume todos los números desde 1 hasta n. 
def sum(n):
    return int(n)*(int(n)+1)/2

print(sum(5))

def sum2(n,m,i=1):
    if n==round(m/2):
        return n
    else:
        resultado=(n+i)+sum2(n-1,m,i+1)
    return resultado/2    

print(sum2(2,2,1))

def suma3(n):
    if n==1:
        return 1
    else:
        resultado = n+suma3(n-1)
    return resultado

print(suma3(100))

#E3: Crea una función recursiva que devuelva el n-ésimo término de la secuencia de Fibonacci.

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(6))

#E4: Implementa una función recursiva que calcule base^exponente.
def exponente(b,n):
    if n==0:
        return 1
    else:
        resultado = b*exponente(b,n-1)
    return resultado

print(exponente(2,8))

#E5: Escribe una función recursiva que cuente cuántos elementos hay en una lista.
lista1=[2,3,4,5,6,7,8,9,10,11,12]
def contar(lista,n=-1):
    if lista[0]==lista[n]:
        return n*-1
    else:
        contar(lista,n-1)

print(contar(lista1))

#E6: Crea una función recursiva que invierta un texto.