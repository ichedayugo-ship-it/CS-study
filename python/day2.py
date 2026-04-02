score = int(input("Enter the score "))
if score >= 80:
    print("Excellent")
elif score >=60:
    print("Pass")
else:
    print("Fail")

temperature = int(input("Enter the temperature: "))
if temperature >30:
    print("Hot")
elif temperature >20:
    print("Warm")
else:
    print("Cold")

number = int(input("Enter the number: "))
if number >0:
    print("Positive")
elif number ==0:
    print("Zero")
else:
    print("Negative")