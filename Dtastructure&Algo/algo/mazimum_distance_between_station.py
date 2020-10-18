"""given the number of cities n numbered from p to n-1 and the cities in which station are located . the task
is to fin the maximum distance between any city and its nearest station """

num_city=6
stations=[3]
max_distance=0

for i in range(num_city):
    nearest_station = 99999999
    for sta in stations:
        if(abs(i-sta)<nearest_station):
            nearest_station=abs(i-sta)
    if max_distance<nearest_station:
        max_distance=nearest_station
print(max_distance)
