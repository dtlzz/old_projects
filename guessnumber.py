import random
from colorama import Fore
import sys
import time
import subprocess


numb = random.randint(0, 1000)
g1 = numb + 50
g2 = numb - 50
print(r'''
    =/\                 /\=
    / \'._   (\_/)   _.'/ \
   / .''._'--(o.o)--'_.''. \
  /.' _/ |`'=/ " \='`| \_ `.\
 /` .' `\;-,'\___/',-;/` '. '\
/.-'       `\(-V-)/`       `-.\
`            "   "          
''')
print("ready to play? you number is anywhere between "
      + Fore.RED + f'{g2}' + ' ' + Fore.GREEN + f'{g1}')
while 0 in range(1):
    def main():
        while True:
            print("Starting program")
            p = subprocess.Popen(['python', 'guessnumber.py'])
            p.wait()
            print("Program exited")
            time.sleep(5)
    gues = int(input(Fore.CYAN + 'number is (0 to give up): '))
    if gues == 0:
        print(Fore.RED + f'the number was {numb}')

        nuk = input((Fore.WHITE + 'do you want to replay? y for yes'))
        if nuk == 'y':
            main()
        else:
            sys.exit()

    nuu = numb - gues
    if nuu == 0:
        print(Fore.GREEN + 'you got it!!!!!!!!!!!!!!!')
        print(r'''
        *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
        ''')
        nuk = input((Fore.WHITE + 'do you want to replay? y for yes'))
        if nuk == 'y':
            main()
        else:
            sys.exit()

    elif nuu > 200:
        print(Fore.CYAN + "you are far away from the truth")
        if nuu > 0:
            print(Fore.GREEN + "go higher!")
        else:
            print(Fore.RED + "go lower!")
    elif 100 < nuu < 200:
        print(Fore.CYAN + 'getting closer')
        if nuu > 0:
            print(Fore.GREEN + "go higher!")
        else:
            print(Fore.RED + "go lower!")
    elif 100 > nuu > 50:
        print(Fore.CYAN + 'getting very closer')
        if nuu > 0:
            print(Fore.GREEN + "go higher!")
        else:
            print(Fore.RED + "go lower!")

    elif 50 > nuu > 10:
        print(Fore.CYAN + "the truth is nearby")
        if nuu > 0:
            print(Fore.GREEN + "go higher!")
        else:
            print(Fore.RED + "go lower!")

    elif nuu < 10:
        print(Fore.CYAN + 'you are there')
        if nuu > 0:
            print(Fore.GREEN + "go higher!")
        else:
            print(Fore.RED + "go lower!")
