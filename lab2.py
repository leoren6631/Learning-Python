#Problem 1: The calculate_grade() function you have just written is part of problem 1. Write 3 more assertEqual() tests to test the function calculate_grade(). In other words, pick three sets of lab scores and test scores, and then calculate (with a calculator if you like) what you think calculate_grade() should return for those lab scores and test scores. Run your script. If any of the assertEqual() tests fail, figure out what is wrong with your program or your assertEqual() tests and correct the error(s). This process is called debugging. (Don’t forget to print out the problem number.)
from cisc106_34 import *

def calculate_grade(lab_score, test_score):
    #calculate and return the grade
    grade = (lab_score + test_score) / 200
    return grade

assertEqual(calculate_grade(41.5, 132.5), 0.87)
assertEqual(calculate_grade(49.2, 120.4), 0.848)
assertEqual(round(calculate_grade(45.5, 133.2), 2), 0.89)

#Problem 2: Write a function named calculate_trapezoid_area() that calculates the area of a trapezoid. (You MUST name your function calculate_trapezoid_area(). The function calculate_trapezoid_area() should have three parameters: the trapezoid’s two bases and the trapezoid’s height (in that order). The function should return the area of the trapezoid. The function header and doc string should look like this:
def calculate_trapezoid_area(base_1, base_2, height):
    area = (base_1 + base_2) * height / 2
    return area

assertEqual(calculate_trapezoid_area(1, 3, 2), 4)
assertEqual(calculate_trapezoid_area(32.0, 0.0, 4.0), 64.0)
assertEqual(round(calculate_trapezoid_area(0.14, 15.07, 21.20), 2), 161.23)

#Problem 3: Write a function called calculate_cylinder_volume(). The function has 2 parameters: radius and height (in that order). calculate_cylinder_volume() should calculate the volume of a cylinder.
from math import pi

def calculate_cylinder_volume(radius, height):
    circle_area = pi * (radius ** 2)
    volume = circle_area * height
    return volume

assertEqual(round(calculate_cylinder_volume(2, 2), 2), 25.13)
assertEqual(round(calculate_cylinder_volume(4, 5), 2), 251.33)
assertEqual(round(calculate_cylinder_volume(3.2, 9.9), 2), 318.48)

#Problem 4:
#x = 'bbb', y = 'a'
def make_string_strata(x, y):
    output = x+'|'+y+'|'+x
    return output
#print (make_string_strata(x, y))

assertEqual(make_string_strata('bbb', 'a'), 'bbb|a|bbb')
assertEqual(make_string_strata('1', '23'), '1|23|1')
assertEqual(make_string_strata('Z', ''), 'Z||Z')

#Problem 5:
'''
An Internet service provider charges for megabytes (MB) transferred according to a sliding scale. Transfers up to and including 500 MB are charged a flat rate (hereinafter called the base). Transfers over 500 MB up to and including 2500 MB are charged 1.25 times the base, plus an additional $0.01/MB for each MB over 500 MB. Transfers over 2500 MB up to and including 12500 MB are charged 3.75 times the base, plus an additional $0.025/MB for each MB over 2500 MB. Transfers over 12500 MB are charged 30 times the base.
Program the function bill_amount(), which takes in an amount of data transferred and a base rate (in that order), and computes the total charge (in dollars). The amount of data transferred should be in MB, and the base rate in dollars). Write 4 assertEqual() tests for 145 MB, 920.8 MB, 8607 MB and 15025 MB, using a base rate of $10.00. Write 3 other assertEqual()() tests using a base rate and data transfer amount of your choosing.
'''
def bill_amount(data, base):
    if data <= 500:
        total_charge = base
    elif 500 < data <= 2500:
        total_charge = base * 1.25 + 0.01 * (data - 500)
    elif 2500 < data <= 12500:
        total_charge = base * 3.75 + 0.025 * (data - 2500)
    else:
        total_charge = base * 30
    return total_charge
'''
print(round(bill_amount(145, 10.00),2))
print(round(bill_amount(920.8, 10.00), 2))
print(round(bill_amount(8607, 10.00), 2))
print(round(bill_amount(15025, 10.00), 2))
'''
assertEqual(round(bill_amount(145, 10.00), 2), 10.00)
assertEqual(round(bill_amount(920.8, 10.00), 2), 16.71)
assertEqual(round(bill_amount(8607, 10.00), 2), 190.18)
assertEqual(round(bill_amount(15025, 10.00), 2), 300.00)

#Problem 6:
'''
First write a function called time_calculator() that takes one parameter – an integer number of seconds. time_calculator() should output (i.e. print) the equivalent number of days, hours, minutes, and seconds. For example, if the user inputs 200000, the output should say something such as “200000 seconds equals 2 days, 7 hours, 33 minutes, 20 seconds”. Your function must accomplish its task by manipulating the input numerically, not with string manipulations. Note that time_calculator() does NOT ask for any input. Next write Python code which prompts the user to input a number of seconds, and then calls your time_calculator() function with the specified number of seconds. Note that the time_calculator() function does not return any value, so assertEqual() tests cannot be used to test its functionality. Test the function in your own way.
'''
def time_calculator(time):
    second = minute = hour = day =0
    if time < 60:
        second = time
    elif 60 <= time < 60**2:
        minute = int(time / 60)
        second = (time - minute*60)
    elif 60**2 <= time < 24*60**2:
        hour = int(time / 60**2)
        minute = int ((time - hour*60**2) / 60)
        second = time - hour*60**2 - minute*60
    else:
        day = int(time / (24*60**2))
        hour = int((time - day*24*60**2) / 60**2)
        minute = int((time - day*24*60**2 - hour*60**2) / 60)
        second = time - day*24*60**2 - hour*60**2 - minute*60
    print (time, 'seconds equals', day,'days,',hour, 'hours,', minute, 'minutes,', second, 'seconds.')
time_calculator(200000)

#Problem 7:
'''
Write a function called swap_2_of_3(), which takes an integer value in the range [0, 999], swaps the tens digit and hundreds digit, and returns the result. As tests, swap_2_of_3(326) should return 236, swap_2_of_3(930) should return 390, swap_2_of_3(20) should return 200, and swap_2_of_3(7) should return 7. Include these four tests, and write three additional assertEqual() tests for your function. N.B. The argument to swap_2_of_3() should not begin with a zero (e.g., 041), because Python 3.4 considers that to be a syntax error.
'''
def swap_2_of_3(num):
    if 0<= num < 10:
        pass
    elif 10 <= num < 100:
        num = int(num/10)*100 + num % 10
    elif 100<= num < 1000:
        num = int(num/100)*10 + int((num - int(num/100)*100)/10)*100 + num % 10
    else:
        num = 'Error input'
    return num
assertEqual(swap_2_of_3(326), 236)
assertEqual(swap_2_of_3(930), 390)
assertEqual(swap_2_of_3(20), 200)
assertEqual(swap_2_of_3(7), 7)
print (swap_2_of_3(-2))

#Problem 7 Extra Credit:
'''
Extend your function to work for integers values in the larger range [-999 to 999]. Include at least 2 additional assertEqual() tests for negative values.
'''
def swap_2_of_3_extend(num):
    if -10< num < 10:
        pass
    elif 10 <= abs(num) < 100:
        if num > 0:
            num = int(num/10)*100 + num % 10
        else:
            num = abs(num)
            num = int(num/10)*100 + num % 10
            num = -1*num
    elif 100<= abs(num) < 1000:
        if num > 0:
            num = int(num/100)*10 + int((num - int(num/100)*100)/10)*100 + num % 10
        else:
            num = abs(num)
            num = int(num/100)*10 + int((num - int(num/100)*100)/10)*100 + num % 10
            num = -num
    else:
        num = 'Error input'
    return num
assertEqual(swap_2_of_3_extend(326), 236)
assertEqual(swap_2_of_3_extend(930), 390)
assertEqual(swap_2_of_3_extend(20), 200)
assertEqual(swap_2_of_3_extend(7), 7)
assertEqual(swap_2_of_3_extend(-7), -7)
assertEqual(swap_2_of_3_extend(-20), -200)
assertEqual(swap_2_of_3_extend(-326), -236)

#Problem 8:
'''
You are tasked with writing a function named mortgage_approval(), to decide whether or not to approve a mortgage loan. The function should return ‘yes’, ‘no’ or ‘maybe’. The function is given 6 pieces of information about a mortgage applicant, in the following order: the loan amount s/he is applying for, her/his current salary, her/his current cash in accounts, her/his estimated non-cash assets, her/his numerical credit score, and her/his last name. The following business rules determine whether or not to approve the loan: 
CISC106, Spring 20161. No mortgage will be approved if an applicant has less than 15% of the loan amount as cash in accounts (i.e., if less than 15%, the mortgage decision is “no”).2. No mortgage will be approved if an applicant has a credit score less than 590.3. For applicants with credit scores in the range [590 – 700) (the value 590 is included, but the value 700 isnot included), current cash in accounts must be greater than or equal to 25% of the loan amount.4. All applicants must have a current salary greater than one-third of the balance of the loan amount, whichis considered to be the loan amount minus the cash in accounts.5. Any applicant with the last name Doe must have at least $750,000 in non-cash assets or the loan isdeclined.6. Any applicant that made it past rules 1 – 5 and has more cash in accounts than the loan amount isautomatically approved (i.e., the mortgage decision is “yes”). Otherwise, the applicant must come to the bank for a personal interview (i.e., the mortgage decision is “maybe”.)Write a minimum of 9 assertEqual() tests that test these rules, making sure that each rule is tested at least once. Organize your tests so that they follow the business rules in the order they are given.
'''
def mortgage_approval(loan_amount, salary, cash, non_cash_assets, credit_score, last_name):
    if cash < loan_amount*0.15 or credit_score < 590:
        result = 'No'
    elif 590 <= credit_score < 700 and cash < 0.25*loan_amount:
        result = 'No'
    elif salary <= (loan_amount-cash)/3:
        result = 'No'
    elif last_name == 'Doe' and non_cash_assets < 750000:
        result = 'No'
    else:
        if cash > loan_amount:
            result = 'Yes'
        else:
            result = 'Maybe'
    return result

assertEqual(mortgage_approval(100000, 50000, 100000*0.25-1, 500000, 699, 'Do'), 'No')

    
    
    


    
