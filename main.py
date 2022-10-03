import random, sys, os, time

number_of_ties = 0
number_of_wins = 0
number_of_loses =  0
m = 0
p = 0

def main_menu():
    print('''    
     ╔══════════════════════════════════════════════════════════════════════════╗
     ║                         WELLCOME TO SIMPLE GAMES                         ║
     ╚══════════════════════════════════════════════════════════════════════════╝
       
''')

def all_games():
    print('''
     ╔══════════════════════════════════╦═══════════════════════════════════════╗                          
     ║  All Games:                      ║             Description               ║
     ║                                  ║                                       ║
     ║  1 ► Guess the number            ║  Try to guess the random number the   ║
     ║                                  ║  computer generates                   ║
     ║                                  ║                                       ║
     ║  2 ► Rock, Paper, Scissors       ║  Play rock, paper, scissors vs the    ║
     ║                                  ║  computer.                            ║
     ║                                  ║                                       ║
     ║  Q ► EXIT                        ║  Leaves the program instant.          ║
     ║                                  ║                                       ║
     ╚══════════════════════════════════╩═══════════════════════════════════════╝   

''')

def error():
    print('     [-] ERROR. NOT A VALID OPTION')
    game_selector()

def game_selector():
    game = input('     • SELECT A GMAE BY INTRODUCCIG THE GAME NUMBER >> ')
    if game.lower() == 'q':
        sys.exit()
    elif game == '1':
        guess()
    elif game == '2':
        rps()
    else:
        error()

def guess_menu():
    print('''
     ╔══════════════════════════════════════════════════════════════════════════╗
     ║                     GUESS THE NUMBER BETWEEN  0 - 20                     ║
     ╚══════════════════════════════════════════════════════════════════════════╝

''')

def guess():
    os.system('clear || cls')
    n = random.randint(1,20)
    trys = 0
    guess_menu()
    while True:
        guess = input('     • SELECT A NUMBER BETWEEN 0 - 20 OR PRESS Q TO EXIT  >>  ')
        os.system('clear || cls')
        guess_menu()
        trys = trys + 1
        if guess == 'q':
            break
        try:
            guess = int(guess)
        except:
            print('     [-] UNKNOWN VALUE. TRY A NUMBER OR PRESS Q TO EXIT')
            trys = trys - 1
            guess = str(guess)
        try:
            if guess >= 1 and guess <= 20:
                if guess == n:
                    print(f'    GOD JOB! YOU GUESSED MY NUMBER IN {trys} TRYS')
                    cont = input('    • YOU WHANT TO PLAY AGAIN ?  Y/N >>  ')
                    if cont.lower() == 'y':
                        continue
                    elif cont.lower() == 'n':
                        print('    GOING BACK TO THE MENU')
                        time.sleep(2)
                        break
                    else:
                        print('    [-] WRONG VALUE. NEXT TIME TRY WITH Y/N')
                        print('    [-] GOING BACK TO THE MENU')
                        time.sleep(2)
                        break
                elif guess > n:
                    print(F'     THE NUMBER IS LESS THAN {guess}')
                    continue
                elif guess < n:
                    print(F'     THE NUMBER IS MORE THAN {guess}')
                    continue
        except:
            continue
        else:
            print('     [-] VALUE TO HIGH OR LOW. TRY A NUMBER BETWEEN 0 - 20')
            trys = trys - 1

def rps_menu():
        print('''
     ╔══════════════════════════════════════════════════════════════════════════╗
     ║                    LET'S GO PLAY ROCK, PAPER, SCISSORS                   ║
     ╚══════════════════════════════════════════════════════════════════════════╝

''')

def rps():
    while True:
        global m,p,number_of_loses,number_of_ties,number_of_wins
        os.system('clear || cls')
        rps_menu()
        m = random.choice(['r','p','s'])
        p = input('     • SELECT ROCK (r), PAPER (p), SCISSORS (s), QUIT (q) >>  ')
        p = p.lower()
        if p == 'q':
            break
        print(f'     YOU CHOSE [{p.upper()}] AND THE COMPUTER CHOSES [{m.upper()}]')
        if p == m:
            print(f'     YOU TIE')
            number_of_ties = number_of_ties + 1
        elif p == 'r' and m == 'p':
            print(f'     YOU LOSS')
            number_of_loses = number_of_loses + 1
        elif p == 'r' and m == 's':
            print(f'     YOU WIN')
            number_of_wins = number_of_wins + 1
        elif p == 'p' and m == 's':
            print(f'     YOU LOSS')
            number_of_loses = number_of_loses + 1
        elif p == 'p' and m == 'r':
            print(f'     YOU WIN')
            number_of_wins = number_of_wins + 1   
        elif p == 's' and m == 'r':
            print(f'     YOU LOSS')
            number_of_loses = number_of_loses + 1
        elif p == 's' and m == 'p':
            print(f'     YOU WIN')
            number_of_wins = number_of_wins + 1
        else:
            print(f'     [-] WRONG VALUE.')

        print(f'     {number_of_wins} WINS, {number_of_loses} LOSES, {number_of_ties} TIES')
        con = input('     • YOU WHANT TO PLAY AGAIN ?  Y/N >>  ')
        con = con.lower()
        if con == 'y':
            continue
        elif con == 'n':
            break
        else:
            print('     [-] WRONG VALUE. NEXT TIME TRY WITH Y/N')
            print('     [-] GOING BACK TO THE MENU.')
            time.sleep(2)
            break

def main():
    while True:
        os.system('clear || cls')
        main_menu()
        all_games()
        game_selector()

if __name__ == '__main__':
    main()