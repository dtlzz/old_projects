import random
print(r'''
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⣿⣿
⣿⣿⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⢰⣿⣿
⣿⣿⣆⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⢸⣿⣿
⣿⣿⡇⠀⠀⠀⠘⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢿⣿⣿⡿⠀⠀⠀⢸⣿⣿
⣿⣿⡿⠿⠓⠂⠸⣿⠋⠀⢀⣠⣤⣾⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣶⣤⡀⠀⠈⣿⡇⠀⠚⠛⢻⣿⣿
⣿⣿⣇⡀⠀⠀⠀⢻⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⡇⣀⣀⣀⣸⣿⣿
⣿⣿⡿⠟⠛⠉⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⢀⣾⣿⣿⣿⣄⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡈⠉⠙⢻⣿⣿
⣿⣿⣇⣠⣴⣾⣿⣿⣿⠋⣽⣿⣿⣿⣿⣿⡿⠿⠿⠟⠿⢿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⠿⠿⠟⠿⠿⢿⣿⣿⣿⣿⣯⡙⢿⣿⣿⣿⣷⣤⣸⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣧⠈⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢿⣿⣿⣿⢿⣿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣀⣠⣤⣤⣤⣤⣄⣀⠀⢀⣴⣿⣿⣿⣿⢸⣿⣿⣿⡎⣿⣿⣿⣷⡄⠀⢀⣀⣤⣤⣤⣤⣤⣤⣙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣽⣿⣿⡿⢋⣾⣿⣿⣿⣧⡹⢿⣿⣋⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣴⣿⣿⣿⣿⣿⣿⣿⣦⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠙⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠙⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠉⠉⠙⢿⣿⣿⣿⣿⣿⠟⠉⠁⠈⠉⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿
⣿⣿⡿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠿⣿⣿
⣿⣿⡇⠈⠻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠁⠀⣿⣿
⣿⣿⡇⠀⠀⠙⣷⣦⣤⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⣴⣿⡟⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⠉⠀⠈⠉⠙⠛⠛⠷⠶⠶⠶⠶⠞⠛⠛⠉⠉⠉⠉⠉⢩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

  _______________________________________________________________
      A R E   Y O U   A    O N E    O R   A   Z E R O ? 
  _______________________________________________________________

''')
var = input('ready to see? ')
va = random.randint(0,1)
if va == 0:
    print(r'''
    ----- computer says you are a:
    
          _____                    _____                    _____                   _______         
         /\    \                  /\    \                  /\    \                 /::\    \        
        /::\    \                /::\    \                /::\    \               /::::\    \       
        \:::\    \              /::::\    \              /::::\    \             /::::::\    \      
         \:::\    \            /::::::\    \            /::::::\    \           /::::::::\    \     
          \:::\    \          /:::/\:::\    \          /:::/\:::\    \         /:::/~~\:::\    \    
           \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \       /:::/    \:::\    \   
            \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \     /:::/    / \:::\    \  
             \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \   /:::/____/   \:::\____\ 
              \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ |:::|    |     |:::|    |
_______________\:::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    ||:::|____|     |:::|    |
\::::::::::::::::::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____| \:::\    \   /:::/    / 
 \::::::::::::::::/____/  \:::\   \:::\   \/____/  \/____|:::::\/:::/    /   \:::\    \ /:::/    /  
  \:::\~~~~\~~~~~~         \:::\   \:::\    \            |:::::::::/    /     \:::\    /:::/    /   
   \:::\    \               \:::\   \:::\____\           |::|\::::/    /       \:::\__/:::/    /    
    \:::\    \               \:::\   \::/    /           |::| \::/____/         \::::::::/    /     
     \:::\    \               \:::\   \/____/            |::|  ~|                \::::::/    /      
      \:::\    \               \:::\    \                |::|   |                 \::::/    /       
       \:::\____\               \:::\____\               \::|   |                  \::/____/        
        \::/    /                \::/    /                \:|   |                   ~~              
         \/____/                  \/____/                  \|___|                        
    ''')
else:
    print(r'''
    ----- computer says you are a: 
    
         _______                   _____                    _____                                   
        /::\    \                 /\    \                  /\    \                                  
       /::::\    \               /::\____\                /::\    \                                 
      /::::::\    \             /::::|   |               /::::\    \                                
     /::::::::\    \           /:::::|   |              /::::::\    \                               
    /:::/~~\:::\    \         /::::::|   |             /:::/\:::\    \                              
   /:::/    \:::\    \       /:::/|::|   |            /:::/__\:::\    \                             
  /:::/    / \:::\    \     /:::/ |::|   |           /::::\   \:::\    \                            
 /:::/____/   \:::\____\   /:::/  |::|   | _____    /::::::\   \:::\    \                           
|:::|    |     |:::|    | /:::/   |::|   |/\    \  /:::/\:::\   \:::\    \                          
|:::|____|     |:::|    |/:: /    |::|   /::\____\/:::/__\:::\   \:::\____\                         
 \:::\    \   /:::/    / \::/    /|::|  /:::/    /\:::\   \:::\   \::/    /                         
  \:::\    \ /:::/    /   \/____/ |::| /:::/    /  \:::\   \:::\   \/____/                          
   \:::\    /:::/    /            |::|/:::/    /    \:::\   \:::\    \                              
    \:::\__/:::/    /             |::::::/    /      \:::\   \:::\____\                             
     \::::::::/    /              |:::::/    /        \:::\   \::/    /                             
      \::::::/    /               |::::/    /          \:::\   \/____/                              
       \::::/    /                /:::/    /            \:::\    \                                  
        \::/____/                /:::/    /              \:::\____\                                 
         ~~                      \::/    /                \::/    /                                 
                                  \/____/                  \/____/                                  
                                                                  
    
    ''')