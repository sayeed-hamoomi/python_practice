min=float("inf")
max=float("-inf")
l=[]


while True:
    n=int(input("enter the number: (0 to exit)"))
    if n==0:
        break
    l.append(n)
for i in l:
    if i <min:
        min =i
    if i>max:
        max=i

print(min, max)

