"""
A cargo ship needs to pick and deliver containers in several ports.

The distance between ports is determined as an array (e.g. [75, 89, 90, 21, 30, 49]), meaning that the distance
between the starting point and port 1 is 75 miles, from port 1 to port 2 is 89 and so on.

The ship can travel to a port only from the neighbor ports (port #3 from example can be reached from port #2 or for
port #4, port #1 can be reached from the starting point and from port #2, the starting point can be reached only from
port #1 and so on). With the distances from the example below, this means that from the starting point to port #3, the
ship needs to travel 75+89+90 miles.

A route is received every morning from the logistics department as an array with the following format
[5, 4, 2, 0, 3, 1], specifying that the ship needs to travel from the starting point to port #5,
then from #5 to #4 and so on.
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
"""


def calculate_distance(distances, routes_of_the_day):
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


list_distances = [75, 89, 90, 21, 30, 49]
day_route = [1, 4, 1, 3]  # result = 941

# calculate_distance(list_distances, day_route)


'''
A planning software for a vessel transport company allows creating schedules for the days in which crew members work.

Each schedule has a start and end date (full day is considered). 

The software needs an improvement in order to create recurrences. A recurrence is created as following: start day of 
the month, number of working days, number of days off and the number of occurrences.  

Q2 (Working Schedules) - Requirement

Write a function that receives these parameters and outputs the working schedules. The working schedules will be 
displayed as a list of working intervals, in the format (startday, endday) of each interval.

The header of the function should be the following:

void DisplaySchedules(int startDay, int noOfWorkingDays, int noOfDaysOff, int noOfOccurences) 


Example:

For startday=1, noOfWorkingDats= 5, noofDaysOff= 3 and noOfOccurences = 5, the function should print: 

(1-5), (9-13), (17-21), (25-29), (3-7) 


Notes:

    You should consider that all months of the year have 30 days 
    You should only write the body of the function 
    You can use any programming language 
_________________________________________
'''


def planing_days(start_day_work, no_of_working_days, no_of_days_off, no_of_occurences):

    list_of_days = []

    while len(list_of_days) < no_of_occurences:
        start_day_work = start_day_work % 30
        finis_day_work = (start_day_work + no_of_working_days) - 1
        list_of_days.append(f"{start_day_work}-{finis_day_work}")
        start_day_work = finis_day_work + (no_of_days_off + 1)
    print(list_of_days)


planing_days(1, 5, 1, 4)
