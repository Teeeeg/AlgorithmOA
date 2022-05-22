from heapq import heappop, heappush


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    def __lt__(self, other):
        return getDistance(self) >= getDistance(other)


def find_closest_points(points, k):
    n = len(points)
    maxHeap = []

    for i in range(k):
        heappush(maxHeap, points[i])

    for i in range(k, n):
        if getDistance(points[i]) < getDistance(maxHeap[0]):
            heappop(maxHeap)
            heappush(maxHeap, points[i])

    return maxHeap


def getDistance(point):
    return (point.x ** 2 + point.y**2)


def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
