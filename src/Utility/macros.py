def get_macros(weight):
    macros = {}
    prot = 2.2 * weight
    cal = 40.0 * weight
    macros["Protein"] = prot
    macros["Calories"] = cal
    macros["Fat"] = cal * 0.3
    macros["Carbohydrates"] = (0.7 * cal - prot * 4.0) / 4.0
    return macros

#for i, k in get_macros(weigth).items():
#    print(i,k)


