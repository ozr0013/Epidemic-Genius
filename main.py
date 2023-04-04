import pandas as pd

# Define function to simulate the spread of a disease over time
def outcome (population, infected, duration, spreadRate, recoveryRate):
    # Iterate over the number of days specified by duration
    for day in range (1, duration + 1):
        # Calculate the number of individuals who have recovered on this day
        recovered = int(infected * recoveryRate)
        # Subtract the number of recovered individuals from the infected population
        infected = int(infected - recovered)
        # Calculate the number of new infections on this day based on the spread rate
        # and add them to the infected population
        infected = int((population * spreadRate) + infected)
        # Check if everyone is infected and print a message if true
        # Calculate the infection rate as a percentage
        infection_rate = (infected / population) * 100
        if infection_rate >= 10:
            quarantine_level = "Level 4 - Full Lockdown."
        elif infection_rate >= 5:
            quarantine_level = "Level 3 - Strict Quarantine. Enforce safety protocols to " \
                               "prevent the need of a full lockdown"
        elif infection_rate >= 2:
            quarantine_level = "Level 2 - Moderate Quarantine. "
        elif infection_rate >= 1:
            quarantine_level = "Level 1 - Basic Quarantine. Consider enforcing stricter protocols to stop the spread."
        else:
            quarantine_level = "No quarantine needed"
        if (infected > population):
            print("Everyone is infected");
        # Otherwise, print the number of infected and recovered individuals for this day
        else:
            print(f'Day {day}:\n\tInfected: {infected}\n\tRecovered: {recovered}\n\tQuarantine Level: {quarantine_level}')
    # End of function

# Main function
if __name__ == "__main__":
    # Read input data from CSV file
    dataset = pd.read_csv('worldpopulation.csv', delimiter ='\t', header = 0)
    # Ask user to input a country name
    countryName = input("Enter a country name: ");
    # Look up the population of the specified country in the dataset
    for index, row in dataset.iterrows():
        if countryName == row['country']:
            population = int(dataset.loc[index, 'population']);
            print(f'{countryName}: {population}');
    # Ask user to input the initial number of infected individuals
    check = False;
    while (check != True):
        infected = int(input(f'Enter initial infected population amount (must be less than {int(population * .10)}): '))
        # Check if the input is within the allowed range and prompt the user to try again if not
        if (infected > population * 10 or infected < 0):
            print('Illegal amount of infected')
            check = False
        else:
            check = True
    # Ask user to input the spread rate and recovery rate
    spreadRate = float(input("Enter rate of spread per day: "))
    recoveryRate = float(input("Enter rate of recovery per day: "))
    # Ask user to input the duration of the simulation
    duration = int(input("Enter Time Span (< 7 days): "))

    # Call the outcome function with the specified parameters
    outcome(population, infected, duration, spreadRate, recoveryRate)