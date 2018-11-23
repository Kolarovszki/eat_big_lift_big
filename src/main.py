import argparse


def get_macros(weight):
    macros = {}
    prot = 2.2 * weight
    macros["Protein"] = prot
    cal = 40.0 * weight
    macros["Calories"] = cal
    macros["Fat"] = cal * 0.3
    macros["Carbohydrates"] = (0.7 * cal - prot * 4.0) / 4.0

    return macros


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--weight", help="Add your bodyweight")
    args = parser.parse_args()
    try:
        weight = int(args.weight)
        print(get_macros(weight))
    except ValueError:
        print("Please enter an integer!")
