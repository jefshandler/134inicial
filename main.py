# importando a biblioteca de teste
import pytest
# nome da função obs quando colocar entre aspas é exatamente o que esta escrito
# quando entre parentes sem aspas é uma variavel
# os dois pontos indica que comecou


def imprimir_oi(name):
    print(f'Oi, {name}')

def somar(numero_a, numero_b):
    return numero_a + numero_b

def subtrair(numero_a, numero_b): #nome metodo ou funcao (nome usando um verbo){(parametro-ingredientes)}
    return numero_a - numero_b

def multiplicar(numero_a, numero_b):
    return numero_a * numero_b

def dividir(numero_a, numero_b):
    return numero_a / numero_b


if __name__ == '__main__':
    imprimir_oi('Jeferson-Helia-Noah')

    # Chamar da definição somar e mostrar o resultado
    resultado = somar(7, -6)
    print(f'a soma: {resultado}')

    # Chamar a definição subtrair e mostrar o resultado
    resultado = subtrair(100, 59)
    print(f'A subtração: {resultado}')

    # Chamar a definição Multiplicar e mostrar o resultado
    resultado = multiplicar(3, 5)
    print(f'A Multiplicação: {resultado}')


    # Chamar a definição Multiplicar e mostrar o resultado
    resultado = dividir(16, 4)
    print(f'A Divisao: {resultado}')

# primeiro teste unitario
def test_somar():
    #1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    #2 - Executa
    resutltado_obtido = somar(numero_a, numero_b)

    #3 - Valida
    assert resutltado_obtido ==resultado_esperado

# Segundo teste unitario
def test_subtrair():
    # 1 - Prepara / Configura
    # 1.1 - Dados de entrada / valores do seu teste /
    # se eu tiver um arquivo isso seria chamadao de massa de dados
    # (quando eu tenho uma planilha com informacao e resultado o nome e massa de teste
    numero_a = 100
    numero_b = 50

    # 1.2 - Resultados Esperados
    resultado_esperado = 50

    # 2 - Executa
    resutltado_obtido = subtrair(numero_a, numero_b)

    # 3 - Valida /Checa
    assert resutltado_obtido == resultado_esperado

# Terceiro teste unitario
def test_multiplicar():
    # 1 - Prepara / Configura
    # 1.1 - Dados de entrada / valores do seu teste /
    # se eu tiver um arquivo isso seria chamadao de massa de dados
    # (quando eu tenho uma planilha com informacao e resultado o nome e massa de teste
    numero_a = 8
    numero_b = 7

    # 1.2 - Resultados Esperados
    resultado_esperado = 56

    # 2 - Executa
    resutltado_obtido = multiplicar(numero_a, numero_b)

    # 3 - Valida /Checa
    assert resutltado_obtido == resultado_esperado

# Terceiro teste unitario
def test_dividr():
    # 1 - Prepara / Configura
    # 1.1 - Dados de entrada / valores do seu teste /
    # se eu tiver um arquivo isso seria chamadao de massa de dados
    # (quando eu tenho uma planilha com informacao e resultado o nome e massa de teste
    numero_a = 20
    numero_b = 5

    # 1.2 - Resultados Esperados
    resultado_esperado = 4

    # 2 - Executa
    resutltado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida /Checa
    assert resutltado_obtido == resultado_esperado


