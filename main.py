import math
import fractions 

def cabeçalho():
    print("--------------------------------------------------")
    print("                CALCULADORA DE FRAÇÕES            ")
    print("--------------------------------------------------")
    print('[1] Soma (+)\n[2] Subtração (-)\n[3] Multiplicação (*)\n[4] Divisão (/)')
    print("--------------------------------------------------")
    print("Escolha uma operação: ", end='')

       
def condicional(opcao):
    if opcao == 1:
        valor_fracao = fr1 + fr2
    elif opcao == 2:
        valor_fracao = fr1 - fr2
    elif opcao == 3:
        valor_fracao = fr1 * fr2
    else:
        valor_fracao = fr1 / fr2
    
    return valor_fracao    

#--------------------------------------------------------------------------------------------------------------------------------------------

cabeçalho()
operacao = int(input())

while True:
    if operacao < 1 or operacao > 4:
        cabeçalho()    
        operacao = int(input())
    else:
        break

print('--------------------1° FRAÇÃO---------------------')
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print('--------------------2° FRAÇÃO---------------------')
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))

fr1 = fractions.Fraction(n1,n2)
fr2 = fractions.Fraction(n3,n4)

valor_fracao = condicional(operacao)

numerador = valor_fracao.numerator
denominador = valor_fracao.denominator

def algoritmo_euclides(numerador, denominador):
        
        while denominador != 0:
            resto = numerador % denominador
            numerador = denominador
            denominador = resto

        return numerador


def verificar_primo(num):
    if num < 2:
        return False 
    
    for i in range(2, int(math.sqrt(num)) + 1):  
        if num % i == 0: 
            return False 
    
    return True

numerador_primo = verificar_primo(numerador)
denominador_primo = verificar_primo(denominador)

if numerador_primo == True or denominador_primo == True:
    resultado = (valor_fracao)   

else:
    resto = algoritmo_euclides(numerador, denominador)
    numerador_final = numerador // resto
    denominador_final = denominador // resto       

    resultado = (fractions.Fraction(numerador_final, denominador_final))

print(resultado)
