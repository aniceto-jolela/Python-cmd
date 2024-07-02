from uteis.game.http_error import begin, welcome

print(' 1º http_error \n 2º [...]')
status = int(input('Which game do you want to play? '))
match(status):
  case 1:
    welcome()
    begin()
  case 2:
    print('Still to build')
  case _:
    raise ValueError('Not a point')
  