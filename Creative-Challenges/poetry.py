import syllables
import random

# Finds words with particular number of syllables
def find_word(num_syllables):
    with open("word_list.txt") as f:
        syllable = float('inf')
        while syllable != num_syllables:
            word = random.choice(f.readlines())
            word = word[:-1]
            syllable = syllables.estimate(word)
        return word

def make_line(num_syllables):
    with open("word_list.txt") as f:
        syllable = float('inf')
        while syllable < num_syllables:
            word = random.choice(f.readlines())
            word = word[:-1]
            syllable = syllables.estimate(word)
    
    word += find_word(num_syllables-syllable)
    return word
        
        
    # returns line with given syllables

if __name__ == "__main__":
    print(make_line(5))