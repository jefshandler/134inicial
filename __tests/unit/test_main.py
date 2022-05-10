import pytest

from main import somar, subtrair, multiplicar, dividir


#class TesteCalc:


# Segundo teste unitario
def test_subtrair(self):
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
def test_multiplicar(self):
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
def test_dividr(self):
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


def test_somar():
    # 1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2 - Executa
    resutltado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resutltado_obtido == resultado_esperado


lista_de_valores = [
    (3, 6, 9),
    (3, 3, 6),
    (5, 4, 9),
    (6, 2, 8),
    (7, 9, 16),
    (2, 5, 7),
    (2222, 5000, 7222),
    (3, 9, 12),
    (-6, +3, -3),
    (10, 50, 60),
    (60, 28, 88),
    (79, 9, 88),
    (29, 59, 88),
    (288, 5000, 5288),
    (-6, +3, -3),
    (10, 50, 60),
    (60, 28, 88),
    (79, 9, 88),
    (29, 59, 88),
    (288, 5000, 5288)

]

@pytest.mark.parametrize('n1, n2, esperado', lista_de_valores)


def test_somar_leitura_lista(n1, n2, esperado):
    # 1 - Configura

    # resultado_esperado = 15

    # 2 - Executa
    obtido = somar(n1, n2)

    # 3 - Valida
    assert esperado == obtido