month31=["january","march","may","july","august","october","december"]
months30=["april","june","september","november"]
month_name=input("enter the month: ")
if (month_name in month31):
    print("this month has 31 days")
elif (month_name in months30):
    print("this month has 30 days")
elif (month_name=="february"):
    print("this month has 28 or 29 days")
else :
    raise ValueError("Please provide a valid month and type it in lower case!")           