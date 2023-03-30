import pandas as pd

def outcome (population, infected, duration, spreadRate, recoveryRate):
    for day in range (1, duration + 1):
        recovered = int(infected * recoveryRate)
        infected = int(infected - recovered)
        infected = int((population * spreadRate) + infected)
        if (infected > population):
            print("Everyone is infected");
        else:
            print(f'Day {day}:\n\tInfected: {infected}\n\tRecovered: {recovered}')
    return;

if __name__ == "__main__":
    #Testing Github

    # Read input data from CSV file
    dataset = pd.read_csv('worldpopulation.csv', delimiter ='\t', header = 0)
    #print(dataset.columns)
    countryName = input("Enter a country name: ");
    for index, row in dataset.iterrows():
        if countryName == row['country']:
            population = int(dataset.loc[index, 'population']);
            print(f'{countryName}: {population}');
    check = False;
    while (check != True):
        infected = int(input(f'Enter initial infected population amount (must be less than {int(population * .10)}): '))
        if (infected > population * 10 or infected < 0):
            print('Illegal amount of infected')
            check = False
        else:
            check = True
    spreadRate = float(input("Enter rate of spread per day: "))
    recoveryRate = float(input("Enter rate of recovery per day: "))
    duration = int(input("Enter Time Span (< 7 days): "))

    outcome(population, infected, duration, spreadRate, recoveryRate)
