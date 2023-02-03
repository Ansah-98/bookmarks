in_x  = int(input("enter a number "))
in_y  = int(input("enter another number\n "))

print("now we are going to check the hcf of the two numbers \n ")

def hcf(x , y ):
    maxi = 0

    if x > y :
        mini = y
    else:
        mini = x

    for i in range(mini):
        if x % (i +1 ) == 0 and y % (i+1)==0:
            maxi = i+1 
    return  f"the highest common factor of {x} and {y} is {maxi}" 


print(hcf(in_x,in_y))