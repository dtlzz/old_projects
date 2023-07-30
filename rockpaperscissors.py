import random
import os
import sys

print(r"""
    - (1) for rock:

        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    - (2) for paper:

        _______
    ---'    ____)____
              ______)
             _______)
             _______)
    ---.__________)
    
    - (3) for scissors:

       _______
    ---'  ____)____
             ______)
         __________)
          (____)
    ---.__(___)
""")
you = int(input('    1- rock\n    2- paper\n    3- scissors\n    ---- you choose--------\n    : '))
opp = random.randint(1, 3)
if you == opp:
    if you == 1:
        print(r"""
    - you chose:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    
    - computer chose:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    ------ that's a draw ------
            """)

        rerun = input('play again? (n for no)').lower()
        if rerun == 'n':
            sys.exit()
        else:
            var = sys.executable
            os.execl(var, var, *sys.argv)

    if you == 2:
        print(r"""
    - you chose:
        _______
    ---'    ____)____
              ______)
             _______)
             _______)
    ---.__________)
    
    
    - computer chose:
        _______
    ---'    ____)____
              ______)
             _______)
             _______)
    ---.__________)
    
    ------ that's a draw ------
    """)

        rerun = input('play again? (n for no)').lower()
        if rerun == 'n':
            sys.exit()
        else:
            var = sys.executable
            os.execl(var, var, *sys.argv)

    if you == 3:
        print(r"""
    - you chose:
    
       _______
    ---'  ____)____
             ______)
         __________)
          (____)
    ---.__(___)
        
        
    - computer chose:
    
       _______
    ---'  ____)____
             ______)
         __________)
          (____)
    ---.__(___)
    
    ------ that's a draw ------
        """)

        rerun = input('play again? (n for no)').lower()
        if rerun == 'n':
            sys.exit()
        else:
            var = sys.executable
            os.execl(var, var, *sys.argv)

else:
    if you == 1 and opp == 2:
        print(r"""
    - you chose:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    - computer chose:
        _______
    ---'    ____)____
              ______)
             _______)
             _______)
    ---.__________)
    
    ------ you lose ------    
        """)

        rerun = input('play again? (n for no)').lower()
        if rerun == 'n':
            sys.exit()
        else:
            var = sys.executable
            os.execl(var, var, *sys.argv)

    if you == 1 and opp == 3:
        print(r"""
    - you chose:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    - computer chose:
    
       _______
    ---'  ____)____
             ______)
         __________)
          (____)
    ---.__(___)
    
    ------ you won ------  
      """)

        rerun = input('play again? (n for no)').lower()
        if rerun == 'n':
            sys.exit()
        else:
            var = sys.executable
            os.execl(var, var, *sys.argv)

    if you == 2 and opp == 1:
        print(r"""
    - you chose:
        _______
    ---'    ____)____
              ______)
             _______)
             _______)
    ---.__________)
    
    
    - computer chose:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    ------ you won ------ 
           """)

        rerun = input('play again? (n for no)').lower()
        if rerun == 'n':
            sys.exit()
        else:
            var = sys.executable
            os.execl(var, var, *sys.argv)

    if you == 3 and opp == 1:
        print(r"""
    - you chose:
    
       _______
    ---'  ____)____
             ______)
         __________)
          (____)
    ---.__(___)
    

    - computer chose:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    ------ you lose ------   
        """)

        rerun = input('play again? (n for no)').lower()
        if rerun == 'n':
            sys.exit()
        else:
            var = sys.executable
            os.execl(var, var, *sys.argv)

    if you == 2 and opp == 3:
        print(r"""
    - you chose:
        _______
    ---'    ____)____
              ______)
             _______)
             _______)
    ---.__________)
    
    
    - computer chose:
    
       _______
    ---'  ____)____
             ______)
         __________)
          (____)
    ---.__(___)
    
    ------ you won ------
    """)

        rerun = input('play again? (n for no)').lower()
        if rerun == 'n':
            sys.exit()
        else:
            var = sys.executable
            os.execl(var, var, *sys.argv)

    if you == 3 and opp == 2:
        print(r"""
    - you chose:
    
       _______
    ---'  ____)____
             ______)
         __________)
          (____)
    ---.__(___)
    
    
    - computer chose:
        _______
    ---'    ____)____
              ______)
             _______)
             _______)
    ---.__________)
    
    ------ you lose ------ 
        """)
        rerun = input('play again? (n for no)').lower()
        if rerun == 'n':
            sys.exit()
        else:
            var = sys.executable
        os.execl(var, var, *sys.argv)
