sequence=[]
while True:
    num=int(input("enter the numbers: "))
    if num==0:
        break
    sequence.append(num)
def oddpair(sequence):
    for i in sequence:
        for j in sequence:
            if i is j:
                continue
            k=i*j
            if k%2!=0:
                return True
    return False

print(oddpair(sequence))
        
 