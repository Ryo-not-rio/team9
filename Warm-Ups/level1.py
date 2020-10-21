""" Hackathon - Level 1 """

def min_max_product(Lst):
    Product = min(Lst) * max(Lst)
    return Product

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return 200
    print(min_max_product([2, 100, 24, 15, 4, 9, 61]))
