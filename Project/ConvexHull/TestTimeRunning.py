import time
from QuickHull import quick_hull
from JarvisMarch import jarvis_march
from GrahamScan import graham_scan

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
    
    # Time execution of Graham Scan algorithm
    start_time = time.time()
    graham_scan(points)
    print("Graham Scan: %s seconds" % (time.time() - start_time))

    # Time execution of Jarvish March algorithm
    start_time = time.time()
    jarvis_march(points)
    print("Jarvish March: %s seconds" % (time.time() - start_time))

    # Time execution of Quick Hull algorithm
    start_time = time.time()
    quick_hull(points)
    print("Quick Hull: %s seconds" % (time.time() - start_time))