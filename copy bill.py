#!/usr/bin/python3
n = int(input("Enter the number of the copies: "))
if n <= 10 :
    B = n * 0.30
elif n > 10 and n <= 30 :
    B = 10 * 0.30 + (n - 10) * 0.25
else :
    B = 10 * 0.30 + 20 * 0.25 + (n - 30) * 0.20
print("The bill is:", B, "DH")