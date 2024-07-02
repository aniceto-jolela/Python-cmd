import random

def welcome():
  """
  Prints a welcome message.
  """
  name = ' Welcome in the game'
  print('.='*40)
  print('\033[31;40m {:^78} \033[m'.format(name))
  print('.='*40)
  print('\033[31m Rules: \033[m')
  print('HTTP status codes indicate the result of a specific HTTP request. \n'+ 
  'They are grouped into five classes:')
  print("""
  1. \033[1;34m Informational Responses (100 – 199): \033[m These responses are tentative and indicate that 
  the request is in progress. 
  Examples include the 100 Continue code and 101 Switching Protocols.
  
  2. \033[1;34m Successful Responses (200 – 299): \033[m Indicates that the request was completed successfully. 
  The 200 OK code is the most common and means the request was successful.

  3. \033[1;34m Redirect Messages (300 – 399): \033[m These codes indicate that the 
  customer must take additional actions to complete the request. 
  Examples include 301 Moved Permanently and 302 Found.

  4. \033[1;34m Client Error Responses (400 – 499): \033[m Indicate that there was an error in the client request.
  For example, the code 404 Not Found means that the resource was not found.
  
  5. \033[1;34m Server Error Responses (500 – 599): \033[m Indicate that a server error occurred while processing     the request. 
  The 500 Internal Server Error code is an example.
 
  """)
  print(' \033[4;33m Notice.: You will have to get at least 3 classes correct to win the game \033[m')
  print('\033[31m Write 6 to end the game. \033[m')
 

def begin():
  """
  This function is used to start the game.
  """
  center = 'Player (1)  |  Player (2)   |   3 - Exit'
  game = 'Game'
  print('{:^98}'.format(game))
  print('-'*100)
  print('\033[1;40;31m {:^98} \033[m'.format(center))
  print('-'*100)
  while True:
    start = input('Choose: [1/2/3] ')
    if start == '1':
      player1()
      break
    elif start == '2':
      player2()
      break
    elif start == '3':
      print('See you next time')
      break
    else:
      print('Uncknown value! Try again')

def player1():
  error = ['1 - Informational Responses (100 – 199)', '2 - Successful Responses (200 – 299)', '3 - Redirect Messages (300 – 399)', '4 - Client Error Responses (400 – 499)', '5 - Server Error Responses (500 – 599)']
  status = {'player': '', 'win': 0, 'point': 10, 'lose': 0, 'attempts': 0}
  player = input('Write your name: ')
  status[player] = player
  count = 1
  def restart():
    status['win'] = 0
    status['point'] = 10
    status['lose'] = 0
    status['attempts'] = 0
    count = 1
  
  while True:
    print('Which class am I thinking about [1/5] ?')
    print(f'\033[1;34m {error[0]} \n {error[1]} \n {error[2]} \n {error[3]} \n {error[4]} \033[m')
    print('-'* 40)
    rand = random.randint(1, 5)
    status['point'] -= 1
    n = int(input('Choose: '))
    if rand == n:
      print('\033[33m You are right! \033[m')
      status['win'] += 1
      if status['win'] == 3:
        details(status[player], status['win'],  status['point'], status['lose'], status['attempts'])
        print('\033[32m You win! You are to be congratulated. 3 coins \033[m')
        ans = input('Do you want to continue? [S/N] ')
        if ans == 'S':
          restart()
          details(status[player], status['win'], status['point'], status['lose'], status['attempts'])
          continue
        else:
          break
      else:
        detail = input('Do you want to see the Status? [S/N] ')
        if detail == 'S':
          details(status[player], status['win'], status['point'], status['lose'], status['attempts'])
    elif status['point'] == 0:
      print('Your points are over! You lose!')
      status['attempts'] = 2
      ans = input('Do you want to restart? [S/N] ')
      if ans == 'S':
        restart()
        details(status[player], status['win'], status['point'], status['lose'], status['attempts'])
        continue
      else:
        details(status[player], status['win'], status['point'], status['lose'], status['attempts'])
        break
    elif count == 5:
      status['attempts'] = 1
      ans = input('Do you want to continue? [S/N] ')
      if ans == 'S':
        count = 0
      else:
        details(status[player], status['win'], status['point'], status['lose'], status['attempts'])
        print('See you next time!')
        break
    elif n == 6:
      details(status[player], status['win'], status['point'], status['lose'], status['attempts'])
      print('Thanks for playing')
      break
    else:
      status['lose'] += 1
      print('\033[31m You are wrong! \033[m')
    count += 1
   
     
def player2():
      error = ['1 - Informational Responses (100 – 199)', '2 - Successful Responses (200 – 299)', '3 - Redirect Messages (300 – 399)', '4 - Client Error Responses (400 – 499)', '5 - Server Error Responses (500 – 599)']
      status = [{'player': '', 'win': 0, 'point': 10, 'lose': 0},{'player': '', 'win': 0, 'point': 10, 'lose': 0}]
      player1 = input('Write your name - player 1 : ')
      player2 = input('Write your name - player 2 : ')
      status[0]['player'] = player1
      status[1]['player'] = player2
      attempts = 0
      count = 1
      pair = 2
      p = 0
      key = 0
      def restart():
        status[0]['player'] = player1
        status[0]['win'] = 0
        status[0]['point'] = 5
        status[0]['lose'] = 0
        status[1]['player'] = player2
        status[1]['win'] = 0
        status[1]['point'] = 5
        status[1]['lose'] = 0
        attempts = 0
        count = 1

      while True:
        print('Which class am I thinking about [1/5] ?')
        print(f'\033[1;34m {error[0]} \n {error[1]} \n {error[2]} \n {error[3]} \n {error[4]} \033[m')
        print('-'* 40)
        if pair%2 == 0:
          rand = random.randint(1, 5)
          status[0]['point'] -= 1
          key = 0
          p = int(input('1º player - Choose: '))
        else:
          status[1]['point'] -= 1
          p = int(input('2º player - Choose: '))
          key = 1
        
        if rand == p:
          print('\033[33m You are right! \033[m')
          status[key]['win'] += 1
          if status[key]['win'] == 3:
            details2(status[0]['player'], status[0]['win'], status[0]['point'], status[0]['lose'], status[1]['player'], status[1]['win'], status[1]['point'], status[1]['lose'], attempts)
            print('\033[32m You win! You are to be congratulated. 3 coins \033[m')
            ans = input('Do you want to continue? [S/N] ')
            if ans == 'S':
              restart()
              details2(status[0]['player'], status[0]['win'], status[0]['point'], status[0]['lose'], status[1]['player'], status[1]['win'], status[1]['point'], status[1]['lose'], attempts)
              continue
            else:
              break
          else:
            detail = input('Do you want to see the Status? [S/N] ')
            if detail == 'S':
              details2(status[0]['player'], status[0]['win'], status[0]['point'], status[0]['lose'], status[1]['player'], status[1]['win'], status[1]['point'], status[1]['lose'], attempts)
        elif status[0]['point'] == 0 and status[1]['point'] == 0:
          print('\033[31m Your points are over! You lose! \033[m')
          attempts = 2
          ans = input('Do you want to restart? [S/N] ')
          if ans == 'S':
            restart()
            details2(status[0]['player'], status[0]['win'], status[0]['point'], status[0]['lose'], status[1]['player'], status[1]['win'], status[1]['point'], status[1]['lose'], attempts)
            continue
          else:
            details2(status[0]['player'], status[0]['win'], status[0]['point'], status[0]['lose'], status[1]['player'], status[1]['win'], status[1]['point'], status[1]['lose'], attempts)
            break
        elif count == 5:
          attempts = 1
          ans = input('Do you want to continue? [S/N] ')
          if ans == 'S':
            count = 0
          else:
            details2(status[0]['player'], status[0]['win'], status[0]['point'], status[0]['lose'], status[0]['attempts'],status[1]['player'], status[1]['win'], status[1]['point'], status[1]['lose'], attempts)
            print('See you next time!')
            break
        elif p == 6:
          details2(status[0]['player'], status[0]['win'], status[0]['point'], status[0]['lose'],status[1]['player'], status[1]['win'], status[1]['point'], status[1]['lose'], attempts)
          print('Thanks for playing')
          break
        else:
          status[key]['lose'] += 1
          print('\033[31m You are wrong! \033[m')
        count += 1
        pair += 1


def details(player = '', win = 0, point = 0, lose = 0, attempts = 0):
  """
  -> Prints the status of the player
  :param player: name of the player
  :param win: number of wins
  :param point: number of points
  :param lose: number of loses
  :param attempts: number of attempts
  :return: None
  """
  states = 'Status'
  print('-' * 40)
  print('{:^40}'.format(states))
  print('-' * 40)
  print(f'Player: {player}')
  if win == 2:
    print('\033[33m Almost there! 2 coins \033[m')
  elif win == 1:
    print('\033[33m took 1 coin!  \033[m')
  elif win == 0:
    print('\033[31m 0 coin!  \033[m')
  print(f'Loses: {lose}')
  print(f'Points: {point}')
  print(f'Attemps: {attempts}')
  print('-' * 40)


def details2(player = '', win = 0, point = 0, lose = 0, player2 = '', win2 = 0, point2 = 0, lose2 = 0, attempts = 0):
  """
  -> Prints the status of the players 1 and 2
  :param player: name of the player
  :param win: number of wins
  :param point: number of points
  :param lose: number of loses
  :param attempts: number of attempts
  :return: None
  :param player2: name of the player
  :param win2: number of wins
  :param point2: number of points
  :param lose2: number of loses
  :param attempts2: number of attempts
  :return: None
  """
  states = 'Player 1 : Status'
  print('~' * 40)
  print('{:^40}'.format(states))
  print('-' * 40)
  print(f'Player: {player}')
  if win == 2:
    print('\033[33m Almost there! 2 coins \033[m')
  elif win == 1:
    print('\033[33m took 1 coin!  \033[m')
  elif win == 0:
    print('\033[31m 0 coin!  \033[m')
  print(f'Loses: {lose}')
  print(f'Points: {point}')
  
  states2 = 'Player 2 : Status'
  print('-' * 40)
  print('{:^40}'.format(states2))
  print('-' * 40)
  print(f'Player: {player2}')
  if win2 == 2:
    print('\033[33m Almost there! 2 coins \033[m')
  elif win2 == 1:
    print('\033[33m took 1 coin!  \033[m')
  elif win2 == 0:
    print('\033[31m 0 coin!  \033[m')
  print(f'Loses: {lose2}')
  print(f'Points: {point2}')
  print('~' * 40)
  print(f'Attemps: {attempts}')
  print('-' * 40)