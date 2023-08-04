og_prices=[4.95,9.95,14.95,19.95,24.95]
print("origin price\t|discounted price\t|new prices")
# print("____________________")
for i in og_prices:
    print(f"{i}\t\t|{i*60/100}\t\t|{round(i-i*60/100,2)}")

    
    