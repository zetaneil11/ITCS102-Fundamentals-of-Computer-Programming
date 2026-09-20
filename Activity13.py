#age (Integer)
#is_employed (boolean)
#credit_score (integer)
#annual_income (float)
#has_collateral (boolean)

age = int(input("Enter age: "))
is_employed = input("Are you currently employed? --> ")
credit_score = int(input("Credit Score history --> "))
annual_income = float(input("How much is your annual income? --> "))
has_collateral = input("Do you have any collateral --> ")


if age >= 21 and is_employed == "yes":
    print("Passed baseline eligibility")

    if credit_score >= 750:
        print("Your credit score is above 750")

        if annual_income >= 100000:
            print("You have a high annual income")
            base_rate = 4.5
            print("Your interest rate is ", base_rate)

        else:
            base_rate = 4.5
            print("Your interest rate is ", base_rate)

    elif credit_score >= 600:

        if has_collateral == "yes":
            base_rate = 7.0
            print("Your interest rate is ", base_rate)

        elif annual_income >= 40000:
            base_rate = 9.5
            print("Your interest rate is ", base_rate)

        else:
            base_rate = 8.0
            print("Your interest rate is ", base_rate)

    elif credit_score < 600:
        print("Credit Score is low failed")

else:
    print("Unrecognized conditions")
