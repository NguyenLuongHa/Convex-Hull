import math
import matplotlib.pyplot as plt
import numpy as np


# Find the point has the lowest coordinate
def lowest_coordinate(points):
    min = points[0]

    for p in points:
        if p[1] < min[1]:
            min = p
    
    return min


# Calculate the angle
def angle(lowestPoint, point):
    if lowestPoint[0] == point[0]:
        return 90

    p = [point[0], lowestPoint[1]]
    opposite = math.sqrt(math.pow(p[0] - point[0], 2) + math.pow(p[1] - point[1], 2))
    adjacent = math.sqrt(math.pow(p[0] - lowestPoint[0], 2) + math.pow(p[1] - lowestPoint[1], 2))
    angle = 0

    if point[0] < lowestPoint[0]:
        angle = 180 - math.degrees(math.atan(opposite / adjacent))
    else:
        angle = math.degrees(math.atan(opposite / adjacent))

    return angle


# Sort by angle
def sort_by_angle(lowestPoint, points):
    lst = dict()

    for p in points:
        if p == lowestPoint:
            continue

        coor = angle(lowestPoint, p)
        lst.update({p: coor})

    sorted_list = {k: v for k, v in sorted(lst.items(), key=lambda item: item[1], reverse= True)}

    return list(sorted_list.keys())


# Check 2 vectors are clockwise or not
def isClockWise(vector1, vector2):
    if np.cross(vector1, vector2) == 0:
        return -1
    elif -np.cross(vector1, vector2) > 0:
        return 0
    else:
        return 1


# Graham Scan algorithm
def graham_scan(points):
    if len(points) <= 2:
        return -1

    lowestPoint = lowest_coordinate(points)
    sorted_list = sort_by_angle(lowestPoint, points)
    stack = [lowestPoint]
    index = 0

    for p in sorted_list:
        running = True

        while running:
            if len(stack) <= 1:
                stack.append(p)
                index += 1
                running = False
                continue
            
            vector1 = [stack[index - 1][0] - stack[index][0], stack[index - 1][1] - stack[index][1]]
            vector2 = [p[0] - stack[index][0], p[1] - stack[index][1]]

            if isClockWise(vector1, vector2) == 1:
                stack.append(p)
                index += 1
                running = False
            else:
                stack.pop()
                index -= 1

    stack.append(lowestPoint)

    return stack

# Read set of points from text file
def read_file(filename):
    file = open(filename, "r")
    data = file.read()
    lst = data.splitlines()
    lst.pop()

    points = []

    for p in lst:
        temp = p.strip("()")
        coor = temp.split(", ")
        points.append((int(coor[0]), int(coor[1])))

    return points

# Main
if __name__ == "__main__":
    points = read_file("points.txt")
    
    x_points = [x[0] for x in points]
    y_points = [y[1] for y in points]
    
    plt.scatter(x_points, y_points)
    
    # Drawing boundary
    boundary = graham_scan(points)

    if boundary == -1:
        print("Can not create a convex hull!")
        print("There must be at least 3 points")
    else:
        bound_x = [x[0] for x in boundary]
        bound_y = [y[1] for y in boundary]
        
        plt.plot(bound_x, bound_y, color = 'r')

    plt.show()