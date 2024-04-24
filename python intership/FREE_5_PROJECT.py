# 1.QR__CODE
"""import qrcode

 def generat_qrcode(text):

     qr = qrcode.QRcode(
         version = 1,
         error_correction = qrcode.constant.ERROT_CORRECT_L,
         box_size = 10,
         border = 4,
     )

     qr.add_date(text)
     qr.make(fit = True)
     img = qr.make_image(fill_color ="black", back_color="white")
     img.save("qrimg.png")
 generat_qrcode("https://www.codewithtomi.com")"""

# 2.LEAP YEAR
"""

def is_leap_year(year):
    if year % 4 ==0:
        if year % 100 == 0:
            if year % 400 == 0:
               print("leap year")
            else:
                print('not leap year')
        else:
            print('leap year')
    else:
        print('Not leap year')

is_leap_year(2025)   # Not leap year"""

# 3. WORD DICTIONARY

"""from PyDictionary import PyDictionary 

dictionary = PyDictionary()

while True:

    word = input("Enter The Word : ")
    if word == "":
       break

    print(dictionary.meaning(word))
"""

# 4. Rock Paper Scissors

"""import random

exit = False
user_point = 0
computer_point = 0

while exit == False:
    options = ['rock','paper','scissors']
    user_input = input("Choose rock ,paper, scissors or exit: ")
    computer_input = random.choice(options)


    if user_input == 'exit':
        print('Game is over')
        exit = True

    if user_input == 'rock':
        if computer_input =='rock':
            print('your input is rock:')
            print('computer input is also rack')
            print('Its tie!!!!')

        elif computer_input == 'paper':
            print('your i/p is rock:')
            print('computer i/p is paper')
            print('computer is win')
            computer_point += 1

        elif computer_input == 'scissors':
            print('your i/p is rock')
            print("computer i/p is scissors")
            print('computer is win !')
            user_point +=1

    elif user_input =='paper':
        if computer_input =='rock':
            print('your input is paper:')
            print('computer input is also rack')
            print('Its tie!!!!')

        elif computer_input == 'paper':
            print('your i/p is paper:')
            print('computer i/p is paper')
            print('computer is win')
            computer_point += 1

        elif computer_input == 'scissors':
            print('your i/p is paper')
            print("computer i/p is scissors")
            print('computer is win !')
            user_point +=1

    elif user_input == 'scissors':
        if computer_input == 'rock':
            print('your input is scissors:')
            print('computer input is also rack')
            print('Its tie!!!!')

        elif computer_input == 'paper':
            print('your i/p is scissors:')
            print('computer i/p is paper')
            print('computer is win')
            computer_point += 1

        elif computer_input == 'scissors':
            print('your i/p is scissors')
            print("computer i/p is scissors")
            print('computer is win !')
            user_point += 1

    elif user_input != 'rock' or user_input != 'paper' or user_input != 'scissors':
        print('Invalid input')"""

# 5.