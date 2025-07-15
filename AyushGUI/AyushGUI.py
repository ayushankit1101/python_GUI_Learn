# WAP to check for a perfect number

# Factors + Sum
# 6 = 3+2+1 = 6

n= int(input("enter any number "))
i=2
sum =0
while i<n:
    if(n%i==0):
        print(i)
        sum = sum+ i
    i+=1

print(" sum of all factors is = ",sum)

if n==sum:
    print("number is perfect ")
else:
    print("number is not perfect")


if sum ==0:
    print("prime number ")
else :
    print("Not Prime")