char_list = [ chr(x) for x in range(ord('A'), ord('Z') + 1) ]
n = 3
count=0
lst=[]
final_lst=[]
def final_longest_path:
    tmp=None
    for x in final_lst:
        if x.count
def LongestPath(matrix):
    result = 1  # Initialize result
    global lst
    global  final_lst

    dup = [ [ -1 for i in range(n) ] for i in range(n) ]


    for i in range(n):
        for j in range(n):
            if (dup[ i ][ j ] == -1):
                stepFind(i, j, matrix, dup)

            final_lst.append(lst)
            print(final_lst)
            result = max(result, dup[ i ][ j ]);
            global count
            count = count+1

            lst=[]
            print('---------------------')
    return result


def stepFind(i, j, matrix, dup):
    # Base case
    global lst
    if (i < 0 or i >= n or j < 0 or j >= n):
        return 0

    if (dup[ i ][ j ] != -1):
        return dup[ i ][ j ]

    if (j < n - 1 and ((matrix[ i ][ j ] + 1) == matrix[ i ][ j + 1 ])):
        print('(', i, ',', j, ')', '->', char_list[ matrix[ i ][ j ] ])
        lst.append((char_list[ matrix[ i ][ j ] ],i,j))
        dup[ i ][ j ] = 1 + stepFind(i, j + 1, matrix, dup)
        return dup[ i ][ j ]

    if (j > 0 and (matrix[ i ][ j ] + 1 == matrix[ i ][ j - 1 ])):
        print('(', i, ',', j, ')', '->', char_list[ matrix[ i ][ j ] ])
        lst.append((char_list[ matrix[ i ][ j ] ], i, j))
        dup[ i ][ j ] = 1 + stepFind(i, j - 1, matrix, dup)
        return dup[ i ][ j ]

    if (i > 0 and (matrix[ i ][ j ] + 1 == matrix[ i - 1 ][ j ])):
        print('(', i, ',', j, ')', '->', char_list[ matrix[ i ][ j ] ])
        lst.append((char_list[ matrix[ i ][ j ] ], i, j))
        dup[ i ][ j ] = 1 + stepFind(i - 1, j, matrix, dup)
        return dup[ i ][ j ]

    if (i < n - 1 and (matrix[ i ][ j ] + 1 == matrix[ i + 1 ][ j ])):
        print('(', i, ',', j, ')', '->', char_list[ matrix[ i ][ j ] ])
        lst.append((char_list[ matrix[ i ][ j ] ], i, j))
        dup[ i ][ j ] = 1 + stepFind(i + 1, j, matrix, dup)
        return dup[ i ][ j ]

        # If none of the adjacent fours is one greater
    dup[ i ][ j ] = 1
    print('(', i, ',', j, ')', '->', char_list[ matrix[ i ][ j ] ])
    lst.append((char_list[ matrix[ i ][ j ] ], i, j))
    return dup[ i ][ j ]


# Driver program
matrix = [ [ 'A', 'B', 'X' ],
           [ 'D', 'C', 'E' ],
           [ 'E', 'F', 'H' ] ]
for i in range(n):
    for j in range(n):
        matrix[ i ][ j ] = char_list.index(matrix[ i ][ j ])


print("Length of the longest path is ", LongestPath(matrix))
print(lst)
