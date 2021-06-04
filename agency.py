bike_model = input("Kindly fill in the model of your bike:")
distance_covered = input("Kindly enter the total distance covered in Km:")
distance_covered = float(distance_covered)

if (bike_model == "Yamaha") or (bike_model == "YAMAHA"):
    if distance_covered <=100:
        expense = (distance_covered * 130)
    elif (distance_covered > 100) and (distance_covered <=500):
        expense = (100 * 130) + ((distance_covered - 100)*115)
    else:
        expense = (100 * 130) + (400 * 115) + ((distance_covered - 500)*100)

print("Hello! Your Total Hire Fee Is Ksh" +str(expense))
print("Thank you for trusting Yamaha Rentals. Looking forward to seeing you soon!")