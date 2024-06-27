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
 

def begin():
  center = '1 - Start   |   2 - Exit'
  print('-'*100)
  print('\033[1;40;31m {:^98} \033[m'.format(center))
  print('-'*100)
  while True:
    start = input('Choose: [1/2] ')
    if start == '1':
      print('Well done')
      break
    elif start == '2':
      print('See you next time')
      break
    else:
      print('Uncknown value! Try again')
  
