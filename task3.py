total_purchase = float(input("Enter total purchase amount: "))
if total_purchase > 100000:
    discount = 0.10
elif total_purchase > 50000:
    discount = 0.05
else:
    discount = 0.0

final_amount = total_purchase - (total_purchase * discount)
print(f"Total amount to be paid: {final_amount}")
