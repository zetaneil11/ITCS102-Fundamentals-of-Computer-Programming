import getpass

username = input("Enter your username--> ")
password = getpass.getpass("Enter your password--> ")

first_name = input("Enter your first name--> ")
job_description = input("What is your job description--> ")
age = int(input("Enter age--> "))
is_employed = input("Are you currently employed? --> ")
credit_score = int(input("Credit Score history --> "))
annual_income = float(input("How much is your annual income? --> "))
has_collateral = input("Do you have any collateral --> ")
collateral = input("What is your collateral? --> ")
collateral_value = int(input("What is the value of your collateral? --> "))

username = "Neil"
password = "1234"

if username == "Neil" and password == "1234":
    print("Username and password correct")

else:
    print("Username and password incorrect")

if age >= 21 and age <= 65 and is_employed == "yes":
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

    if collateral_value <= 30000:
        print("Invalid")

    else:
        print("valid")
else:
    print("Unrecognized conditions")
