# Write a program that:
# Creates a text file called "numbers.txt" ✅
# Writes numbers 1 to 50, one per line ✅
# Reads the file back ✅
# Calculates and prints the sum of all numbers in the file ✅

# Additional attempts
# Allow the user to specify how many numbers to generate ✅
# Add error handling to your solution ✅
# Calculate other statistics (average, min, max) ✅


def writeNumbers():
    prompt = int(input("How many numbers do you want to generate? "))
    if prompt > 1:
        for num in range(1, prompt + 1):
            with open("numbers.txt", "a") as file:
                file.write(f"{num}\n")
        print(f"You have just created a range of numbers from 1-{prompt} in a file named numbers.txt!\n")
    elif prompt < 2:
        print("Please enter a number greater than 1.")
        writeNumbers()

writeNumbers()


def stats():
    numbers = []
    with open("numbers.txt") as file:
        for line in file:
            numbers.append(int(line.strip()))
        total = sum(numbers)
        print(f"The total of the numbers in the file is: {total}\n")

        average = total/2
        print(f"The average of the numbers in the file is: {average}")
        print(f"The minimum number in the file is: {min(numbers)}")
        print(f"The maximum number in the file is: {max(numbers)}")
        

stats()