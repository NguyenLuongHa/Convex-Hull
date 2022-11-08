import matplotlib.pyplot as plt
import numpy as np


# Find the point has the left-most coordinate
def find_leftmost_point(points):
    left_most = points[0]

    for p in points:
        if p[0] < left_most[0]:
            left_most = p

    return left_most


# Check 2 vectors are clockwise or not
def isClockWise(current_point, stack_point, next_point):
    vector1 = [stack_point[0] - current_point[0], stack_point[1] - current_point[1]]
    vector2 = [next_point[0] - current_point[0], next_point[1] - current_point[1]]

    if np.cross(vector1, vector2) == 0:
        return -1
    elif -np.cross(vector1, vector2) > 0:
        return 0
    else:
        return 1


# Jarvis March algorithm
def jarvis_march(points):
    if len(points) <= 2:
        return -1

    leftmost_point = find_leftmost_point(points)
    current_point = None
    next_point = None
    stack = [leftmost_point]
    index = 0
    check_point = leftmost_point

    while True:
        for p in points:
            if p in stack:
                continue

            if current_point == None:
                current_point = p
                continue

            next_point = p

            if isClockWise(current_point, stack[index], next_point) == 0:
                current_point = next_point

        if check_point == current_point or current_point == None or isClockWise(current_point, stack[index], leftmost_point) == 0:
            break

        check_point = current_point
        stack.append(current_point)
        index += 1
        current_point = None

    stack.append(leftmost_point)
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
    boundary = jarvis_march(points)

    if boundary == -1:
        print("Can not create a convex hull!")
        print("There must be at least 3 points")
    else:
        bound_x = [x[0] for x in boundary]
        bound_y = [y[1] for y in boundary]
        
        plt.plot(bound_x, bound_y, color = 'r')

    plt.show()