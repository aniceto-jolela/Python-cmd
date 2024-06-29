import random

def welcome():
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
  status = {'player': '', 'win': 0, 'lose': 0, 'attempts': 0}
  player = input('Write your name: ')
  status[player] = player
  win = 0
  winner = 1
  count = 1
  
  while True:
    print('Which class am I thinking about [1/5] ?')
    print(f'\033[1;34m {error[0]} \n {error[1]} \n {error[2]} \n {error[3]} \n {error[4]} \033[m')
    print('-'* 40)
    rand = random.randint(1, 5)
    n = int(input('Choose: '))
    if rand == n:
      print('\033[33m You are right! \033[m') 
    elif win == 3:
      status['win'] = winner + 1
      print(status.items)
      print('\033[32m You win! \033[m')
      win = 0
    elif count == 5:
      ans = input('Do you want to continue [s/n]? ')
      if ans == 's':
         count = 0
      else:
        print(status.items())
        print('See you next time!')
        break
    elif n == 6:
      print(status.items())
      print('Thanks for playing')
      break
    else:
      print('\033[31m You are wrong! \033[m')
      win = 0
      winner = 0
    count += 1
    win += 1
    
    
def player2():
    error = ['1 - Informational Responses (100 – 199)', '2 - Successful Responses (200 – 299)', '3 - Redirect Messages (300 – 399)', '4 - Client Error Responses (400 – 499)', '5 - Server Error Responses (500 – 599)']
    status = {'player': '', 'win': 0, 'lose': 0, 'attempts': 0}
    player = input('Write your name: ')
    status[player] = player
    win = 1
    winner = 1
    count = 1

    while True:
      print('Which class am I thinking about [1/5] ?')
      print(f'\033[1;34m {error[0]} {error[1]} {error[2]} \n {error[3]} {error[4]} \033[m')
      print('-'* 40)
      rand = random.randint(1, 5)
      n = int(input('Choose: '))
      if rand == n:
        print('\033[33m You are right! \033[m') 
      elif win == 3:
        status['win'] = winner + 1
        print(status.values)
        print('\033[32m You win! \033[m')
        win = 0
      elif count == 5:
        ans = input('Do you want to continue [s / n]?')
        if ans == 's':
           count = 0
        else:
          print(status.items())
          print('See you next time!')
          break
      elif n == 6:
        print('Thanks for playing')
        break
      else:
        print('\033[31m You are wrong! \033[m')
        win = 0
        winner = 0
        break
      count += 1
      win += 1