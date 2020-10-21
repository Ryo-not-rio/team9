""" Hackathon - Level 2 """

def longest_word(string):
    # Add your solution here. You can use additional functions if need be.
    # Don't forget to add a DocString for all your functions and comment your code.
    # Your functions should return values rather than printing the result although you can use printing for testing purposes.
    string = string.replace(",", " ") # Removes punctuation
    x = string.split() # Splits the sentence
    return max(x, key=len) # Returns the word with the most characters


if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return lorem
    print(longest_word("lorem ipsum, dolor sit amet"))
