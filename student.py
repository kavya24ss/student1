principal = float(input("Enter the Principal amount: ")) 
rate = float(input("Enter the Rate of Interest (in %): ")) 
time = float(input("Enter the Time (in years): ")) 
simple_interest = (principal * rate * time) / 100 
amount = principal * (1 + rate / 100) ** time 
compound_interest = amount - principal 
print("\n--- Results ---") 
print("Simple Interest =", simple_interest) 
print("Compound Interest =", compound_interest) 
