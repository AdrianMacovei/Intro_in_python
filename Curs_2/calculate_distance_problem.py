'''
A cargo ship needs to pick and deliver containers in several ports.

The distance between ports is determined as an array (e.g. [75, 89, 90, 21, 30, 49]), meaning that the distance
between the starting point and port 1 is 75 miles, from port 1 to port 2 is 89 and so on.

The ship can travel to a port only from the neighbor ports (port #3 from example can be reached from port #2 or for
port #4, port #1 can be reached from the starting point and from port #2, the starting point can be reached only from
port #1 and so on). With the distances from the example below, this means that from the starting point to port #3, the
ship needs to travel 75+89+90 miles.

A route is received every morning from the logistics department as an array with the following format [5, 4, 2, 0, 3, 1],
specifying that the ship needs to travel from the starting point to port #5, then from #5 to #4 and so on.
At the end of the route, the ship needs to be back at the starting point.

Question 1 (Vessel Routes) - Requirement

Write a function that calculates how many miles will the ship travel for a certain route.

int CalculateDistance(int[] distances, int[] route);


Example:

int[] distances = new int[] { 75, 89, 90, 21, 30, 49 };

int[] route = new int[] { 2, 4, 1 };

The function should return 550 for the provided values.


Notes:

    You should only write the body of the function
    You can use any programming language
'''


def calculate_distance():
    distances = [75, 89, 90, 21, 30, 49]
    routes_of_the_day = [1, 3, 1, 3] # result = 941
    total_distance = 0
    current_port = 0

    for j in range(0, len(routes_of_the_day)):
        anterior_port = current_port
        current_port = routes_of_the_day[j]
        if anterior_port < current_port:
            for i in range(anterior_port, current_port):
                total_distance += distances[i]
        elif anterior_port > current_port:
            for i in range(anterior_port - 1, current_port - 1, -1):
                total_distance += distances[i]
    if current_port != 0:
        for i in range(current_port - 1, -1, -1):
            total_distance += distances[i]

    print(total_distance)


calculate_distance()
