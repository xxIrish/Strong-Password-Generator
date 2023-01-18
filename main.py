

#Password Generator

import random
#Here you are going to put in the characters
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()
number = "0123456789"
symbols= "!@#$%&*"

#Now we are going to tell it what to use from the list above
Use_for = lower_case + upper_case + number + symbols
length_for_pass = 24

#This is telling it how to compile the information that we have provided
password = "".join(random.sample(Use_for,length_for_pass))

print("Your Generated Password:")
print(*password, sep="")