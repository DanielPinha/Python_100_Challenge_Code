print("Welcome to the tip calculator.")
# Total bill without adding tip
total_bill = float(input("What was the total bill? $"))
# Tip percentage assuming only possibility of 10, 12 or 15
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# Number of people
num_people = int(input("How many people to split the bill? "))

# Total bill with tip added
total_bill_tip = total_bill * (1 + tip_percentage / 100)
# Bill divided for each person
bill_per_person = total_bill_tip / num_people

# Output informing the value to pay
message = f"Each person should pay: ${round(bill_per_person,2)}"
print(message)
