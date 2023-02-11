from random import randint as ran
from random import choice as ch
from playsound import playsound
import pyttsx3
import pywhatkit as pwk



cores = {'azul': '\033[34m', 'stop': '\033[m'}
falar = pyttsx3.init('sapi5')


class Filhos:
    def __init__(self):
        self.lista_de_numeros = {'marina': '+55 61 81541965', 'daniel': '+55 61 96052272', 'joao': '+55 61 81781162'}
        self.lista = []
        self.lista_de_seguros_e_acoes = []
        self.lista_de_cartoes = ['cartao de isencao', 'cartao dividindo os lucros', 'cartao dividindo despesa']
        self.lista_de_cartao_daniel = []
        self.lista_de_cartao_marina = []

    def filhos(self):
        filhos = int(input('quantos filhos voçê ganhou? '))
        self.lista.append(filhos)

    def valordosfilhos(self):
        valor_total = sum(self.lista) * 48.000
        print(valor_total)

    def linha_vazia(self):
        print(f'{"- - " * 10}')



    def mostrando_ativos(self, daniel=False, marina=False):
        filhos.linha_vazia()
        if daniel is True:
            for item in daniel_jogador.lista_de_seguros_e_acoes:
                print(item)
        if marina is True:
            for item in marina_jogador.lista_de_seguros_e_acoes:
                print(item)

    def comprando_cartao(self, daniel=False, marina=False):
        if daniel is True:
            cartao_escolhido = ch(daniel_jogador.lista_de_cartoes)
            daniel_jogador.lista_de_cartao_daniel.append(cartao_escolhido)
            print('cartão armazenado')
        if marina is True:
            cartao_escolhido = ch(marina_jogador.lista_de_cartoes)
            marina_jogador.lista_de_cartao_marina.append(cartao_escolhido)
            print('cartão armazenado')

    def excluindo_cartao(self, daniel=False, marina=False):
        if daniel is True:
            print('''cartao de isencao
cartao dividindo os lucros
cartao dividindo despesa''')
            cartao_a_ser_removido = str(input('digite o nome do cartao a ser removido: '))
            daniel_jogador.lista_de_cartao_daniel.remove(cartao_a_ser_removido)
            daniel_jogador.mandando_mensagem_automatica_para_daniel(nome='daniel')
        if marina is True:
            print('''cartao de isencao
cartao dividindo os lucros
cartao dividindo despesa''')
            cartao_a_ser_removido = str(input('digite o nome do cartao a ser removido: '))
            marina_jogador.lista_de_cartao_marina.remove(cartao_a_ser_removido)
            marina_jogador.mandando_mensagem_automatica_para_marina(nome='joao')

    def excluindo_seguros(self, daniel=False, marina=False):
        if daniel is True:
            print('seguro de vida, seguro de casa, ação, seguro de carro')
            seguro_a_ser_removido = str(input('digite o nome do seguro a ser removido: '))
            daniel_jogador.lista_de_seguros_e_acoes.remove(seguro_a_ser_removido)
            daniel_jogador.mostrando_ativos()
        if marina is True:
            print('seguro de vida, seguro de casa, ação, seguro de carro')
            seguro_a_ser_removido = str(input('digite o nome do seguro a ser removido: '))
            marina_jogador.lista_de_seguros_e_acoes.remove(seguro_a_ser_removido)
            marina_jogador.mostrando_ativos()

    def mandando_mensagem_automatica_para_marina(self, nome):
        pwk.sendwhatmsg_instantly(phone_no=f'{self.lista_de_numeros[nome]}',
                                  message=f'seus cartões são: {marina_jogador.lista_de_cartao_marina}',
                                  wait_time=22
                                  ,
                                  tab_close=True,
                                  close_time=13)
        falar = pyttsx3.init('sapi5')

    def mandando_mensagem_automatica_para_daniel(self, nome):
        pwk.sendwhatmsg_instantly(phone_no=f'{self.lista_de_numeros[nome]}',
                                  message=f'seus cartões são: {daniel_jogador.lista_de_cartao_daniel}',
                                  wait_time=22
                                  ,
                                  tab_close=True,
                                  close_time=13)

    def comprando_acoes_ou_seguros(self, daniel=False, marina=False):
        filhos.linha_vazia()
        print('''[1] - seguro de carro 
[2] - seguro de vida
[3] - seguro de casa
[4] - ação
        ''')
        escolha = str(input('qual seguro voce deseja comprar? ')).lower()
        if daniel is True:
            if escolha == '1':
                daniel_jogador.lista_de_seguros_e_acoes.append('seguro de carro')
            elif escolha == '2':
                daniel_jogador.lista_de_seguros_e_acoes.append('seguro de vida')
            elif escolha == '3':
                daniel_jogador.lista_de_seguros_e_acoes.append('seguro de casa')
            elif escolha == '4':
                daniel_jogador.lista_de_seguros_e_acoes.append('ação')
        elif marina is True:
            if escolha == '1':
                marina_jogador.lista_de_seguros_e_acoes.append('seguro de carro')
            elif escolha == '2':
                marina_jogador.lista_de_seguros_e_acoes.append('seguro de vida')
            elif escolha == '3':
                marina_jogador.lista_de_seguros_e_acoes.append('seguro de casa')
            elif escolha == '4':
                marina_jogador.lista_de_seguros_e_acoes.append('ação')

    def dia_da_sorte(self, marina=False, daniel=False):
        print('[1] = receber 20 mil reais')
        print('[2] = tentar ganhar 300 mil reais')
        escolha = str(input('voce deseja receber 20 mil reais ou tentar ganhar 300 mil? ')).lower()
        if escolha == '1':
            print('ótimo, receba seus 20 mil reais do banco')
        if escolha == '2':
            lista_de_numeros = []
            numero_sorteado_aleatoriamente = ran(1, 10)
            for numeros in range(0, 2):
                numero_escolhido = int(input('digite um número entre de 1 até 10: '))
                lista_de_numeros.append(numero_escolhido)
            for numeros in lista_de_numeros:
                if numeros == numero_sorteado_aleatoriamente:
                    print(
                        f'parabêns, o número sorteado foi: {numero_sorteado_aleatoriamente} e voce sorteou um dos valores,'
                        f' receba 300 mil reais do banco ')
                else:
                    print('pelo jeito voce não sorteou o número certo, uma pena')

    def numero_da_sorte_do_milionario(self, marina=False, daniel=False):
        while True:
            r = str(input('digite enter para sortear o seu número da sorte')).lower()
            if r == '':
                numero_da_sorte = ran(1, 10)
                print(f'seu número da sorte é: {numero_da_sorte}')
                return numero_da_sorte
                break
            else:
                print('digite apenas enter por favor')


filhos = Filhos()
marina_jogador = Filhos()
daniel_jogador = Filhos()
numero_da_sorte = ''
while True:
    r = str(input('DIGITE ENTER: ')).lower()
    if r == 'numero da sorte':
        escolha = str(input('quem deseja escolher o número da sorte? ')).lower()[0]
        if escolha == 'm':
            numero_da_sorte = marina_jogador.numero_da_sorte_do_milionario(marina=True)
        if escolha == 'd':
            numero_da_sorte = daniel_jogador.numero_da_sorte_do_milionario(daniel=True)

    elif r == '':
        n = ran(1, 10)
        frase = f'o número sorteado é: {n}'
        print(frase)
        falar.say(frase)
        falar.runAndWait()
        if n == numero_da_sorte:
            falar_chata = (pyttsx3.init('sapi5'))
            frase_chata = 'voçe rodou o número sorteado do seu oponente, lhe pague vinte e quatro mil reais'
            print(frase_chata)
            falar_chata.say(frase_chata)
            falar_chata.runAndWait()


    elif r == 'fim':
        break
    elif r == 'filhos':
        escolha = str(input('digite de quem é o filho: ')).lower()[0]
        if escolha == 'm':
            marina_jogador.filhos()
        elif escolha == 'd':
            daniel_jogador.filhos()
    elif r == 'contar filhos':
        escolha = str(input('digite de quem voce deseja contabilizar os filhos?  ')).lower()[0]
        if escolha == 'm':
            marina_jogador.valordosfilhos()
        elif escolha == 'd':
            daniel_jogador.valordosfilhos()
    elif r == 'comprar seguros':
        escolha = str(input('digite quem deseja comprrar o seguro/ação? ')).lower()[0]
        if escolha == 'm':
            marina_jogador.comprando_acoes_ou_seguros(marina=True)
        elif escolha == 'd':
            daniel_jogador.comprando_acoes_ou_seguros(daniel=True)
    elif r == 'mostrar seguros':
        escolha = str(input('digite quem vai mostrar os seguros. ')).lower()[0]
        if escolha == 'm':
            marina_jogador.mostrando_ativos(marina=True)
        elif escolha == 'd':
            daniel_jogador.mostrando_ativos(daniel=True)
    elif r == 'mostrar cartoes':
        escolha = str(input('digite quem vai mostrar os cartões. ')).lower()[0]
        if escolha == 'm':
            marina_jogador.mandando_mensagem_automatica_para_marina(nome='joao')
        elif escolha == 'd':
            daniel_jogador.mandando_mensagem_automatica_para_daniel(nome='daniel')
        playsound('are_you_ready.mp3')
    elif r == 'comprar cartoes':
        escolha = str(input('digite quem vai comprar os cartões. ')).lower()[0]
        if escolha == 'm':
            marina_jogador.comprando_cartao(marina=True)
        if escolha == 'd':
            daniel_jogador.comprando_cartao(daniel=True)
    elif r == 'excluir cartoes':
        escolha = str(input('digite quem vai excluir os cartoes. ')).lower()[0]
        if escolha == 'm':
            marina_jogador.excluindo_cartao(marina=True)
        if escolha == 'd':
            daniel_jogador.excluindo_cartao(daniel=True)
    elif r == 'excluir seguros':
        escolha = str(input('digite quem vai excluir os seguros. ')).lower()[0]
        if escolha == 'm':
            marina_jogador.excluindo_seguros(marina=True)
        if escolha == 'd':
            daniel_jogador.excluindo_seguros(daniel=True)
        playsound('are_you_ready.mp3')
    elif r == 'dia da sorte':
        escolha = str(input('digite quem vai realizar o dia da sorte ')).lower()[0]
        if escolha == 'm':
            marina_jogador.dia_da_sorte(marina=True)
        if escolha == 'd':
            daniel_jogador.dia_da_sorte(daniel=True)
