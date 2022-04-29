# importando a biblioteca de teste
import pytest
# nome da função obs quando colocar entre aspas é exatamente o que esta escrito
# quando entre parentes sem aspas é uma variavel
# os dois pontos indica que comecou
def imprimir_oi(name):
    print(f'Oi, {name}')

def somar(numero_a, numero_b):
    return numero_a + numero_b



if __name__ == '__main__':
    imprimir_oi('Jeferson-Helia-Noah')

    resultado = somar(7, -6)
    print(f'a soma: {resultado}')

# primeiro teste unitario
def teste_somar():
    #1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    #2 - Executa
    resutltado_obtido = somar(numero_a, numero_b)

    #3 - Valida
    assert resutltado_obtido ==resultado_esperado