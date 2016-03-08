'''
Computers continue to play an ever-increasing role in education. Write a program that will help elementary school students learn addition, subtraction, multiplication, division, and exponentiation. Use a random number generator,
randint(a, b) to generate two integers between a and b, in order to ask questions such as “How much is 6 * 7?”, “How much is 10 + 20?”, “How much is 19 - 16?”, “How much is 8 / 4?”, and “How much is 4 ^ 5?”. (The ^ (carrat) symbol is often used to indicate exponentiation.)
'''
from random import randint
import random

i = 0
j = 0
option = ('a', 's', 'm', 'd', 'e')


def inputs():
    x = input()
    x = int(x)
    return x

def exp_limit(x, y):
    global base, exponent
    if x ** y > 4100:
        exponent = randint(0, 10)
        base = randint(0, 10)
        exp_limit(base, exponent)
    else:
        return base, exponent
        
def addition_check(x):
    global i
    if i < 2:
        if x == (random_number1 + random_number2):
            print("Correct\n")
        else:
            i += 1
            print("Incorrect, please try again:")
            x = inputs()
            addition_check(x)
    else:
        print ("Sorry, you missed this one. The correct answer is %d\n" % (random_number1 + random_number2))
   
def subtraction_check(x):
    global i
    if i < 2:
        if x == minuend - subtrahend:
            print("Correct\n")
        else:
            i +=1
            print("Incorrect, please try again:")
            x = inputs()
            subtraction_check(x)
    else:
        print("Sorry, you missed this one. The correct answer is %d\n" % (minuend - subtrahend))

def multiplication_check(x):
    global i
    if i < 2:
        if x == random_number1 * random_number2:
            print("Correct\n")
        else:
            i +=1
            print("Incorrect, please try again:")
            x = inputs()
            multiplication_check(x)
    else:
        print("Sorry, you missed this one. The correct answer is %d\n" % (random_number1 * random_number2))

def division_check(x):
    global i
    if i < 2:
        if x == quotient:
            print("Correct\n")
        else:
            i +=1
            print("Incorrect, please try again:")
            x = inputs()
            division_check(x)
    else:
        print("Sorry, you missed this one. The correct answer is %d\n" % quotient)
        

def exponetiation_check(x):
    global i
    if i < 2:
        if x == base ** exponent:
            print("Correct\n")
        else:
            i +=1
            print("Incorrect, please try again:")
            x = inputs()
            exponetiation_check(x)
    else:
        print("Sorry, you missed this one. The correct answer is %d\n" % (base ** exponent))
'''
def randomize_main(arg):        
    if arg == 'a':
        print("you have chosen addition\n")
        for j in range(4):
            random_number1 = randint(0, 15)
            random_number2 = randint(0, 15)
            print("how much is %d + %d?" % (random_number1, random_number2))
            add = inputs()
            addition_check(add)

    elif arg == 's':
        print("you have chosen substraction\n")
        for j in range(4):
            minuend = randint(0, 15)
            subtrahend = randint(0, minuend)
            print("how much is %d - %d?" % (minuend, subtrahend))
            sub = inputs()
            subtraction_check(sub)

    elif arg == 'm':
        print("you have chosen multiplication\n")
        for j in range(4):
            random_number1 = randint(0, 15)
            random_number2 = randint(0, 15)
            print("how much is %d * %d?" % (random_number1, random_number2))
            mul = inputs()
            multiplication_check(mul)

    elif arg == 'd':
        print("you have chosen division\n")
        for j in range(4):
            divisor = randint(1, 12)
            quotient = randint(0, 12)
            dividend = divisor * quotient
            print("how much is %d / %d?" % (dividend, divisor))
            div = inputs()
            division_check(div)

    elif arg == 'e':
        print("you have chosen exponetiation\n")
        for j in range(4):
            exponent = randint(0, 10)
            base = randint(0, 10)
            exp_limit(base, exponent)
            print("how much is %d ^ %d?" % (base, exponent))
            exp = inputs()
            exponetiation_check(exp)           
    
'''



while(1):
    print("----------------------------------------------------------\nWelcome to the CISC106 Basic Math Instructor. This program\nallows you to practice your math skills in addition,\nsubtraction, multiplication, division, and exponentiation.\n----------------------------------------------------------")
    print("Type one of the following single letter operations\n{a, s, m, d, e, q}")
    print("     a for addition,\n     s for subtraction,\n     m for multiplication,\n     d for division,\n     e for exponetiation,\n     r for randomize\n     q to quit\n")
    print("Enter your choice:")

    arg =input()        
    if arg == 'a':
        print("you have chosen addition\n")
        random_number1 = randint(0, 15)
        random_number2 = randint(0, 15)
        print("how much is %d + %d?" % (random_number1, random_number2))
        add = inputs()
        addition_check(add)

    elif arg == 's':
        print("you have chosen substraction\n")
        minuend = randint(0, 15)
        subtrahend = randint(0, minuend)
        print("how much is %d - %d?" % (minuend, subtrahend))
        sub = inputs()
        subtraction_check(sub)

    elif arg == 'm':
        print("you have chosen multiplication\n")
        random_number1 = randint(0, 15)
        random_number2 = randint(0, 15)
        print("how much is %d * %d?" % (random_number1, random_number2))
        mul = inputs()
        multiplication_check(mul)

    elif arg == 'd':
        print("you have chosen division\n")
        divisor = randint(1, 12)
        quotient = randint(0, 12)
        dividend = divisor * quotient
        print("how much is %d / %d?" % (dividend, divisor))
        div = inputs()
        division_check(div)

    elif arg == 'e':
        print("you have chosen exponetiation\n")
        exponent = randint(0, 10)
        base = randint(0, 10)
        exp_limit(base, exponent)
        print("how much is %d ^ %d?" % (base, exponent))
        exp = inputs()
        exponetiation_check(exp)

    elif arg == 'r':
        arg = random.choice(option)
        if arg == 'a':
            print("you have chosen addition\n")
            for j in range(4):
                random_number1 = randint(0, 15)
                random_number2 = randint(0, 15)
                print("how much is %d + %d?" % (random_number1, random_number2))
                add = inputs()
                addition_check(add)

        elif arg == 's':
            print("you have chosen substraction\n")
            for j in range(4):
                minuend = randint(0, 15)
                subtrahend = randint(0, minuend)
                print("how much is %d - %d?" % (minuend, subtrahend))
                sub = inputs()
                subtraction_check(sub)

        elif arg == 'm':
            print("you have chosen multiplication\n")
            for j in range (4):
                random_number1 = randint(0, 15)
                random_number2 = randint(0, 15)
                print("how much is %d * %d?" % (random_number1, random_number2))
                mul = inputs()
                multiplication_check(mul)

        elif arg == 'd':
            print("you have chosen division\n")
            for j in range(4):
                divisor = randint(1, 12)
                quotient = randint(0, 12)
                dividend = divisor * quotient
                print("how much is %d / %d?" % (dividend, divisor))
                div = inputs()
                division_check(div)

        elif arg == 'e':
            print("you have chosen exponetiation\n")
            for j in range(4):
                exponent = randint(0, 10)
                base = randint(0, 10)
                exp_limit(base, exponent)
                print("how much is %d ^ %d?" % (base, exponent))
                exp = inputs()
                exponetiation_check(exp)

    elif arg == 'q':
        print("Thank you for using the CISC106 Basic Math Instructor program\nGoodbye.")
        break

    else:
        print("You have input an error letter, please try again:\n")
        
        
#print(X)
'''    
while(1):
    print("----------------------------------------------------------\nWelcome to the CISC106 Basic Math Instructor. This program\nallows you to practice your math skills in addition,\nsubtraction, multiplication, division, and exponentiation.\n----------------------------------------------------------")
    print("Type one of the following single letter operations\n{a, s, m, d, e, q}")
    print("     a for addition,\n     s for subtraction,\n     m for multiplication,\n     d for division,\n     e for exponetiation,\n     r for randomize\n     q to quit\n")
    print("Enter your choice:")

    arg =input()
    if arg == 'r':
        arg = random.choice(option)
        randomize_main(arg)
    elif arg == 'q':
        print("Thank you for using the CISC106 Basic Math Instructor program\nGoodbye.")
        break
    elif arg == 'a' or 's' or 'm' or 'd' or 'e':
        main(arg)
    else:
        print("You have input an error letter, please try again:")
        arg = input()
        main(arg)
'''
