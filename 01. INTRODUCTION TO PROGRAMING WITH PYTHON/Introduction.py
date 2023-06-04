# WRITE A PROGRAM THAT WILL DISPLAY THE FOLLOWING QUESTIONS FOR USER:
#       “WHAT IS YOUR NAME?“
#        “HOW OLD ARE YOU?“
#        “WHERE DO YOU LIVE?“
# and will read the user's responses and display the corresponding messages:
#       “HELLO, (ANSWER(NAME))“.
#       “YOUR AGE IS  (ANSWER(AGE))“.
#       “YOU LIVE IN  (ANSWER(CITY))“.   

NAME = input("WHAT IS YOUR NAME? ")
AGE = int(input("HOW OLD ARE YOU? "))
CITY = input("WHERE DO YOU LIVE? ")
print(f"\n")
print(f"HELLO, {NAME}")
print(f"YOUR AGE IS {AGE}")
print(f"YOU LIVE IN {CITY}")
