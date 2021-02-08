from modules.getting_username import *
from modules.output import *
from modules.calculation_palindrome import *

name = user_name()
word = user_input()
outcome = palindrome(word)
result = output(name, word, outcome)
print(result)





