print("Welcome to the tip calculator.")

Total_Bill = input("What was the total bill? $")

Tip = input("What percentage tip would you like to give? 10, 12 or 15? ")

People_Split = input("Hoe many people to split the bill? ")

Bill_with_tip = float(Total_Bill) + (float(Total_Bill)*(float(Tip)/100))

Each_person_bill = round(Bill_with_tip / float(People_Split),2)

print(f"Each person should pay: ${Each_person_bill}")