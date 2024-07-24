# Exercise 1-2-13
tankCapacity = int(input("Enter the capacity of the fuel Tank: "))
fuelComsumption = int(input("How much fuel is consumed for 100km?: "))
fuelLeft = int(input("How much fuel is left (in %): "))

rangeLeft = (tankCapacity * (fuelLeft / 100)) / (fuelComsumption / 100)

print(f"You have fuel left for {rangeLeft:.1f}")

if rangeLeft < 200:
    print("Refuel")
else:
    print("Continue driving")
