"""
Author: Parthiv Patel, pate1459@purdue.edu
Assignment: 12.1 Pyword
Date: 04/9/2022

Description:
    The program allows users to play the game Jotto while keeping a leaderboard and tracking the user's points.

Contributors:
    N/A

My contributor(s) helped me:
    [X] understand the assignment expectations without
        telling me how they will approach it.
    [X] understand different ways to think about a solution
        without helping me plan my solution.
    [X] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""

import random


"""Write new functions below this line (starting with unit 4)."""


def pick_game_words(converted_list):

    list_of_words = []


    random_index = random.randrange(len(converted_list))
    list_of_words.append(converted_list[random_index])
    random_index = random.randrange(len(converted_list))
    list_of_words.append(converted_list[random_index])
    random_index = random.randrange(len(converted_list))
    list_of_words.append(converted_list[random_index])

    return list_of_words


def hall_of():
    res = {}
    score = []
    name = []
    print()
    print("--- Hall of Fame ---")
    print(" ## : Score : Player")
    with open("hall_of_fame.txt") as file:
        for line in file:
            score.append(line.split(',')[0])
            line.strip()
            line = line.strip()
            name.append(line.split(', ')[1])

    
    #for element in inputfile:
    #    newlst.append(element.strip())

    #res = dict(s.split(", ") for s in newlst)

    topTenKey = list(score)[:10]
    topTenVal = list(name)[:10]



    #if (topTenKey[0] == "96" and topTenVal[0] == "John"):
    #    print(f"{(1):>3}"+ " :" + f"{topTenKey[0]:>6}" + " : " + topTenVal[0])
    #    print(f"{(2):>3}"+ " :" + f"{topTenKey[0]:>6}" + " : " + topTenVal[0])

    for i in range(len(topTenKey)):
        tempkey = topTenKey[i].replace("[","").replace("]","")
        tempval = topTenVal[i].replace("[","").replace("]","")
        tempval=tempval.replace("'", "")

        print(f"{(i + 1):>3}"+ " :" + f"{tempkey:>6}" + " : " + tempval)


def emp(alphabet):
    alphabet = {"a": " ","b": " ","c": " ","d": " ","e": " ","f": " ","g": " ","h": " ","i": " ","j": " ","k": " ","l": " ","m": " ", "n": " ","o": " ","p": " ","q": " ","r": " ","s": " ","t": " ","u": " ","v": " ","w": " ","x": " ","y": " ","z": " "}

    return alphabet
    

    
            
def main():
    
    my_file = open("words.txt", "r")
    converted_list = []
    content_list = my_file.readlines()
    for element in content_list:
        converted_list.append(element.strip())
    loop = 0
    score = 0
    loop2 = 0
    special_char = "!@#$%^&*()-+?_=,<>/"
    alphabet = {"a": " ","b": " ","c": " ","d": " ","e": " ","f": " ","g": " ","h": " ","i": " ","j": " ","k": " ","l": " ","m": " ", "n": " ","o": " ","p": " ","q": " ","r": " ","s": " ","t": " ","u": " ","v": " ","w": " ","x": " ","y": " ","z": " "}
    res = {}
    scorelist = []
    namelist = []
    game_words = pick_game_words(converted_list)
    print("Welcome to PyWord.")
    while (loop == 0):
        print()
        print("----- Main Menu -----")
        print("1. New Game")
        print("2. See Hall of Fame")
        print("3. Quit")
        print()
        a = input("What would you like to do? ")
        if (a == '1'):
            loop = 0
            name = input("Enter your player name: ")
            print()
            turns = 0
            for round in range(3):
                print("Round " + str(round + 1) + ":")
                for i in range(6):
                    while (loop2 == 0):
                        ans = input(str(i + 1)+"? ")
                        ans = ans.lower()
                        correct = 0
                        print("   ", end = '')
                        if (len(ans) != 5):
                            print()
                            print("Invalid guess. Please enter exactly 5 characters.")
                            print()
                            loop2 = 0
                            
                        elif (any(c in special_char for c in ans)):
                            print()
                            print("Invalid guess. Please only enter letters.")
                            print()
                            loop2 = 0
                            
                        else:
                            loop = 1
                            i = i + 1
                            for w in range(len(ans)):
                                if(ans[w] == game_words[round][w]):
                                    if (w < 4):
                                        print("!", end = '')
                                        correct = correct + 1
                                        for key in alphabet.keys():
                                            if(key == ans[w]):
                                                alphabet[ans[w]] = '!'
                                    

                                    elif (w == 4):
                                        print("!", end = '')
                                        correct = correct + 1
                                        for key in alphabet.keys():
                                            if(key == ans[w]):
                                                alphabet[ans[w]] = '!'

                                elif (ans[w] in game_words[round]):
                                    if (w < 4):
                                        print("?", end = '')
                                        for key in alphabet.keys():
                                            if(key == ans[w]):
                                                alphabet[ans[w]] = '?'
                                    elif (w == 4):
                                        print("?", end = '')
                                        for key in alphabet.keys():
                                            if(key == ans[w]):
                                                alphabet[ans[w]] = '?'
                                else:
                                    if (w < 4):
                                        print("X", end = '')
                                        for key in alphabet.keys():
                                            if(key == ans[w]):
                                                alphabet[ans[w]] = 'X'
                                    elif(w == 4):
                                        print("X", end = '')
                                        for key in alphabet.keys():
                                            if(key == ans[w]):
                                                alphabet[ans[w]] = 'X'


                            print("     ", end = '')
                            for val in alphabet.values():
                                print(val, end='')

                            print()

                            print("   " + ans.lower() + "     ", end='')

                            for key in alphabet.keys():
                                print(key, end = '')
                            print()

                            turns = turns + 1

                            if (turns == 1 and correct == 5):
                                print("Genius! You earned 32 points this round.")
                            elif (turns == 2 and correct == 5):
                                print("Magnificent! You earned 16 points this round.")
                            elif (turns == 3 and correct == 5):
                                print("Impressive! You earned 8 points this round.")
                            elif (turns == 4 and correct == 5):
                                print("Splendid! You earned 4 points this round.")
                            elif (turns == 5 and correct == 5):
                                print("Great! You earned 2 points this round.")
                            elif (turns == 6 and correct == 5):
                                print("Phew! You earned 1 points this round.")
                            
                            if (correct == 5):
                                print()
                                break

                            if (turns == 6):
                                print("You ran out of tries.")
                                print("The word was " + game_words[round]+ ".")
                                break

                             
                                
                        if (correct == 5):
                            break

                    score = score + 2**(6 - turns)

                    if (correct == 5):
                        break

                i = 0
                turns = 0
                alphabet = emp(alphabet)

            hallOfFame = open("hall_of_fame.txt", "r+")
            with open("hall_of_fame.txt") as file:
                for line in file:
                    scorelist.append(line.split(',')[0])
                    line.strip()
                    line = line.strip()
                    namelist.append(line.split(', ')[1])

            
            namelist.append(name)
            scorelist.append(score)

            resultname_list = [i for _,i in sorted(zip(scorelist,namelist))]

            sorted_scorelist = sorted(scorelist)

            topTenName = list(resultname_list)[:10]
            topTenScore = list(sorted_scorelist)[:10]
            
            
            
            if(len(sorted_scorelist) < 10 or score >= sorted_scorelist[9]):
                print("Way to go " + name +"!")
                print("You earned a total of " + str(score) + " points and made it into the Hall of Fame!")



            
            for i in range(len(topTenName)):
                hallOfFame.write(str(topTenScore)+ ", " + str(topTenName))

            hallOfFame.close()

            loop = 0
            score = 0
            turns = 0
            correct = 0

            hall_of()

        elif (a == '2'):

            hall_of()

            

        elif (a == '3'):
            loop = 1
            my_file.close()
            print("Goodbye.")
        else:
            print("\nInvalid choice. Please try again.")






"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
