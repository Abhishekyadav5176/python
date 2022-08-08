# # name = input("enter your name\n")
# # print("good morning,"+ name)


# # second question 2.0
# letter =''' Dear <|NAME|>,
# Greeting from abc coding house i am happy to tell you about your 
# selection you are seleted
# Have agreat day
# thanks for parsipates bro
# Date : <|date|>'''

# letter ="Dear harry ,\n\tthis python course is nice!,\nthanks"
# print(letter)

# st = "this is a string with double  space"
# doublespace = st.find("  ")
# print(doublespace)

from asyncio import AbstractChildWatcher


letter = '''Dear <|NAME|>,
GREETINGS FROM ABC CODING HOUSE
THANKS
Date: <|DATE|>,'''
# print(letter)
name = input ("enter your name\n")
date = input ("enter date\n")
letter =letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print (letter)

