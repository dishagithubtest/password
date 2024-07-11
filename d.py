import string
import random
if __name__ == "__main__":
    ascii1 = string.ascii_lowercase
    ascii2 = string.ascii_uppercase
    digits = string.digits
    punc = string.punctuation
    plen = int(input("Enter password length:"))
    s = []
    s.extend(list(ascii1))
    s.extend(list(ascii2))
    s.extend(list(digits))
    s.extend(list(punc))
    random.shuffle(s)
    print("The password is:")
    print("".join(s[0:plen]))


