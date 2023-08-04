humnan_years=int(input("enter the human years: "))

if (humnan_years<=2 and humnan_years>0):
    print(f"your dog age is: {humnan_years*10.5}")
elif humnan_years<=0:
    raise ValueError("age can only be positive")
else:
    print(f"your dog age is: {21+(humnan_years-2)*4}")
        
