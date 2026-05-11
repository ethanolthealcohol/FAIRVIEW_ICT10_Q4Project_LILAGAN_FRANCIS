from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt

# these are the days in a fixed order
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# these store absencess
data = {day: 0 for day in days}

def update(e):
    # this gets the values from HTML
    day_value = document.getElementById("day").value
    abs_input = document.getElementById("absences").value

    try:
        value = int(abs_input)
        data[day_value] = value

        # convert to numpy array
        y = np.array([data[d] for d in days])

        # this clears the previous plot
        plt.clf()

        # this is responsible for the graph itself
        plt.plot(days, y, marker='o')
        plt.title("Weekly Attendance (Absences)")
        plt.xlabel("Day")
        plt.ylabel("Absences")
        plt.grid(True)

        # this clears the outputs
        output_div = document.getElementById("output")
        output_div.innerHTML = ""

        # this displays the graph in the HTML after clicking the button
        display(plt, target="output")

    except:
        print("Enter a valid number")