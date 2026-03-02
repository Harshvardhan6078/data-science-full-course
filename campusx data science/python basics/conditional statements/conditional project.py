# concept of break , continue , pass





pop = 10000
year = 2025

year2 = int(input("please enter the year at which you want to see te population"))

while year2  >= year :
    pop = pop + (pop/10)
    print("in year",year,"population will be",pop)
    year +=1
    exit

else:
    if year2 < (year - 1) :
        print("please give correct input")
    