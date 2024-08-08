# fav_anime=input('what is your favourite anime ? ')
# fav_animecharac=input("favourite anime character ? ")
# quote_of_favcharac=input(fav_animecharac+' favourite quotes ')
# print(fav_anime+" has this character "+fav_animecharac+" whose fav quote is "+"\'"+quote_of_favcharac+"\'")
# Formatted strings which help the user to visualize how the output will be displayed
# name='Retam'
# age='20'
# msg=f"My name is '{name}' and age is '{age}'";
# # formatted string
# print(msg)
# string='Python for Beginners'
# print(string.casefold())
# print(string.find('for'))
# the find method of string returns the index of the substring in the ori string
# var = 'for' in string
# print(var)
# var contains a boolean expression using the in operator
# print(string.title())
# title method returns a string where every word's first letter is a capital letter
# Math functions
# import calendar as cd
# calendar = cd.calendar(2024)
# print(type(calendar))
# print(calendar)
# print('hello')
# print('world')
# pattern program 1
# for x in range(1,6):
#     for z in range(x,6):
#         print(' ',end="")
#     for y in range(1,x+1):
#         print('* ', end="")
#     print('')
# # print(' ',end="")
# for x in range(7,0,-1):
#     for z in range(x,7):
#         print(' ',end="")
#     for y in range(1,x):
#         print('* ',end="")
#     print('')
#

# import maskpass
# # print('pasword :')
# password=maskpass.askpass(prompt="Enter you password ",mask="")
# if len(password)!=0:
#     print(' password recieved')
# else:
#     print('password not recieved ')
# Echoing password and masked with hashtag(#)
# import maskpass # importing maskpass library
#
# # prompt msg = Password and
# # masking password with hashtag(#)
# pwd = maskpass.askpass(prompt="Password:", mask="#")
# print(pwd)
name='Retams'
print(name[:])
# starting index:end index this operator creates a new string from the starting index to the end index from the existing string
#the default values for starting index=0 and end index=len(string)
print(name[::-1])
print(name[:2])
# this : splicing operator in python has its own syntax which is  start:end:jump example 1:4:2
print(name[::2])
# the output of the above statement will be Rtm printing only the characters in the multiples of two
print(name[::-1])
# this will print the string in reverse
print(name[::-2])
# the above code will also print the string in reverse but will also do charac jumping at the multiples of two

