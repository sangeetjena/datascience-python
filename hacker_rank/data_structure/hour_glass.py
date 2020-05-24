arr = [[1,1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]]


max_len = len(arr)
prev_sum=-9999
for i in range(1,max_len-1):
    for j in range(1,max_len-1):
        curr_sum =arr[j-1][i-1] + arr[j-1][i] + arr[j-1][i+1] + arr[j][i] + arr[j+1][i-1] + arr[j+1][i] + arr[j+1][i+1]
        if prev_sum < curr_sum:
            prev_sum=curr_sum

print(prev_sum)