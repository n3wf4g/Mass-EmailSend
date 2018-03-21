#Important: install the email_to and colorama module
#Made by Ang33l

import email_to
import colorama
from colorama import Fore as F
from colorama import init
init()
lista = input('Email List: ')
lista = open(lista, 'r').readlines()
lista = [linha.replace('\n',"") for linha in lista]

for linha in lista:

  server = email_to.EmailServer('smtp.gmail.com', 587, 'yourgooglemail@gmail.com', 'yourgooglepass')
  server.quick_email(linha, 'Message title',
                    ['# Blue text', 'Something text'],
                    style='h1 {color: blue}')
  print(F.BLUE + '---------[ Email Send To: ' + linha + ' ---------]')
