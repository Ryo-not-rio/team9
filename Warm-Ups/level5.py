""" Hackathon - Level 5 """

def convert(numeral):
    conv = {"I": 1, "X": 10, "C": 100, "M": 1000, "V": 5, "L": 50, "D": 500}
    return int(sum([conv[s] for s in numeral]))

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return 1145
    print(convert('MCXLV'))
    
    
