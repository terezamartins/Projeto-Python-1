# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6

import random


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

    def iniciar(self):
        while True:
            resposta = input(self.mensagem).upper().strip()
            if resposta == 'SIM' or resposta == 'S':
                self.gerar_valor_do_dado()
            elif resposta == 'NÃO' or resposta == 'N':
                print('Ok. Muito obrigada pela participaçãó!')
                break
            else:
                print('Por favor, digitar sim ou não.')

    def gerar_valor_do_dado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))


simulador = SimuladorDeDado()
simulador.iniciar()

