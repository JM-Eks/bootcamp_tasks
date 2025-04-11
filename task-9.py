# You've been hired by a local meteorological office to analyze temperature data from the past month.

# Tasks:
# Create a function called temperatureStats that accepts a list of daily temperatures and returns the minimum, maximum, and average temperatures. ✅
# Add a default parameter that lets the user choose between Celsius and Fahrenheit outputs. ✅
# Create a function called temperatureSummary that uses your first function and returns a formatted string summary of the results. ✅

# 💡 I learnt how to import the statistics module for this.
import statistics

tempUnit = input("Choose a unit (F/C): ")

def temperatureStats(unit):
    temp = []

    with open("daily_temperatures.txt") as file:
        for line in file:
            temp.append(int(line.strip()))

        averageTemp = f"{statistics.mean(temp):.1f} {unit}"
        maxTemp = f"{max(temp)} {unit}"
        minTemp = f"{min(temp)} {unit}"

        # I learnt that returning more than one value like this returns them as a tuple
        return averageTemp, maxTemp, minTemp


def temperatureSummary():
    stats = temperatureStats(tempUnit)
    averageTemp, maxTemp, minTemp = stats
    print("\nTEMPERATURE SUMMARY\n")
    print(f"Highest temperature today is {maxTemp}.")
    print(f"Lowest temperature today is {minTemp}.")
    print(f"The average temperature today is {averageTemp}.")

temperatureSummary()