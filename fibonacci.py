a, b, c = 0, 1, 0


def show():
    print('*'*45)
    print('Welcome to fibonacci:')
    print('*'*45)
    sh = int(input('choose the option: \n '
                   '1º Only? \n 2º Start and End? \n '))
    if sh == 1:
        n = int(input('fibonacci: '))
        fibonacci(n)
    elif sh == 2:
        start = int(input('fibonacci [start]: '))
        end = int(input('fibonacci [end]: '))
        fibonacci(0, start, end)
    else:
        print('\033[31m Error! \033[m')


def fibonacci(only=0, start=0, end=0):
    global a, b, c

    if only != 0 and start != 0 and end != 0:
        return print('\033[34m Warning! \033[m \n enter the start and end value or just only.')
    elif only > 0 and start == 0 and end == 0:
        a = 0
        c = only
        return fibonaccipositive(a, c)
    elif start < end and only == 0:
        a = start
        c = end
        return fibonaccipositive(a, c)
    elif start > end and only == 0:
        a = start
        c = end
        return fibonaccinegative(a, c)


def fibonaccipositive(pa=0, pc=0):
    global b
    while pa < pc:
        print(pa)
        pa, b = b, pa + b


def fibonaccinegative(na=0, nc=0):
    global b
    while na > nc:
        print(na)
        na, b = b, na - b


show()