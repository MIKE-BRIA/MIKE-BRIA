def determine_generation(year):
    if year >= 1997:
        return "Generation Z"
    elif year >= 1981:
        return "Millennials"
    elif year >= 1966:
        return "Generation X"
    elif year >= 1946:
        return "Baby Boomers"
    else:
        return "Silent Generation or earlier"

birth_year = int(input("Enter your birth year: "))
generation = determine_generation(birth_year)
print("Your generation is:", generation)
