def korok_seed_guide():
    print("Welcome to The Korok Seed Guide!")
    print("1. Create the Korok Seed Guide")
    print("2. Add a feature to help players find all 900 Korok seeds")
    print("3. Offer help levels based on player credits")
    
    credits = int(input("Enter your available credits: "))
    if credits >= 5:
        print("You have enough credits for advanced help!")
    elif credits >= 1:
        print("You can access basic hints!")
    else:
        print("You need more credits to access help.")
