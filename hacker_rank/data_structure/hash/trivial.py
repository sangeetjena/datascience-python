def insert(dict, value):
    dict[value] = 1
if __name__ == "__main__":
    dict = {}
    arr = [1,3,-3,5,-7,8]
    for x in arr:
        insert(dict,x)
    try:
            if (dict[-2] == 1):
                print("value present " + str(dict[-3]))
    except :
            print("not present")
