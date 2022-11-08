import matplotlib.pyplot as plt
import numpy as np
import math


# Find distance between 2 vectors
def distance(left_most, right_most, point):
    vector1 = [left_most[0] - right_most[0], left_most[1] - right_most[1]]
    vector2 = [point[0] - right_most[0], point[1] - right_most[1]]

    length1 = math.sqrt(math.pow(vector1[0], 2) + math.pow(vector1[1], 2))
    length2 = math.sqrt(math.pow(vector2[0], 2) + math.pow(vector2[1], 2))

    if length1 == 0 or length2 == 0:
        return 0

    sin_theta = math.sqrt(1 - math.pow(np.dot(vector1, vector2)/(length1 * length2), 2))

    return sin_theta * length2


# Check 2 vectors are clockwise or not
def is_clockwise(left_most, right_most, point):
    vector1 = [left_most[0] - right_most[0], left_most[1] - right_most[1]]
    vector2 = [point[0] - right_most[0], point[1] - right_most[1]]

    if np.cross(vector1, vector2) == 0:
        return -1
    elif -np.cross(vector1, vector2) > 0:
        return 0
    else:
        return 1


# Find the furthest point from a specific vector
def furthest(sorted_points, left_most, right_most, flag):
    index1 = sorted_points.index(left_most)
    index2 = sorted_points.index(right_most)
    list_points = sorted_points[index1: index2 + 1]
    max = 0
    furthest_point = None


    if flag == "below":
        for p in list_points:
            if is_clockwise(left_most, right_most, p) == 1:
                dist = distance(left_most, right_most, p)

                if dist > max:
                    max = dist
                    furthest_point = p
    else:
        for p in list_points:
            if is_clockwise(right_most, left_most, p) == 1:
                dist = distance(left_most, right_most, p)

                if dist > max:
                    max = dist
                    furthest_point = p
    
    return furthest_point


# Find the hull
def find_hull(sorted_points, left_most, right_most, flag):
    furthest_point = furthest(sorted_points, left_most, right_most, flag)
    
    if furthest_point is None:
        return []

    lst = []
    lst.append(furthest_point)

    lst += find_hull(sorted_points, left_most, furthest_point, flag)
    lst += find_hull(sorted_points, furthest_point, right_most, flag)

    return lst


# Quick Hull algorithm
def quick_hull(points):
    if len(points) <= 2:
        return -1

    sorted_points = sorted(points, key=lambda x: x[0])
    left_most = sorted_points[0]
    right_most = sorted_points[-1]

    hull = []
    hull = hull + [left_most] + sorted(find_hull(sorted_points, left_most, right_most, "above"), key=lambda x: x[0]) + [right_most]
    hull = hull + sorted(find_hull(sorted_points, left_most, right_most, "below"), key= lambda x: x[0], reverse= True) + [left_most]

    return hull

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
    boundary = quick_hull(points)

    if boundary == -1:
        print("Can not create a convex hull!")
        print("There must be at least 3 points")
    else:
        bound_x = [x[0] for x in boundary]
        bound_y = [y[1] for y in boundary]
        
        plt.plot(bound_x, bound_y, color = 'r')

    plt.show()