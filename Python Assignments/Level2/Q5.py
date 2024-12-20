def analyze_weather(temperatures):
    if not temperatures:
        return "No temperature readings provided."

    average_temp = sum(temperatures) / len(temperatures)

    highest_temp = max(temperatures)
    lowest_temp = min(temperatures)

    print(f"Average Temperature: {average_temp:.1f}")
    print(f"Highest Temperature: {highest_temp}")
    print(f"Lowest Temperature: {lowest_temp}")

# Sample input
temperatures = [25, 28, 21, 24, 27]
analyze_weather(temperatures)
