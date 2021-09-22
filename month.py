## month
## Ishai Masada
## Gives a message to the user based on the month of the year

def month():
    month = input("Type in the month of the year: ").title()
    months = {'January': "Happy New Year!", 'February': "Happy Valentine's Day!", 'March': "Happy St. Patrick's Day!", 'April': "Happy April Fools Day!", 'May': "Happy birthday if it's your birthday!", 'June': "Stay hydrated for the summer!", 'July': "Happy Fourth of July!", 'August': "Get ready for school!", 'September': "Have fun at school!", 'October': "Happy Halloween!", 'November': "Happy Thanksgiving!", 'December': "Merry Christmas!"}
    if month in months:
        print(months.get(month))
    else:
        print("Your input did not read as a month of the year")

month()
