import pandas as pd
import tkinter as tk

def get_population():
    # Read input data from CSV file
    dataset = pd.read_csv('worldpopulation.csv', delimiter='\t', header=0)
    # Look up the population of the specified country in the dataset
    for index, row in dataset.iterrows():
        if country.get() == row['country']:
            return int(dataset.loc[index, 'population'])
    return 0

def calculate():
    # Get input values from entry fields
    countryName = country.get()
    infected = int(infected_input.get())
    spreadRate = float(spread_rate_input.get())
    recoveryRate = float(recovery_rate_input.get())
    duration = int(duration_input.get())

    # Get population of specified country from CSV file
    population = get_population()

    # Calculate the number of infected individuals for each day of the simulation
    infected_list = [infected]
    for day in range(1, duration):
        new_infected = int(infected_list[day-1] * spreadRate)
        recovered = int(infected_list[day-1] * recoveryRate)
        infected = max(infected_list[day-1] + new_infected - recovered, 0)
        infected_list.append(infected)

    # Display the results in the output label
    output_label.config(text=f'{countryName}: {population}\nInfected: {infected_list}')

# Create a Tkinter window
window = tk.Tk()
window.title("Simulation")

# Create entry fields for user input
country_label = tk.Label(window, text="Country:")
country_label.grid(row=0, column=0)
country = tk.Entry(window)
country.grid(row=0, column=1)

infected_label = tk.Label(window, text="Initial Infected Population:")
infected_label.grid(row=1, column=0)
infected_input = tk.Entry(window)
infected_input.grid(row=1, column=1)

spread_rate_label = tk.Label(window, text="Rate of Spread per Day:")
spread_rate_label.grid(row=2, column=0)
spread_rate_input = tk.Entry(window)
spread_rate_input.grid(row=2, column=1)

recovery_rate_label = tk.Label(window, text="Rate of Recovery per Day:")
recovery_rate_label.grid(row=3, column=0)
recovery_rate_input = tk.Entry(window)
recovery_rate_input.grid(row=3, column=1)

duration_label = tk.Label(window, text="Duration of Simulation:")
duration_label.grid(row=4, column=0)
duration_input = tk.Entry(window)
duration_input.grid(row=4, column=1)

# Create a button to start the simulation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2)

# Create a label to display the results
output_label = tk.Label(window, text="")
output_label.grid(row=6, column=0, columnspan=2)

# Start the Tkinter event loop
window.mainloop()