# Exercise 2-2-7
c = "Frankreich"
print(sorted(c, key=lambda x: x.lower()))

c = "Frankreich"
sorted_chars = sorted(c, key=str.lower)
print(sorted_chars)