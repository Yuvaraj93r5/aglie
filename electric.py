units=int(input("enter number of units consumed: "))
if units<=100:
  bill=units*2
elif units<=200:
  bill=(100*2)+((units-100)*3)
else:
  bill=(100*2)+(100*3)+((units-100)*5)
print("Total Electricity Bill = RS."bill)
