import pandas as pd

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

    for day in range (1, duration + 1):
        recovered = int(infected * recoveryRate)
        infected = int(infected - recovered)
        infected = int((population * spreadRate) + infected)
        if (infected > population):
            print("Everyone is infected");
        else:
            print(f'Day {day}:\n\tInfected: {infected}\n\tRecovered: {recovered}')

# CODE NOT BEING USED
    #country = dataset.loc[0, 'country']
    #infected = input(int()) #int(dataset.loc[0, 'infected'])
    recovered = 0 #int(dataset.loc[0, 'recovered'])
    duration = 14
    #prob_spread_without_epidemic = .10#float(dataset.loc[0, 'prob_spread_without_epidemic'])
    #prob_spread_with_epidemic = .25#float(dataset.loc[0, 'prob_spread_with_epidemic'])
    #epidemic = False

    # Simulate the spread of the disease
   # for day in range(1, duration + 1):
       # newly_infected = 0
        #newly_recovered = 0

        # Calculate probability of spread based on whether there is an epidemic
       # if epidemic:
           # prob_spread = prob_spread_with_epidemic
        #else:
           # prob_spread = prob_spread_without_epidemic

        # Infect susceptible population
        #for person in range(population - recovered):
            #if random.random() < prob_spread:
               # newly_infected += 1

        # Recover infected population
      #for person in range(infected):
           #if random.random() < 0.1:  # Assuming 10% chance of recovery per day
               # newly_recovered += 1

        # Update population counts
        #infected += newly_infected - newly_recovered
        #recovered += newly_recovered

        # Check if epidemic has started
        #if not epidemic and infected > 10:
           # epidemic = True

        # Print daily statistics
        #print(f"Day {day}: {infected} infected, {recovered} recovered in {country}")

        # End simulation if everyone is recovered or epidemic has subsided
        #if infected == 0 or (epidemic and newly_infected == 0):
        #break