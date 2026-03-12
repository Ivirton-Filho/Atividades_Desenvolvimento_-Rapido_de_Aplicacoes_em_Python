def calculo(numero_a, numero_b, operacao):
    match operacao:
        case 'soma':
            return numero_a + numero_b
        case 'subtração':
            return numero_a - numero_b
        case 'multiplicação':
            return numero_a * numero_b
        case 'divisão':
            if numero_b != 0:
                return numero_a / numero_b
            else:
                return 'Erro: Divisão por zero não é permitida.'
        case _:
            return 'Operação inválida.'