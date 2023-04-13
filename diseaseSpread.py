import pandas as pd
import tkinter as tk
import chart

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
    totalPercentage = []
    recoveredPeople = []
    for day in range(1, duration):
        new_infected = int(infected_list[day-1] * spreadRate)
        recovered = int(infected_list[day-1] * recoveryRate)
        recoveredPeople.append(recovered)
        infected = max(infected_list[day-1] + new_infected - recovered, 0)
        infected_list.append(infected)

    length = len(infected_list)
    for num in range(0, length):
        totalPercentage.append(str(round(infected_list[num] / population * 100000, 2)) + '%')
    # Create a new window to display the results
    result_window = tk.Toplevel(window)
    result_window.geometry("1000x800")
    result_window.title("Simulation Results")

    # Define colors and font for the label
    bg_color = "#f2f2f2"  # light gray background
    fg_color = "#333333"  # dark gray foreground
    font = ("Arial", 16, "bold")  # font family, size and weight

    # Create a label to display the results
    new_output_label = tk.Label(result_window, text=f'{countryName}: \nPopulation of Infected '
                                                    f'(each element represents a day): '
                                                    f'{infected_list}'
                                                    f'\nInfected Percentages (per day): {totalPercentage}'
    # will be 1 less array length because first day does
    # not have recovered value
                                                    f'\nPeople Recovered Each Day: {recoveredPeople}',
                                bg=bg_color, fg=fg_color, font=font)
    new_output_label.pack(pady=50)

    # Center the label in the middle of the window
    result_window.update_idletasks()
    x = (result_window.winfo_width() - new_output_label.winfo_width()) // 2
    y = (result_window.winfo_height() - new_output_label.winfo_height()) - 999 // 2
    new_output_label.place(x=x, y=y)

# Create a Tkinter window
window = tk.Tk()
window.geometry("750x400")
window.title("Disease Spread Simulation")

# Calculate label font size based on window size
label_font_size = int(window.winfo_reqheight() / 10)

# Create entry fields for user input
country_label = tk.Label(window, text="Country:", font=("TkDefaultFont", label_font_size))
country_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
country = tk.Entry(window, font=("TkDefaultFont", label_font_size))
country.grid(row=0, column=1, padx=10, pady=10, sticky="W")

infected_label = tk.Label(window, text="Initial Infected Population:", font=("TkDefaultFont", label_font_size))
infected_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
infected_input = tk.Entry(window, font=("TkDefaultFont", label_font_size))
infected_input.grid(row=1, column=1, padx=10, pady=10, sticky="W")

spread_rate_label = tk.Label(window, text="Rate of Spread per Day:", font=("TkDefaultFont", label_font_size))
spread_rate_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
spread_rate_input = tk.Entry(window, font=("TkDefaultFont", label_font_size))
spread_rate_input.grid(row=2, column=1, padx=10, pady=10, sticky="W")

recovery_rate_label = tk.Label(window, text="Rate of Recovery per Day:", font=("TkDefaultFont", label_font_size))
recovery_rate_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")
recovery_rate_input = tk.Entry(window, font=("TkDefaultFont", label_font_size))
recovery_rate_input.grid(row=3, column=1, padx=10, pady=10, sticky="W")

duration_label = tk.Label(window, text="Duration of Simulation:", font=("TkDefaultFont", label_font_size))
duration_label.grid(row=4, column=0, padx=10, pady=10, sticky="W")
duration_input = tk.Entry(window, font=("TkDefaultFont", label_font_size))
duration_input.grid(row=4, column=1, padx=10, pady=10, sticky="W")

# Create a button to start the simulation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


# Create a label to display the results
output_label = tk.Label(window, text="", font=("TkDefaultFont", label_font_size))
output_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Center all labels and entry fields
for child in window.winfo_children():
    child.grid_configure(padx=50, pady=10)
    child.grid_configure(sticky="EW")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# Start the Tkinter event loop
window.mainloop()
