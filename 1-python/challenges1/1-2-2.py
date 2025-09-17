positive_count = 0
negative_count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break
    elif number > 0:
        positive_count += 1
    else:
        negative_count += 1

print("Number of positive numbers:", positive_count)
print("Number of negative numbers:", negative_count)