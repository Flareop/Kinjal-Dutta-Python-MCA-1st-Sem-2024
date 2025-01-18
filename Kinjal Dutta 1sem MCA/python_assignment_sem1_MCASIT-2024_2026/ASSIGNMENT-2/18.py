
health = input("Enter the health condition (excellent/poor): ").strip().lower()
age = int(input("Enter the age of the person: "))
residence = input("Enter the residence type (city/village): ").strip().lower()
sex = input("Enter the sex of the person (male/female): ").strip().lower()

if health == "excellent" and 25 <= age <= 35 and residence == "city":
    if sex == "male":
        premium_rate = 4
        policy_limit = 200000
        print("The person is insured.")
        print(f"Premium rate: Rs. {premium_rate} per thousand")
        print(f"Maximum policy amount: Rs. {policy_limit}")
    elif sex == "female":
        premium_rate = 3
        policy_limit = 100000
        print("The person is insured.")
        print(f"Premium rate: Rs. {premium_rate} per thousand")
        print(f"Maximum policy amount: Rs. {policy_limit}")
    else:
        print("Invalid input for sex.")
        
elif health == "poor" and 25 <= age <= 35 and residence == "village" and sex == "male":
    premium_rate = 6
    policy_limit = 10000
    print("The person is insured.")
    print(f"Premium rate: Rs. {premium_rate} per thousand")
    print(f"Maximum policy amount: Rs. {policy_limit}")
else:
    print("The person is not insured.")
