import time
from unicodedata import digit

t = input('Digite um número: (Em segundos)')

if t.isdigit():
    t = int(t)
else:
    print('Resultado inválido!')
    

while t != 0:
    minutes, seconds = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(timer, end='\r')
    time.sleep(1)
    t = t - 1

print('O TEMPO ACABOU')