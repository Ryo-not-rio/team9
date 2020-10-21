""" Hackathon - Level 1 """

def min_max_product(list):
    Minimum = Lst[0]
    Maximum = Lst[0]
    for Item in Lst[1:]:
        Minimum = min(Minimum, Item)
        Maximum = max(Minimum, Item)

    Product = Maximum * Minimum
    return Product

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return 200
    print(min_max_product([2, 100, 24, 15, 4, 9, 61]))
