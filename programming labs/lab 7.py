# Lab 07 - Calendar Verification System

# Taking input
year = int(input("Enter year: "))

# Validating year
if year <= 0:
    print("Error: Please enter a positive year.")

else:
    # Checking leap year
    if year % 400 == 0:
        status = "LEAP YEAR"
        reason = "Divisible by 400"

    elif year % 100 == 0:
        status = "COMMON YEAR"
        reason = "Century year not divisible by 400"

    elif year % 4 == 0:
        status = "LEAP YEAR"
        reason = "Divisible by 4 and not a century year"

    else:
        status = "COMMON YEAR"
        reason = "Not divisible by 4"

    # Calendar details
    if status == "LEAP YEAR":
        february = 29
        days = 366
    else:
        february = 28
        days = 365

    # Displaying results
    print("\n------ CALENDAR VERIFICATION SYSTEM ------")
    print("Year:", year)
    print("Status:", status)
    print("Days in Year:", days)
    print("Days in February:", february)
    print("Reason:", reason)
    print("------------------------------------------")