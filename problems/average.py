l = []
while True:
    number= int( input("enter the number: "))
    if number==0:
        break
    l.append(number)
print(l)
s=0
for i in l:
    s+=i
print(s/len(l))



