""" Hackathon - Level 6 """

alphabet = "abcdefghijklmnopqrstuvwxyz"

def cipher(str, x):
    return "".join([alphabet[(alphabet.index(s)+x)%26] for s in str])

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return salve
    print(cipher('pxisb', 3))
