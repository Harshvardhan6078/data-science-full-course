
# program to find the output of series up to n terms
# series = 1/1! + 2/2! + 3/3! + ..........

n = int(input("please enter the length of series"))
fact = 1
result = 0

for i in range (1 , n+1):
    fact = fact * i
    result = result + i/fact

print(result)