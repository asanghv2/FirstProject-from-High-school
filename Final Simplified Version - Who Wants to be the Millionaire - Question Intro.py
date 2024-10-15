# ==============================================================================

# Author: Aadi Sanghvi, Aryan Sodadasu
# Title: Who Wants to be a Millionaire
# Description: program asks the user rounds of questions, going from easy to \\
# hard.Each round grants a prize if the answer of the question is correct. Every
# round, the prize increases till the user reaches the $1 million round.

# ==============================================================================

# Imports Random Module
import random

# Imports Time Module
import time


# Prints out the round and its prize
def moneyscale():
    print("\n10  $1 MILLION\n9   $500,000\n8   $250,000\n7   $125,000\n6\
   $64,000\n5   $32,000\n4   $16,000\n3   $8,000\n2   $4,000\n1   $2,000")


# Introduces user to the game, with the rules
def introduction():
    # Welcomes the user.
    print("\nWelcome to who wants to be the Millionaire! ")
    #Display for 1 second
    time.sleep(1)
    # Recall moneyscale()
    moneyscale()
    #Display for 1 second
    time.sleep(1)


# Generates a different question each round.
def questionGen():
    questionRoundGeneration = random.randint(0, 2)
    return questionRoundGeneration


# Gets the Question and Ans.
def usersQuesAndAns(roundNum, questionsList, quesInRoundNum):
    questionToAsk = questionsList[roundNum][quesInRoundNum][0]
    questionToAskAns = questionsList[roundNum][quesInRoundNum][1]
    return questionToAsk, questionToAskAns


# Introduces the round and prize.
def questionRoundIntro(NumOnRound, moneyList, roundPlaceList):
    print(roundPlaceList[NumOnRound], "round will grant you $" \
    + moneyList[NumOnRound], 'if correct!')
    time.sleep(1)


# Program will ask user for answer and will check if it is valid or not.
def validateUserAns():
    userAns = input("\nEnter answers:'A','B','C','D',\
 'Options' or 'Quit' to quit: ").lower()
    possibleOutcomes = ['a', 'b', 'c', 'd', 'quit', "options"]
    if userAns in possibleOutcomes:
        return userAns
    else:
        while True:
            if userAns not in possibleOutcomes:
                print(\
                "\nYou MUST enter 'A', 'B', 'C', 'D', 'Options' or 'Quit'.")
                userAns = input(
                    "\nEnter: 'A','B','C','D', 'Options' or 'Quit': ").lower()
                if userAns.lower() in possibleOutcomes:
                    return userAns.lower()


# Converts price in price list to integers.
def price_money(price):
    commas = price.count(",")
    for comma in range(commas):
        price = price.replace(',', '')
    price = int(price)
    return price


# Tells user the correct answer and the prize money they get to take home.
def wrongOrQuit(Ans, moneyUserEarned):
    print("\nThe answer is:", Ans.upper() + '.')
    print("You won $" + str(moneyUserEarned))


# Prints special message if user becomes millionaire.
def millionaire():
    print("\nCongrats you have just earned $1,000,000. You are a MILLIONAIRE!")
    #Display for 1 second
    time.sleep(1)

    


# Checks if users answer is valid when they are asked if they wanna play again.
def userPlayAgainValidation():
    userPlayAgainOptions = ['yes', 'no']
    # userPlayAgain = input("\nWant to play again? ('Yes'/'No'): ").lower()
    while True:
        userPlayAgain = input("\nWant to play again? ('Yes'/'No'): ").lower()
        if userPlayAgain in userPlayAgainOptions:
            if userPlayAgain == 'yes':
                return True
            else:
                return False
        else:
            print("You must enter 'Yes' or 'No'.")


# If user wants to play again
def thankYouPlayAgain():
    print("\nTHANK YOU FOR PLAYING WHO WANTS TO BE A MILLIONAIRE!")
    hintOptions = ['50/50', 'skip']
    run = userPlayAgainValidation()
    return run, hintOptions


# Checks if the user entered valid hint option and returns
def validHintOptions():
    while True:
        if len(hintfulOptions) >= 1:
            user_option = input("\nSelect the following options: " \
            + str(hintfulOptions) + " or 'Exit' to exit options menu: ").lower()

            if user_option in hintfulOptions:
                # Removes the option user entered
                hintfulOptions.remove(user_option)
                break
            # Exits
            elif user_option == 'exit':
                break
            else:
                print("\nOption not available.")
    return user_option


# For the 50/50 option if user selects it
def fiftyFifty(ans):
    possibleAns = ['a', 'b', 'c', 'd']
    possibleFiftyCorrectOptions = [ans]
    for elements in possibleAns:
        if elements == ans:
            possibleAns.remove(ans)
    otherOption = random.choice(possibleAns)
    possibleFiftyCorrectOptions.append(otherOption)
    # Sorts the letters.
    possibleFiftyCorrectOptions.sort()
    return possibleFiftyCorrectOptions


# Asks user to enter valid options in 50/50.
def userValid50Ans(listOfCorrect):
    print("\nYour options are now:", listOfCorrect[0].upper(), "and", \
    listOfCorrect[1].upper() + '.')
    while True:
        newUserOption = input("\nPlease "
                              "enter new possible answers or 'Quit': ").lower()
        if newUserOption != 'quit':
            if newUserOption in listOfCorrect:
                return newUserOption
        else:
            if newUserOption == 'quit':
                return 'quit'
            else:
                print("\nYou must enter new possible answers or 'Quit'")


# Function if Correct
def user_correct(round_num, program_run, hintful_options, \
                 user_prize_money, prices, new_round, userLost):
    print("\n ... The answer is ...")
    #Display for 2 seconds
    time.sleep(2)
    print("CORRECT!")
    #Display for 1 second
    time.sleep(1)
    # If user passed the last round.
    if round_num == 9:
        millionaire()
        # Outputs Thank you message after user has made money and\
        # Asks user if they wanna play again?
        # User lost becomes True
        round_num = 0
        userLost = True
        program_run, hintful_options = thankYouPlayAgain()
        user_prize_money = 0
        # If not in the last round
    else:
        # Calculates the amount of money user can take home.
        roundPrize = price_money(prices[round_num])
        user_prize_money = roundPrize
        # Will move on to the next round.
        round_num += 1
        new_round = True
        program_run = True
        userLost = False
    return round_num, program_run, hintful_options, user_prize_money, userLost


# Function if incorrect.
def user_incorrect(the_ans, user_prize_money, userLost, round_num, program_run,
    hintful_options):
    print("\n ... The answer is ...")
    #Display for 2 seconds
    time.sleep(2)
    print("INCORRECT!")
    #Display for 1 second
    time.sleep(1)
    # Outputs the answer and the prize money user can take home.
    wrongOrQuit(the_ans, user_prize_money)
    userLost = True
    round_num = 0
    program_run, hintful_options = thankYouPlayAgain()
    user_prize_money = 0
    return user_prize_money, userLost, round_num, program_run, hintful_options


# Function if user quits.
def user_quit(userLost, program_run, the_ans, user_prize_money):
    userLost = True
    # Outputs the answer and the prize money user can take home.
    wrongOrQuit(the_ans, user_prize_money)
    program_run = False
    # Prints thank you message.
    print("\nTHANK YOU FOR PLAYING WHO WANTS TO BE A MILLIONAIRE!")
    return userLost, program_run

#Checks prize if user enters incorrect or quits
def userPrizeReset(round_num, prices_lst):
    if round_num != 0:
        user_prize_money = price_money(prices_lst[round_num - 1])
    else:
        user_prize_money = 0
    return user_prize_money


############################################### MAIN PROGRAM ###################
# Displays the Rules

questionNum = ['\nFirst', '\nSecond', '\nThird', '\nFourth', '\nFifth', \
               '\nSixth', '\nSeventh', '\nEighth', '\nNinth', '\nLast']

prices = ['2,000', '4,000', '8,000', '16,000', '32,000', '64,000', '125,000', \
          '250,000', '500,000', '1,000,000']

# Creates hintful options
hintfulOptions = ['50/50', 'skip']

# Questions, choices and their answers.
questionsAndChoices = [
    # Round 1
    [
        # Qs 1
        ["\nWhat is the only food that cannot go bad? \nA. Dark chocolate\
 \nB. Peanut butter \nC. Canned tuna \nD. Honey", "d"],
        # Qs 2
        ["\nWhat is the most visited tourist attraction in the world? \
        \nA.Eiffel Tower\
\nB.Statue of Liberty \nC.Great Wall of China \nD.Colosseum", "a"],
        # Qs 3
        ["\nWhat’s the heaviest organ in the human body? \nA. Brain\
 \nB. Liver \nC. Skin \nD. Heart", "b"]
    ],

    # Round 2
    [
        # Qs 1
        ["\nWho made the third most 3-pointers in the Playoffs in NBA history?\
\nA. Kevin Durant \nB. JJ Reddick \nC. Lebron James \nD. Kyle Korver", "c"],
        # Qs 2
        ["\nWhich of these EU countries does not use the euro as its currency?\
 \nA.Poland \nB.Denmark \nC.Sweden \nD.All of the above", "d"],
        # Qs 3
        ["\nWhich fast food restaurant has the largest number of retail\
 locations in the world?\
\nA.Jack In The Box \nB.Chipotle \nC.Subway \nD.McDonald’s", "c"]
    ],
    # Round 3
    [
        # Qs 1
        ["\nWhich location was recorded as hottest temperature ever on Earth?\
\nA.Mitribah, Kuwait \nB.Death Valley, California \nC.Yuma,\
Arizona \nD.Key West, Florida", "b"],

        # Qs 2
        ["\nWhat is the oldest soft drink in the United States?\
\nA.Coca Cola \nB.Pepsi \
\nC.Dr. Pepper \nD.Canada Dry Ginger Ale", "c"],

        # Qs 3
        ["\nIn what country do more than half of people believe in elves?\
\nA.Norway \nB.Russia \nC.Holland \nD.Iceland", "d"]
    ],

    # Round 4
    [
        # Qs 1
        ["\nWhich European country has the longest coastline?\
 \nA.Italy \nB.Greece \nC.Norway \nD.Croatia", "b"],
        # Qs 2
        ["\nWhich Country produces the most coffee in the world?\
 \nA.Vietnam \nB.Indonesia  \nC.Brazil \nD.Columbia", "c"],
        # Qs 3
        ["\nHow many countries are present in Africa?\
\nA.57 \nB.54 \nC.43 \nD.39", "b"]
    ],

    # Round 5
    [
        # Qs 1
        ["\nWhich gas features predominately in the earth’s atmosphere,\
 making up roughly 78% of dry air?\
\nA.Nitrogen \nB.Methane  \nC.Argon \nD.Hydrogen", "a"],
        # Qs 2
        ["\nWhat is the biggest state by land mass in America?\
\nA.California \nB.Alaska \nC.Texas \nD.Florida", "b"],
        # Qs 3
        ["\nWhat was the name of the Greek god of war?\
\nA.Apollo \nB.Zeus \nC.Hermes \nD.Ares", "d"]
    ],
    # Round 6
    [
        # Qs 1
        ["\nIn which part of your body would you find the cruciate ligament?\
\nA.Elbow \nB.Foot \nC.Knee \nD.Hand", "c"],
        # Qs 2
        ["\nHow many Henry VIII’s wives were named after Catherine?\
\nA.One \nB.Two \nC.Three  \nD.Four", "c"],
        # Qs 3
        ["\nWhat is the common name for absorbic acid?\
\nA.Vitamin B12 \nB.Vitamin C \nC.Vitamin K \nD.Vitamin D", "b"]
    ],
    # Round 7
    [
        # Qs 1
        ["\nWhich European country technically shares a border with Brazil,\
 because one of its “overseas departments” does? \
\nA.Germany \nB.Belgium \nC.France \nD.Great Britain", "c"],
        # Qs 2
        ["\nWhat actor said, “If you had been a public figure since\
 the time you were a toddler… maybe you too would value\
  privacy above all else”?\
\nA.Leonardo DiCaprio \nB.Jodie Foster\
\nC.Shirley Temple \nD.Daniel Radcliffe", "b"],
        # Qs 3
        ["\nWhich princess was traditionally called\
 Badr al-Budur before Disney renamed her?\
\nA.Belle \nB.Anna \nC.Jasmine \nD.Ariel", "c"]

    ],
    # Round 8
    [
        # Qs 1
        ["\nIn Swedish, a skvader is a rabbit with what unusual feature?\
\nA.Wings \nB.Glasses \nC.Leotard \nD.Giant Hands", "a"],
        # Qs 2
        ["\nThe three actors who starred as Magneto,\
 Iron Man and Doctor Strange have all played what other character?\
 \nA.James Bond \nB.Basil Fawlty \nC.Ebenezer Scrooge \nD.Sherlock Holmes",
         "d"],
        # Qs 3
        ["\nWhich country’s flag features an eagle eating a snake?\
 \nA.Dominica \nB.Mozambique \nC.Guam \nD.Mexico", "d"]
    ],

    # Round 9
    [
        # Qs 1
        ["\nAlthough it freed itself from the United States in 1946,\
 what nation’s Independence Day celebrates its declaration of\
 independence from Spain in 1898?\
 \nA.Mexico \nB.The Philippines \nC.Argentina \nD.Guatemala", "b"],
        # Qs 2
        ["\nWhat country’s land is mostly on an island,\
 although most of its people live on a\
 peninsula across the South China Sea?\
\nA.Malaysia \nB.Indonesia \nC.Thailand \nD.Papua New Guinea", "a"],
        # Qs 3
        ["\nThe world’s oldest known musical instruments \
 are 42,000-year-old flutes made from bird bone and the ivory of what mammal?\
\nA.Megalodon \nB.Mammoth \nC.Sabar toothed tiger \nD.Dire wolf", "b"]
    ],
    # Round 10
    [
        # Qs 1
        ["\nMauritius is the only African country where the most\
         commonly practised\
 religion is what? \nA.Mormonism \nB.Hinduism \
 \nC.Protestantism \nD.Atheism", "b"],

        # Qs 2
        ["\nKersti Kaljulaid was 46 years old when she became the\
 youngest president ever elected to lead which country?\
 \nA.Belarus \nB.Lithuania \nC.Latvia \nD.Estonia", "d"],
        # Qs 3
        ["\nWhat flightless bird, now extinct,\
 was last seen on an island off the coast of Iceland? \nA.Saint Helena Hoopoe\
 \nB.Amsterdam wigeon \nC.The great auk (Pinguinus impennis)\
 \nD.Jamaican caracara", "c"]
    ]
]

# Welcomes the user.
introduction()

# Runs the program again until user quits
programRun = True
newRound = True  #

while programRun == True:
    user_lost = False

    roundNum = 0
    userPrizeMoney = 0

    # Runs the game until user makes it to the last round or lost
    while roundNum < 10 and user_lost == False:
        questionRoundIntro(roundNum, prices, questionNum)

        # If new question:
        if newRound == True:  #
            randomRoundQuestion = questionGen()

        theQuestion, theAns = usersQuesAndAns(roundNum, questionsAndChoices, \
                                              randomRoundQuestion)
        print(theQuestion)

        # Gets user's ans
        ansUserEntered = validateUserAns()

        # If the user entered the correct answer.
        if ansUserEntered == theAns:
            roundNum, programRun, hintfulOptions, userPrizeMoney, user_lost = \
                user_correct(roundNum, programRun, \
                             hintfulOptions, userPrizeMoney, prices, newRound,
                             user_lost)

        # If user entered options
        elif ansUserEntered == 'options':
            if len(hintfulOptions) != 0:
                # Gets the Hint option from the user
                userOption = validHintOptions()

                # If 50/50:
                if userOption == '50/50':
                    newChoices = userValid50Ans(fiftyFifty(theAns))

                    # If the user entered correct ans:
                    if newChoices == theAns:
                        roundNum, programRun, hintfulOptions,\
                        userPrizeMoney, user_lost = \
                            user_correct(roundNum, programRun, \
                                         hintfulOptions, userPrizeMoney, prices,
                                         newRound, user_lost)

                    # If user entered incorrect ans:
                    elif newChoices != theAns and newChoices != 'quit':
                        userPrizeMoney = userPrizeReset(roundNum, prices)
                        userPrizeMoney, user_lost, roundNum, programRun, \
                        hintfulOptions = user_incorrect(theAns,\
                userPrizeMoney, user_lost, roundNum,programRun,hintfulOptions)

                    # If user entered 'quit':
                    else:
                        if newChoices == 'quit':
                            userPrizeMoney = userPrizeReset(roundNum, prices)
                            user_lost, programRun = user_quit(user_lost,\
                                        programRun,theAns,userPrizeMoney)

                # if user exited the options menu:
                elif userOption == "exit":
                    # Will Return back to the game
                    newRound = False


                # If user entered skip.
                else:
                    if userOption == 'skip':
                        if roundNum != 9:
                            roundNum += 1
                            newRound = True  #
                            print("\nYou have moved on to the next round.")
                            # Shows the prize money!
                            roundPrize = price_money(prices[roundNum])
                            userPrizeMoney = roundPrize
                        else:
                            millionaire()
                            # Outputs Thank you message after\
                            # user has made money and\
                            # Ends the game
                            user_lost = True
                            # Asks user if they wanna play again?
                            programRun, hintfulOptions = thankYouPlayAgain()
                            roundNum = 0
                            userPrizeMoney = 0
            else:
                if len(hintfulOptions) == 0:
                    newRound = False
                    print("\nYou have no hintful options available.")


        # If user wants to quit.
        elif ansUserEntered == 'quit':
            userPrizeMoney = userPrizeReset(roundNum, prices)
            user_lost, programRun = user_quit(user_lost,\
                                              programRun,theAns,userPrizeMoney)

        # If user enters incorrect answer.
        else:
            userPrizeMoney = userPrizeReset(roundNum, prices)
            userPrizeMoney, user_lost, roundNum, programRun, \
            hintfulOptions = user_incorrect(theAns, \
                                            userPrizeMoney, user_lost, roundNum,
                                            programRun, hintfulOptions)

