  
""" Hackathon - Level 5 """

def convert(numeral):
    conv = {"I": 1, "X": 10, "C": 100, "M": 1000, "V": 5, "L": 50, "D": 500}
    summed = 0
    for i, s in enumerate(numeral):
        temp_s = conv[s]
        if i < len(numeral)-2:
            if conv[numeral[i+1]] > temp_s:
                temp_s = -temp_s
        summed += temp_s
    return summed

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return 1145
    print(convert('MCXLV'))
