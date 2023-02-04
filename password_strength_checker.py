'''
------------------------------------Password Strength Checker------------------------------------
'''


import string
import getpass


def check_password_strength():
   password = getpass.getpass('Enter the password: ')
   if len(password) < 8:
        print("Error.....password must be of minimum 8 characters..!!")
        print("Look for another one.")
        return 0
   strength = 0
   remarks = ''
   lower_count = upper_count = num_count = wspace_count = special_count = 0

   for char in list(password):
       if char in string.ascii_lowercase:
           lower_count += 1
       elif char in string.ascii_uppercase:
           upper_count += 1
       elif char in string.digits:
           num_count += 1
       elif char == ' ':
           wspace_count += 1
       else:
           special_count += 1

   if lower_count >= 1:
       strength += 1
   if upper_count >= 1:
       strength += 1
   if num_count >= 1:
       strength += 1
   if wspace_count >= 1:
       strength += 1
   if special_count >= 1:
       strength += 1

   if strength == 1:
       remarks = ('It is a very weak password.'
           ' Change it as soon as possible.')
   elif strength == 2:
       remarks = ('That\'s still a weak password.'
           ' You should look for another one.')
   elif strength == 3:
       remarks = 'This password is fine, but it can be improved.'
   elif strength == 4:
       remarks = ('It is a tough password.'
           ' But still there is a room for improvement.')
   elif strength == 5:
       remarks = ('That\'s a strong password...!!'
           ' Guessing your password is tough.')

   print('\n******  Your password has  ******\n')
   print(f'Total characters : {len(password)} ') 
   print(f'Lowercase letters : {lower_count}')
   print(f'Uppercase letters : {upper_count}')
   print(f'Digits : {num_count}')
   print(f'Whitespaces : {wspace_count}')
   print(f'Special characters : {special_count}')
   print(f'Password Strength : {(strength / 5)*100}%')
   print(f'Remark : {remarks}')


def check_pwd(another_pw=False):
   valid = False 
   if another_pw:
       choice = input(
           'Do you want to check another password\'s strength (y/n) : ')
   else:
       choice = input(
           'Do you want to check your password\'s strength (y/n) : ')

   while not valid:
       if choice.lower() == 'y':
           return True
       elif choice.lower() == 'n':
           print('Exiting...!')
           return False
       else:
           print('Invalid input...please try again. \n')
           return 0


if __name__ == '__main__':
   print('\n----------Check password strength----------\n')
   check_pw = check_pwd()
   while check_pw:
       check_password_strength()
       check_pw = check_pwd(True)
