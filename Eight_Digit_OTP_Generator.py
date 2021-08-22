import math
import random


def OTP_Generator():

     # We can use str or integers
     # str => Combining all strings (Digit1 + Digit2 + ...)
     # int => Adding each int multiplied with place values (Digit1 * 1000 + Digit2 * 100 + ...)

     # Integer method
     
     Digit1 = random.randint(1,9) # Make sure the 1st digit of 4 digit no./OTP is not zero
     Digit2 = random.randint(0,9)
     Digit3 = random.randint(0,9)
     Digit4 = random.randint(0,9)
     Digit5 = random.randint(0,9)
     Digit6 = random.randint(0,9)
     Digit7 = random.randint(0,9)
     Digit8 = random.randint(0,9)

     OTP = Digit1 * 10000000 + Digit2 * 1000000 + Digit3 * 100000 + Digit4 * 10000 + Digit5 * 1000 + Digit6 * 100 + Digit7 *10 + Digit8

     print('Your OTP is:',OTP)
     
     return OTP


if __name__ == '__main__':
     print(OTP_Generator())
