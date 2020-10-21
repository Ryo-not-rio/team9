""" Hackathon - Level 3 """

def oddish_evenish(x):
    if sum([int(i) for i in list(str(x))]) % 2 == 0:
        return "Evenish"
    return "Oddish"

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return Oddish
    print(oddish_evenish(1190))
    
