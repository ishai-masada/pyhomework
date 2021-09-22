## Rectangle Area
## Ishai Masada
## Calculates the area for a rectangle

def rec_area():
    length = int(input('Type in the length of the rectangle: '))
    width = int(input('Type in the width of the rectangle: '))
    area = length*width
    if area < 0:
        print("Invalid input: measurements cannot be negative")
    else:
        print(area)

rec_area()
