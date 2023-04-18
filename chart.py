import matplotlib.pyplot as plt

#with open('worldpopulation.csv') as population_file:
    #reader = csv.DictReader(population_file)
    #infected_people = []
    #population_total = []

    #for row in reader:
       # infected_people.append(int(row['infected'].strip()))
        #population_total.append(int(row['population'].strip()))

def makePlot(infected_list):
    days_list = range(1, len(infected_list) + 1)

    plt.plot(days_list, infected_list)
    plt.title('Number of Infected People over Time')
    plt.xlabel('Days')
    plt.ylabel('Number of Infected People')
    return plt
#Days = range(1, 366)  # assuming the data is for a leap year
#plt.plot(Days, infected_people, label="Infected")
#plt.plot(Days, population_total, label="Population")

#plt.xlabel('Days')
#plt.ylabel('Number of people')
#plt.legend(shadow=True, loc="upper right")

#plt.title('Infected people and total population over time')
#plt.show()



