
from random import choice
from time import sleep

cores = {
    'Limpar': '\033[m',
    'Vermelho': '\033[31m',
    'Verde': '\033[32m',
    'Amarelo': '\033[33',
    'Azul': '\033[34m'
}

# O computador da a sua jogada
lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista)

print('Suas opçoes:\n[ 1 ] - PEDRA\n[ 2 ] - PAPEL\n[ 3 ] - TESOURA')
jogador = int(input('Qual é a sua jogada: '))
print('JO\nKEN\nPO!!!')
# -----------------------------------------------------------------------------------------------------------------------
if computador == 'Pedra' and jogador == 3:  # Pedra > Tesoura = Computador vence
    print('-=' * 12)
    print('Computador jogou Pedra')
    print('Jogador jogou Tesoura')
    print('-=' * 12)
    print('{}COMPUTADOR VENCE{}'.format(cores['Azul'], cores['Limpar']))
elif computador == 'Tesoura' and jogador == 1:  # Tesoura < Pedra = Jogador vence
    print('-=' * 12)
    print('Computador jogou Tesoura')
    print('Jogador jogou Pedra')
    print('-=' * 12)
    print('{}JOGADOR VENCE{}'.format(cores['Verde'], cores['Limpar']))
elif computador == 'Pedra' and jogador == 1:  # Pedra == Pedra = Empate
    print('-=' * 12)
    print('Computador jogou Pedra')
    print('Jogador jogou Pedra')
    print('-=' * 12)
    print('{}EMPATE{}'.format(cores['Amarelo'], cores['Limpar']))
# ----------------------------------------------------------------------------------------------------------------------
elif computador == 'Papel' and jogador == 1:  # Papel > Pedra = Computador vence
    print('-=' * 12)
    print('Computador jogou Papel')
    print('Jogador jogou Pedra')
    print('-=' * 12)
    print('{}COMPUTADOR VENCE{}'.format(cores['Azul'], cores['Limpar']))
elif computador == 'Pedra' and jogador == 2:  # Pedra < Papel = Jogador vence
    print('-=' * 12)
    print('Computador jogou Pedra')
    print('Jogador jogou Papel')
    print('-=' * 12)
    print('{}JOGADOR VENCE{}'.format(cores['Verde'], cores['Limpar']))
elif computador == 'Papel' and jogador == 2:  # Papel == Papel = Empate
    print('-=' * 12)
    print('Computador Jogou Papel')
    print('Jogador jogou Papel')
    print('-=' * 12)
    print('{}EMPATE{}'.format(cores['Amarelo'], cores['Limpar']))
# ----------------------------------------------------------------------------------------------------------------------
elif computador == 'Tesoura' and jogador == 2:  # Tesoura > Papel = Computador vence
    print('-=' * 12)
    print('Computador jogou Tesoura')
    print('Jogador jogou Papel')
    print('-=' * 12)
    print('{}COMPUTADOR VENCE{}'.format(cores['Azul'], cores['Limpar']))
elif computador == 'Papel' and jogador == 3:  # Papel < Tesoura = Jogador vence
    print('-=' * 12)
    print('Computador jogou Papel')
    print('Jogador jogou Tesoura')
    print('-=' * 12)
    print('{}JOGOADOR VENCE{}'.format(cores['Verde'], cores['Limpar']))
elif computador == 'Tesoura' and jogador == 3:  # Tesoura == Tesoura = Empate
    print('-=' * 12)
    print('Computador jogou Tesoura')
    print('Jogador jogou Tesoura')
    print('-=' * 12)
    print('{}EMPATE{}'.format(cores['Amarelo'], cores['Limpar']))
