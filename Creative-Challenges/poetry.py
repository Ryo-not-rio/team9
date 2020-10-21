import syllables

def make_line(num_syllables):
    # returns line with given syllables
    return num_syllables*"a"

if __name__ == "__main__":
    print("{0:^20}\n{1:^20}\n{2:^20}".format(make_line(5), make_line(7), make_line(5)))