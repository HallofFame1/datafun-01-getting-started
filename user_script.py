"""
Complete the script.
"""
# PART 1
temp1 = input("Enter temperature 1 in Celsius: ")
temp2 = input("Enter temperature 2 in Celsius: ")
temp3 = input("Enter temperature 3 in Celsius: ")

temp_1 = float(temp1)
temp_2 = float(temp2)
temp_3 = float(temp3)

# PART 2
sum= temp_1 + temp_2 + temp_3
avg = sum / 3
product = temp_1 * temp_2 * temp_3
smallest = min(temp_1, temp_2, temp_3)
largest = max(temp_1, temp_2, temp_3)
range = largest - smallest

print(" The Sum is :", round(sum, 2))
print(" The Average temperature is:", round(avg, 2))
print("The Product is:", round(product, 2))
print("The Smallest temperature is:", smallest)
print("The Largest temperature is:", largest)
print("The Range of temperatures is:", range)

# PART 3
if temp_3 < 0:
    print("It's below freezing at the Doggy Daycare!")
elif temp_3 == 0:
    print("It's freezing at the Doggy Daycare!")
else:
    print("It's above freezing at the Doggy Daycare!")