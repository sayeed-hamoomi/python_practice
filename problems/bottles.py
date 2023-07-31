l1=0.10
g1=0.25
#lessthan one litre bottle deposite
small_bottle= float(input("number of small bottles: ")) 
#greaterthan one litre bottle deposite
large_bottle= float(input("number of large bottles: "))
#refund of the bottles by sizes
refund=(l1*small_bottle)+(g1*large_bottle)
#totalrefund
print(f"total_refund: ${round(refund,2)}")