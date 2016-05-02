import math
import unittest
import sys


# converts the feet to inches
def convert_feet_to_inches(height_in_feet):
    inches_returned = height_in_feet * 12
    return inches_returned


def complete_height_to_inches(feet, inches):
    full_convert = feet + inches
    return full_convert


def convert_height_to_metric(height):
    metric_height = (height * 0.025)  # convert height to metric
    return metric_height


def convert_weight_to_metric(weight):  # convert weight to metric
    metric_weight = (weight * 0.45)
    return metric_weight


def square_metric_height(height):  # square height
    squared_result = (height * height)
    return squared_result


def get_bmi_number(weight, height_squared):
    final_bmi = (weight / height_squared)
    return final_bmi


# main function to give BMI result
def tell_bmi(height_in_feet, height_in_inches, weight):
    """
    I don't know why this is here. Not used.

    new_height_feet = convert_feet_to_inches(height_in_feet)
    new_height = complete_height_to_inches(new_height_feet, height_in_inches)
    metric_height = convert_height_to_metric(new_height)

    converted_height = square_metric_height(metric_height)
    """

    converted_height = convert_weight_to_metric(weight)

    new_bmi = get_bmi_number(converted_height, converted_height)

    if new_bmi >= 30:
        statement = "Obese"

    if 25 <= new_bmi < 30:
        statement = "Overweight"

    if 18.5 <= new_bmi < 25:
        statement = "Normal Weight"

    if new_bmi < 18.5:
        statement = "Underweight"

    return statement


def main_bmi():

    while True:

        feet = float(input('Enter feet of height: '))
        inches = float(input('Enter inches of height: '))
        pounds = float(input('Enter weight in pounds: '))

        resultant = tell_bmi(feet, inches, pounds)

        print(resultant)
        print('\n')

        returner = input('Do you want to return to the main menu: (y) or (n)')

        if returner == 'y':
            return


# functions for Distance Formula
def subtract_x_values(x_point1, x_point2):  # subtract X values
    return x_point2 - x_point1


def subtract_y_values(y_point1, y_point2):  # subtract Y Values
    return y_point2 - y_point1


def square_x_value(x_value):  # square X Values
    return x_value * x_value


def square_y_value(y_value):  # square Y Values
    return y_value * y_value


def add_value(x_squared, y_squared):  # add squared values together
    return x_squared + y_squared


def get_distance(total_before_squaring):  # get square root of distance
    return math.sqrt(total_before_squaring)


def distance_formula(x1_value, y1_value, x2_value, y2_value):  # aggregate functions to perform distance formula
    first_parenthesis = subtract_x_values(x1_value, x2_value)
    second_parenthesis = subtract_y_values(y1_value, y2_value)
    square_first_parenthesis = square_x_value(first_parenthesis)
    square_second_parenthesis = square_y_value(second_parenthesis)
    total_values = add_value(square_first_parenthesis, square_second_parenthesis)
    final_distance = get_distance(total_values)

    return final_distance


def calculate_distance():
    while True:
        x1_value = int(input('Enter X coordinate of First point: '))
        y1_value = int(input('Enter Y coordinate of First point: '))
        x2_value = int(input('Enter X coordinate of Second point: '))
        y2_value = int(input('Enter Y coordinate of Second point: '))
        resultant = distance_formula(x1_value, y1_value, x2_value, y2_value)
        print(resultant)
        print('\n')
        returner = input('Do you want to return to the main menu: (y) or (n)')
        if returner == 'y':
            return


# Functions for Retirement

def convert_percentage(amount, percentage):
    return amount * percentage


def matched_savings(amount):
    return amount + amount


def increase_age(age):
    return age + 1


def total_savings_amount(my_part, employer_part):
    return my_part + employer_part


def get_retirement(start_age, salary, percentage, goal):

    total_savings = 0

    final_age = start_age

    while total_savings < goal:
        my_percentage = convert_percentage(salary, percentage)
        employer_match = matched_savings(my_percentage)
        total_savings = total_savings + total_savings_amount(my_percentage, employer_match)
        final_age = increase_age(final_age)

        if final_age >= 100:
            print('Goal not met')
            break

    print('Goal met by age ' + str(final_age))

    return


def retirement_plan():
    while True:
        user_age = int(input('Enter your current age: '))
        user_annual_salary = float(input('Enter annual salary: $'))
        user_percentage = float(input('Enter percentage saved (as a decimal percentage): '))
        user_goal = float(input('Enter desired retirment savings goal: $'))
        get_retirement(user_age, user_annual_salary, user_percentage, user_goal)
        print('\n')
        returner = input('Do you want to return to the main menu: (y) or (n)')
        if returner == 'y':
            return

# ============== EMAIL VERIFICATION SECTION ============= #

# Check to make sure '@' symbol is present at least once but no more than once
def verifyAtSymbol(string):
    count = 0
    stringLength = len(string) - 1
    while (stringLength >= 0):
        if (string[stringLength] == '@'):
            count += 1
        stringLength -= 1
    return count == 1

# Check to make sure '.' symbol is present at least once
def verifyDotSymbol(string):
    count = 0
    stringLength = len(string) - 1
    while (stringLength >= 0):
        if (string[stringLength] == '.'):
            count += 1
        stringLength -= 1
    return count >= 1
     
# Check to make sure domain is equal to or less than 3 characters
def verifyDomain(string):
    domain = string.split('.')
    return len(domain[1]) <= 3

def email_verifier():

    while True:
        enteredEmail = str(input('Enter e-mail to be verified: '))
        
        if verifyAtSymbol(enteredEmail) and verifyDotSymbol(enteredEmail) and verifyDomain(enteredEmail):
            print("Valid Email\n")
        else:
            print("Invalid Email\n")
            
        print("Would you like to verify another email address?")
        emailMenu = input ("Enter 'y' for yes, otherwise enter anything else to return to the main menu: ")
        
        if (emailMenu != 'y'):
            break

# running test


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(convert_feet_to_inches(1), 12)

    def test2(self):
        self.assertEqual(convert_feet_to_inches(1.0), 12)

    def test3(self):
        self.assertEqual(convert_feet_to_inches(1), 12.0)

    def test4(self):
        self.assertEqual(convert_feet_to_inches(1.1), 12.0)


if __name__ == '__main__':
    unittest.main(exit=False)


while True:
    print('1. Calculate BMI')
    print('2. Calculate Distance Formula')
    print('3. Calculate Retirement')
    print('4. Verify Emails')
    print('Enter anything else to exit.\n')

    choice = (input('Please choose an option: '))

    if choice == '1':
        main_bmi()
    elif choice == '2':
        calculate_distance()
    elif choice == '3':
        retirement_plan()
    elif choice == '4':
        email_verifier()
    else:
        sys.exit()
