"""Given arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop.
"""

arrival=[9.0,9.40,9.50,11.00,15.00,18.00]
dept=[9.10,11.20,11.30,12.00,19.00,20.00]
i=1
j=0
platforms=1
maxplatform=1
while i<len(arrival) and j<len(dept):
    print(arrival[i],dept[j])
    if (arrival[i]<dept[j]):
        i=i+1
        platforms=platforms+1
    elif(arrival[i]>dept[j]):
        if(platforms>1):
            platforms=platforms-1
        j=j+1
    if(maxplatform<platforms):
        maxplatform=platforms
print(platforms)