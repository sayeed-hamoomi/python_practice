vovels= ["a","e","i","o","u"]
words=input("enter the sentence: ")
total_count=0
for i in words:
    if i in vovels:
        total_count+=1
print(f"the sum of vovel: {total_count}")        
