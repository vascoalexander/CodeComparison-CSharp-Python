# Exercise 1-2-9
weight = float(input('Enter the weight of your parcel(in kg): '))
shipmentFee = 0.25
extraWeight = (weight - 10) // 1

if weight <= 10.0:
    shipmentFee = 0.0
elif weight > 20.0:
    shipmentFee = 0.5

if weight - extraWeight - 10 != 0:
    extraWeight += 1

shipmentCost = extraWeight * shipmentFee + 3.0   
print(f"Shipment Cost: {shipmentCost}")