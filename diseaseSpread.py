import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from PIL import ImageTk, Image
from tkinter import Label

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
    initialInfected = infected
    spreadRate = float(spread_rate_input.get())
    recoveryRate = float(recovery_rate_input.get())
    duration = int(duration_input.get())

    # Get population of specified country from CSV file
    population = get_population()

    # Calculate the number of infected individuals for each day of the simulation
    infected_list = [infected]
    for day in range(duration):
        new_infected = int(infected_list[day] * spreadRate)
        recovered = int(infected_list[day] * recoveryRate)
        infected = max(infected_list[day] + new_infected - recovered, 0)
        infected_list.append(infected)

    # Create a new window to display the results
    result_window = tk.Toplevel(window)
    result_window.title("Simulation Results")

    # Calculate the screen size and center the window
    screen_width = result_window.winfo_screenwidth()
    screen_height = result_window.winfo_screenheight()
    window_width = 800
    window_height = 600
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    result_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create a matplotlib figure to display the graph
    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(111)
    ax.plot(infected_list, marker='o', linestyle='-', linewidth=2)
    ax.set_title(f'{countryName}: Infected Population Over Time', fontsize=16)
    ax.set_xlabel('Days', fontsize=14)
    ax.set_ylabel('Infected Population', fontsize=14)

    # Add the matplotlib figure to the Tkinter window
    canvas = FigureCanvasTkAgg(figure, result_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    description_window = tk.Tk()
    description_window.title("Description")
    description_window.geometry("800x200")
    text_box = tk.Label(description_window, text = f"This chart models {countryName} after {duration} days with"
                                                   f"an infection rate of {spreadRate} and a\nrecover rate of {recoveryRate}."
                                                   f"The initial amount of infected individuals was {initialInfected}."
                                                   f" Each day, the\namount of recovered and newly infected will "
                                                   f"be calculated based off"
                                                   f"the current infected amount,\nthen the recovered people will be subtracted "
                                                   f"from the total infected, and the new infected will be added\n"
                                                   f" This goes on for as many days"
                                                   f" as inputted.\n The end amount of total infected is {infected_list[-1]}.")
    text_box.configure(font=("Arial", 16), justify = 'center', anchor = 'center', padx = 10, pady = 20)
    text_box.pack()

# Create a Tkinter window
window = tk.Tk()
window.title("Disease Spread Simulation")


# Calculate label font size based on window size
label_font_size = int(window.winfo_reqheight() / 10)

# Create entry fields for user input
country_label = tk.Label(window, text="Country:", font=("TkDefaultFont", label_font_size), fg = 'gray7')
country_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
country = tk.Entry(window, font=("TkDefaultFont", label_font_size), fg = 'gray7')
country.grid(row=0, column=1, padx=10, pady=10, sticky="W")
country.configure(bg='gray63')
country_label.configure(bg='gray63')

infected_label = tk.Label(window, text="Initial Infected Population:", font=("TkDefaultFont", label_font_size), fg = 'gray7')
infected_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
infected_input = tk.Entry(window, font=("TkDefaultFont", label_font_size), fg = 'gray7')
infected_input.grid(row=1, column=1, padx=10, pady=10, sticky="W")
infected_input.configure(bg='gray63')
infected_label.configure(bg = 'gray63')

spread_rate_label = tk.Label(window, text="Rate of Spread per Day:", font=("TkDefaultFont", label_font_size), fg = 'gray7')
spread_rate_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
spread_rate_input = tk.Entry(window, font=("TkDefaultFont", label_font_size), fg = 'gray7')
spread_rate_input.grid(row=2, column=1, padx=10, pady=10, sticky="W")
spread_rate_input.configure(bg = 'gray63')
spread_rate_label.configure(bg='gray63')

recovery_rate_label = tk.Label(window, text="Rate of Recovery per Day:", font=("TkDefaultFont", label_font_size), fg = 'gray7')
recovery_rate_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")
recovery_rate_input = tk.Entry(window, font=("TkDefaultFont", label_font_size), fg = 'gray7')
recovery_rate_input.grid(row=3, column=1, padx=10, pady=10, sticky="W")
recovery_rate_input.configure(bg='gray63')
recovery_rate_label.configure(bg='gray63')

duration_label = tk.Label(window, text="Duration of Simulation (in days):", font=("TkDefaultFont", label_font_size), fg = 'gray7')
duration_label.grid(row=4, column=0, padx=10, pady=10, sticky="W")
duration_input = tk.Entry(window, font=("TkDefaultFont", label_font_size), fg = 'gray7')
duration_input.grid(row=4, column=1, padx=10, pady=10, sticky="W")
duration_input.configure(bg='gray63')
duration_label.configure(bg='gray63')

# Create a button to start the simulation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Center all labels and entry fields
for child in window.winfo_children():
    child.grid_configure(padx=50, pady=10)
    child.grid_configure(sticky="EW")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window.configure(bg='steel blue')

# Start the Tkinter event loop
window.mainloop()