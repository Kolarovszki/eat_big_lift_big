import argparse

from Utility.macros import get_macros

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--weight", help="Add your bodyweight")
    args = parser.parse_args()
    try:
        weight = int(args.weight)
        print(get_macros(weight))
    except ValueError:
        print("Please enter a number!")
