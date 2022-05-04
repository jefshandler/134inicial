from main import somar, subtrair, multiplicar, dividir


class TesteCalc:
    def test_somar(self):
        # 1 - Configura
        numero_a = 8
        numero_b = 7
        resultado_esperado = 15

        # 2 - Executa
        resutltado_obtido = somar(numero_a, numero_b)

        # 3 - Valida
        assert resutltado_obtido == resultado_esperado

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
