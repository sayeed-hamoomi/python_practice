deposit_amonut=float(input("enter the amount yo deposit: "))
interest_rate=4/100
amount_1=deposit_amonut+deposit_amonut*interest_rate
amount_2=amount_1+amount_1*interest_rate
amount_3=amount_2+amount_2*interest_rate
print(f"first year balance:${round(amount_1,2)}\nsecond year balance: ${round(amount_2,2)}\nthird year banlance: ${round(amount_3,2)} ")