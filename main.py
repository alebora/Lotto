#Lotto 6/49 Simulation

#Five add ons:
#1.Timer count down
#2.Asks and uses name and capitalizes
#3.Ascending order
#4.Italicizes text
#5.Loops the program and gives different option programs

import random
import time 
import colorama
import sys
import replit
from tabulate import tabulate
from colorama import Fore, Back

colorama.init(autoreset=True)

#This function is preformed which tells us if any of the numbers inputed match the random lottery numbers generated by the rand() function.
def matching(numbers, rand_nums):
  #Sets a blank list to the variable counter 
  counter = []
  #This subtracts 1 element from the number that returns the len() function. So we do not have 7 elements instead of 6 since the for loop starts counting from 0. 
  for i in range(len(numbers)-1):
    #This checks every element from the numbers inputed by person in the numbers list and contrasts them with the numbers generated in the rand_nums list and adds every match to the counter list.
    if numbers[i] in rand_nums:
      counter = counter + [numbers[i]]
  #returns the counter list of matched values to line 108
  return counter 

#This is the function that randomizes the lottery numbers **This code was taken from https://www.101computing.net/lottery-numbers/ and manipulated to fit the program**
def rand():
  #Initialise an empty list that will be used to store the 6 lucky numbers 
  lotteryNumbers = []
  for i in range (0,6):
    number = random.randint(1,50)
    #Check if this number has already been picked and...
    while number in lotteryNumbers:
      #...if it has, pick a new number instead 
      number = random.randint(1,50)
    #Now that we have a unique number, let's append it to our list.
    lotteryNumbers.append(number)

  #This sorts the list in ascending order
  lotteryNumbers.sort()

  #Added time delay of 3 seconds and counts down from 3 before displaying the generated lottery numbers.
  for i in range(3):
    #end = '\r' is a built in function that returns the program to the beginning of the line. This repeats three times with the delay of 1 second.
    print("Drumroll please..." + str(3-i) , end = '\r')
    time.sleep(1)

  #Display the list on screen:
  print(' ')
  print('\x1b[3;30;43m' + "Today's lottery numbers are: " + '\x1b[0m') 
  print(lotteryNumbers)
  #This returns the lotterynumber value to line 106
  return lotteryNumbers

#This function is preformed if the peroson indicated 'Y' that yes they would like to play
def play():
  #sets the numbers as an empty list 
  numbers = []
  #ran counts the amount of inputs which is currently set to zero
  ran = 0
  #This loop will repeat untill there are 6 rans counted which is when it wil proceed to line 92
  while ran < 6:
    #This numbers the messages printed from 1 to 6 to keep the amount of inputs organized for the person
    temp = input(str(ran+1) + ". Please input a number from 1-49:")
    # Prints a message to try again if no value is entered
    if temp is None or temp == '':
      print('\x1b[3;35;33m' + "Im sorry I couldnt get that. Please enter a number between 1 and 49." + '\x1b[0m' )
    #Prints a message to try again if anything but a number is entered
    elif temp.isdigit() == False:
      print('\x1b[3;35;33m' + "Im sorry I couldnt get that. Please enter a number between 1 and 49." + '\x1b[0m' )
    else: 
      #States that the numbers inputed are integers
      temp = int(temp)
      #Prints a message to try again if a number is entered more than once
      if temp in numbers:
        print('\x1b[3;35;33m' + "Sorry you already selected this number. Please input another one." + '\x1b[0m' )
      #If the numbers are in range and are not repeated then it adds 1 to the input counter (ran)
      elif temp in range(1, 49): 
        numbers = numbers + [temp]
        ran = ran + 1
      #Prints a message to try again if a number is lower than 1 or higher than 49
      else: 
        print('\x1b[3;35;33m' + "The number you inputed is out of range, try again and please make sure the number is not less than 1, and not greater than 49." + '\x1b[0m')
  print('')
  #After the person inputs 6 different numbers then a messsage is printed asking the person if they would like to see the numbers they inputed in ascending order
  ask = input("Would you like to see your numbers sorted in ascending order?[State Y if yes, press any other key for no]:")
  #If the person said 'Y' then the numbers are presented in ascending order
  if ask == "Y" or ask == "y":
    numbers.sort()
    print(numbers)
   #If the person said 'N' then the numbers are presented as they were inputed
  else:
    print(numbers)
  #After the numbers are printed this goes to the next function which is rand() in line 35
  rand_nums = rand()
  
  #after the lottery numbers are returned to line 106 then we are saying that the result is equal to our new function matching() with the arguments of number variables and rand_num variable which is the lottery numbers. Then the matching() function is preformed in line 23.
  result = matching(numbers, rand_nums)
  #If none of the numbers match then a messgae is displayed saying no numbers match 
  if len(result) == 0:
    print('\x1b[3;35;33m' + "You got zero numbers right. Dont give up, better luck next time!" + '\x1b[0m')
  #If some of the numbers match then a messgae is displayed saying how many numbers match and what those numbers are. Then the program returns to line 124
  else:
    print('\x1b[3;35;33m' + "You got " + str(len(result)) + " number(s) right, they are " + str(result) + '\x1b[0m')
  

#First function in place, this is responsible for the question of would the person like to play or not
def start_func(name): 
  print('')
  print('')
  #Adds name from line 137 and then asks would they like to play or not 
  start = input('\x1b[3;30;43m' + name.title() + ", Would you like to play lotto 6/49?[Y/N]:" + '\x1b[0m')
  #If the person said 'Y' then the lotto proceeds to open the next function which is the play() function in line 64
  if start == "Y" or start == "y":
    play()
    #After function play() completes the program goes to line 144 
    return False 
  #If the person said 'N' then the program prints a message and stops
  elif start == "N" or start == "n":
    print("Thats okay, have a good rest of your day!")
    return True
  #If the person inputed an invalid statement (not 'Y' or 'N') then a message is diplayed to try again and the start_func returns false and loops again
  else:
    print('\x1b[3;35;33m' + "Im sorry, I didnt get that. Please try again." + '\x1b[0m')
    return False

#**********************************************#
#***PROGRAM STARTS HERE. First Name question***#
#**********************************************#
def firstQuest():
  name = input('\x1b[3;35;33m' + "Hello, what is your name?:" + '\x1b[0m')

  #While our result is equal to true (because result equals false and not result would equal true) then the while loop will proceed 
  result = False
  while not result:
    #While loop takes us to the start_func() function in line 116
    result = start_func(name)

#------------------------------------------------------
#Lotto program A
def runStart():
  # run starting time
  start = time.time()

  while True:
    # prints out information for user with time delay for effect. this is why it must be a variable - otherwise we cannot apply the letter by letter delay 
    explanation = 'Welcome to Lotto 6/49! \nYou will be asked to choose 6 numbers, in order to correctly guess the system generated lotto numbers. \nEnsure your input follows the instructions where they are stated.\nGood luck!\n'

   # this loop will allow us to print out each character one by one.
    for char in explanation:
     time.sleep(0.05)
     sys.stdout.write(char)
     sys.stdout.flush()

    # prompts user to enter their name, their name is then the new "name" variable to be used throughout the code
    name = input(Fore.RED + "\nPlease enter your name/nickname: \n") 
    print('')
    time.sleep(1)
    # uses the variable 'name' to welcome them using their input
    print(Fore.BLUE + "Greetings, " + name.capitalize() + "!😎\n")
    time.sleep(2)
    

    # empty list - will store the winning lottery numbers
    lottery = []

    for i in range(0, 6):
        number = random.randint(1, 50)
        # find out if the number is already in lottery / used :
        while number in lottery:
            # if it is, pick a new number:
            number = random.randint(1, 50)
        #append the numbers to the list until we have 6 chosen numbers in a list 
        lottery.append(number)

    # user input, asks if they want the numbers sorted
    while True:
        print("Would you like the WINNING numbers to be in ascending order when they are revealed? (Y/N - Capital Letter Only): ")
        answer = str(input())
        # sorts if user input is "Y"
        if (answer) == 'Y':
            lottery.sort()
            break
        # this is for if user input is "N", so that it does not change the list order, however, it accepts the input
        elif (answer) == 'N':
          break
        # this is for if their input is invalid (not "N" or "Y"), it will print this informative statement for the user and the loop will restart, prompting them to enter their input again until it meets the input requirement.
        else:
          print(Fore.BLACK + Back.RED + "Your input was not accepted. Try again.\n")
          continue
  

    # instruction statement printed to console for user understanding - restates the requirements for the numbers
    print(Fore.BLACK + Back.RED + '\nTo choose your lotto numbers, you will have to enter 6 different numbers between 1 and 49. \nEnsure it is a whole number!')

    # empty list - users selection will be put here
    userinfo = []
    # ran variable counts the amount of inputs it has taken so far, currently set to zero. 
    ran =1
    while ran !=7:
      while True:
        try: 
          # will prompt user to input a number, and will use the ran variable to show the user how many of their numbers have been input already. this will be helpful if they enter an invalid input, as they will know which number they are on.
          number = int(input(f'{ran}.' + " Enter any digit between 1 and 49:"))
          # if the number has already been chosen and appended to the userinfo list, it will print this statement and prompt them to choose a different number
          if number in userinfo: 
             print(Fore.BLACK + Back.RED + "You have already selected this number. Please input a different number.")
          # if the number does not meet the range requirment is either lower than 1 or higher than 49, it will print this statement and prompt them to choose a number that is within the range
          elif number <1 or number > 50:
            print(Fore.BLACK + Back.RED + "Your input is out of range, try again. Make sure the number is between 1 and 50.")
          # if the input is a valid number, it will append it to the userinfo list and repeat. 
          else:
            userinfo.append(number)
            # each time a valid number is input, the ran variable increases by one. when it reaches 6, the loop will automatically stop
            ran +=1
            break 
        # if the number does not meet the input type requirement (it is not a digit/number) it will print this statement and prompt the user to choose a number rather than a different value type
        except ValueError: 
           print(Fore.BLACK + Back.RED + "Please ensure your input is the correct value type - must be an integer.")

  
    # allows user to have the numbers revealed with a time delay
    while True:
      print("\nWould you like the winning numbers to be revealed with a time delay? (Y/N - Capital Letter Only): ")
      answer = input()
      # if they choose "Y", it will reveal each number in the list one by one, on seperate lines.
      if (answer) == 'Y':
          print(Fore.CYAN + 'The winning lottery numbers for today are...')
          time.sleep(2)
          # i represents each number, not each seperate digit (for example 12 will print as "12" not "1" and "2" seperately)
          for i in (lottery):
            print(i, '\n')
            time.sleep(0.5)
          break
      # if they respond "N", it prints the entire list in one go.
      elif (answer) == 'N':
          print(Fore.CYAN + 'The winning lottery numbers for today are...')
          print(lottery)
          print("\n")
          break
      # if their input is invalid (not "N" or "Y"), it will print this statement and the question will prompt them to enter their input again.
      else:
          print(Fore.BLACK + Back.RED + "Your input was not accepted. Try again.")
          print("\n")
          continue

    # print user input numbers to the screen to remind them what they chose
    print(Fore.CYAN + "Your numbers were...")
    print(userinfo)
    print("\n")

    # counts how many of the winning numbers user guessed correct, if any. 
    counter = 0
    for number in userinfo:
        if number in lottery:
            counter += 1
    print('')
    time.sleep(2)
    # prints amount for the user to see
    print(Fore.BLUE + "You guessed " + str(counter) + " winning number(s).")

    # prints an engaging fact for user
    print(Fore.BLUE +
          "To get ONE of the SIX numbers, there is a 6/49 probablity. \nThis is because you have you have 50 numbers to choose from per round.\n")

    # prompts user input for more details on their luck / probabilities 

#-------------------------------------
def calc():
  #Bonus compound interest calculator

  #Python program to compute compound interest 
  
  #
  initial_investment = float(input("Enter the principal amount: "))
  
  times = int(input("Enter the number of time periods: "))
  
  interest = float(input("Enter the rate of interest(decimal): "))
  
  periods = float(input("Enter the number of times interest applied per time period: "))

  #compute compound interest
  A =  initial_investment * (pow((1 + interest / periods), times * periods)) 
  
  #print
  print('')
  print("You gained: {}".format(A - initial_investment))
  print("Your final amount after " + str(times) + " time periods: " + str(A))

  #-------------

cond = False
while not cond: 
  program_decision = input( '\x1b[3;30;43m' + 'Hello, which program would you like to access \n 1. Lotto Program A \n 2. Lotto Program B \n 3. Compound Investment calculator? [1/2/3]:' + '\x1b[0m')
  if program_decision == '1':
    runStart()
    cond = True
  elif program_decision == '2':
    firstQuest()
    cond = True
  elif program_decision == '3':
    calc()
    cond = True
  else:
    print('\x1b[3;35;33m' + "This input is not an option, please input 1, 2, or 3." + '\x1b[0m')




#Calculating the odds-----------------------------------
#6/49 x 5/48 x 4/47 x 3/46 x 2/45 x 1/44 = 1/13983816 
#Your odds of getting one number are 6/49 or 12.2% 
#Your odds of getting two numbers right are 5/392 or 1.3%
#Your odds of getting three numbers right are 5/4606 or 0.1%%
#Your odds of getting four numbers right are 15/211876 or 7.1 x 10^-7%
#Your odds of getting five numbers right are 1/317814 or 3.1 x 10^-6%
#Your odds of getting all the numbers right are 1/13983816 or 7.2 x 10^-8%
