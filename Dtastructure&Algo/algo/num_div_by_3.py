def div_by_3(x):
    sum=0
    while x>0:
        sum=sum+x%10
        x=x//10
        print(x)
    mul=3
    print(sum)
    while (mul<=sum):
        mul=mul*3
        if(mul==sum):
            print("div by 3")
            break
div_by_3(81)

