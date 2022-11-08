import random as rand

number = int(input("Enter the number of points: "))
points = open("points.txt", "w")

for i in range(number):
    x_coor = rand.randint(-number, number)
    y_coor = rand.randint(-number, number)
    points.write(str((x_coor, y_coor)) + "\n")

points.close()