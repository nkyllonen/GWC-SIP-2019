'''
Some more examples of using dictionaries.
'''

def main():
    data = {"a": {"Year" : 2000, "People" : 43820},
            "b": {"Year" : 2001, "People" : 834084},
            "c": {"Year" : 2000, "People" : 893042},
            "d": {"Year" : 2004, "People" : 8098},
            "e": {"Year" : 2004, "People" : 132},
            "f": {"Year" : 2004, "People" : 743892},
            "g": {"Year" : 2001, "People" : 9807}
            }

    totals = {}

    for y in data:
        d = data[y]
        print(d)
        if (d["Year"] in totals):
            # if we DO have this data point, add!
            totals[d["Year"]] += d["People"]
        else:
            # if we DON'T have this data point, append!
            totals[y] = d["People"]

    print(totals)

if __name__ == '__main__':
    main()
