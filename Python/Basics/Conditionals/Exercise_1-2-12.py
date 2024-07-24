# Exercise 1-2-12
portions = int(input('How much portions to heat?: '))
heatingTime = int(input('Enter the heating time(in sec): '))
heatingTimeMod = 1.0

if portions == 2:
    heatingTimeMod = 1.5
elif portions == 3:
    heatingTimeMod = 2.0
elif portions > 3:
    print('Heating more than 3 portions is not recommended')

m = (heatingTime * heatingTimeMod) // 60
s = (heatingTime * heatingTimeMod) % 60

print(f"Time to heat: {m:.0f} min {s:.0f} sec")

