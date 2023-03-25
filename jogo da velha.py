import os
posicao = {}
for i in range(9):
    posicao[i+1]=' '


print('======================================================================================================\n')
#print('JOGO DA VELHA!!\n')
print('   █ █▀▀▀█ █▀▀█ █▀▀▀█   █▀▀▄ █▀▀▄   █   █ █▀▀▀ █    █  █ █▀▀▄')
print('   █ █   █ █ ▄▄ █   █   █  █ █▄▄█    █ █  █▀▀▀ █    █▀▀█ █▄▄█')
print('█▄▄█ █▄▄▄█ █▄▄▀ █▄▄▄█   █▄▄█ █  █    ▀▄▀  █▄▄▄ █▄▄█ █  █ █  █\n')
print('======================================================================================================\n')

print('RESGRA: OS JOGADORES DEVEM ESCOLHER O NUMERO DE ACORDO COM A TABELA AO LADO')
print('E SEGUIR AS INTRUÇÕES QUE APARECEM NA TELA\n')


nome_jogador1=input('informe o nome do 1º jogador: ')
nome_jogador2=input('informe o nome do 2º jogador:  ')

jogador="X"
jogando=True

vitoria = [
          [1, 2, 3],  # Linhas
          [4, 5, 6],
          [7, 8, 9],
     
          [7, 4, 1],  # Colunas
          [8, 5, 2],
          [9, 6, 3],
        
          [7, 5, 3],  # Diagonais 
          [1, 5, 9]
        ]

print('\n')
print('  JOGO ATUAL\t   TABELA GUIA')
print('|---|---|---|\t  |---|---|---|')
print(f'| {posicao[1]} | {posicao[2]} | {posicao[3]} |\t  | 1 | 2 | 3 |')
print('|---|---|---|\t  |---|---|---|')
print(f'| {posicao[4]} | {posicao[5]} | {posicao[6]} |\t  | 4 | 5 | 6 |')
print('|---|---|---|\t  |---|---|---|')
print(f'| {posicao[7]} | {posicao[8]} | {posicao[9]} |\t  | 7 | 8 | 9 |')
print('|---|---|---|\t  |---|---|---|')
print('\n')


while jogando:

  print(f"é a vez do {jogador}: escolha um numero:")
  entrada = int(input())
  if os.name== "nt": 
    os.system('cls')
  else:
    os.system('clear')

  print('======================================================================================================\n')
  print('   █ █▀▀▀█ █▀▀█ █▀▀▀█   █▀▀▄ █▀▀▄   █   █ █▀▀▀ █    █  █ █▀▀▄')
  print('   █ █   █ █ ▄▄ █   █   █  █ █▄▄█    █ █  █▀▀▀ █    █▀▀█ █▄▄█')
  print('█▄▄█ █▄▄▄█ █▄▄▀ █▄▄▄█   █▄▄█ █  █    ▀▄▀  █▄▄▄ █▄▄█ █  █ █  █\n')
  print('======================================================================================================\n')

  print('RESGRA: OS JOGADORES DEVEM ESCOLHER O NUMERO DE ACORDO COM A TABELA AO LADO')
  print('E SEGUIR AS INTRUÇÕES QUE APARECEM NA TELA\n')
  

  if entrada in posicao.keys():
     
 
    if posicao[entrada] == ' ':
        posicao[entrada] = jogador
       
   
        for v in vitoria:
           count = 0
 
           for i in v:
               if posicao[i] == jogador:
                  count = count +1   

           if count == 3:
              print('======================================================================================================\n')
              print('██████╗  █████╗ ██████╗  █████╗ ██████╗ ███████╗███╗   ██╗███████╗')
              print('██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝')
              print('██████╔╝███████║██████╔╝███████║██████╔╝█████╗  ██╔██╗ ██║███████╗')
              print('██╔═══╝ ██╔══██║██╔══██╗██╔══██║██╔══██╗██╔══╝  ██║╚██╗██║╚════██║')
              print('██║     ██║  ██║██║  ██║██║  ██║██████╔╝███████╗██║ ╚████║███████║')
              print('╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝')
              print(f'{nome_jogador1} venceu, tu é um abestado mesmo!!')
              jogando = False
              break
           elif count == 3:
               print('======================================================================================================\n')
               print('██████╗  █████╗ ██████╗  █████╗ ██████╗ ███████╗███╗   ██╗███████╗')
               print('██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝')
               print('██████╔╝███████║██████╔╝███████║██████╔╝█████╗  ██╔██╗ ██║███████╗')
               print('██╔═══╝ ██╔══██║██╔══██╗██╔══██║██╔══██╗██╔══╝  ██║╚██╗██║╚════██║')
               print('██║     ██║  ██║██║  ██║██║  ██║██████╔╝███████╗██║ ╚████║███████║')
               print('╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝')
               print(f'{nome_jogador2} venceu, tu é um abestado mesmo!!')
               jogando = False
               break 
        if (v ==8):
                 print('======================================================================================================\n')
                 print('Deu velha')         

        if jogador=="X":
          jogador="O"  
        else:
          jogador="X" 
           
    else:
         print('======================================================================================================\n')
         print('posicao ja ocupada')            
  else:
      print('======================================================================================================\n')
      print("\nJogada inválida. Tente novamente.\n")

      if jogador==" ":
         print('insira um numero de 1 á 9')
  

  print('  JOGO ATUAL\t   TABELA GUIA')
  print('|---|---|---|\t  |---|---|---|')
  print(f'| {posicao[1]} | {posicao[2]} | {posicao[3]} |\t  | 1 | 2 | 3 |')
  print('|---|---|---|\t  |---|---|---|')
  print(f'| {posicao[4]} | {posicao[5]} | {posicao[6]} |\t  | 4 | 5 | 6 |')
  print('|---|---|---|\t  |---|---|---|')
  print(f'| {posicao[7]} | {posicao[8]} | {posicao[9]} |\t  | 7 | 8 | 9 |')
  print('|---|---|---|\t  |---|---|---|')
  print('\n')