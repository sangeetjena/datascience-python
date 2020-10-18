"""Given arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop.
"""

arrival=[9.0,9.40,9.50,11.00,15.00,18.00]
dept=[9.10,12.00,11.20,11.30,19.00,20.00]
book=[]
for i in range(0,len(arrival)):
    found=0
    for j in range(0,len(book)):
        if(arrival[i]>book[j]):
            book[j]=dept[i]
            found=1
            break
    print(found)
    if found==0:
        book.append(dept[i])
    print(book)
print(len(book))
print(book)