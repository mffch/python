import string
import random

def password(lettersnumbers=8):
    x=string.digits + string.ascii_letters
    return ''.join(random.choice(x) for i in range(lettersnumbers) )