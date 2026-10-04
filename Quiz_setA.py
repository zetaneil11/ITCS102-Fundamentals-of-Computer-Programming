name = input("Enter your name: ")
age = int(input("Enter your age: "))
rev = float(input("Enter monthly revenue: "))
cs = int(input("Enter credit score: "))
yrs_b = int(input("Years business: "))
has_defaults = bool(input("Default history: "))
collateral = input("Collateral: ")
c_value = float(input("Collateral value: "))

max_loan = 0
base_fee = 0.0

if age >= 21 and yrs_b >= 2 and has_defaults == False:
    print("Baseline passed")

    if cs >= 720:
        max_loan = rev * 3
        if rev >= 50000:
            base_fee = max_loan * 0.015
            print("base fee rate is" , base_fee)
        else:
            base_fee = max_loan * 0.025
            print("base fee rate is" , base_fee)

        if c_value >= max_loan:
            print("collateral", c_value, "is sufficient")

            if c_value % 5000 != 0:
                base_fee = base_fee + 250
                print("base fee rate is" , base_fee)

        else:
            print("collateral", c_value, "is insufficient")

    elif cs <= 620 and cs < 720:
        max_loan = rev * 1.5
        if yrs_b >= 5:
            base_fee = max_loan * 0.02
            print("base fee rate is" , base_fee)
        else:
            base_fee = max_loan * 0.035
            print("base fee rate is" , base_fee)

        if c_value >= max_loan:
            print("collateral", c_value, "is sufficient")
        else:
            print("collateral", c_value, "is insufficient")

            if c_value % 5000 != 0:
                base_fee = base_fee + 250
                print("base fee rate is" , base_fee)
            

    elif cs < 620:
        print("Rejected: Credit score below requirement")

    else:
        print("Not eligible for loan")

else:
    print("Rejected: High risk application")
