import tkinter as tk

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert():
    try:
        temperature = float(temperature_entry.get())
        if fahrenheit_radio.get():
            converted_temp = fahrenheit_to_celsius(temperature)
            result_label.config(text=f"{temperature:.2f} degrees Fahrenheit is equal to {converted_temp:.2f} degrees Celsius.")
        else:
            converted_temp = celsius_to_fahrenheit(temperature)
            result_label.config(text=f"{temperature:.2f} degrees Celsius is equal to {converted_temp:.2f} degrees Fahrenheit.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid temperature.")

# Create the main application window
root = tk.Tk()
root.title("Temperature Converter")

# Variables to store user inputs
fahrenheit_radio = tk.IntVar()
temperature = tk.DoubleVar()

# Fahrenheit to Celsius Radiobutton
fahrenheit_radio_button = tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=fahrenheit_radio, value=1)
fahrenheit_radio_button.grid(row=0, column=0, columnspan=2)

# Celsius to Fahrenheit Radiobutton
celsius_radio_button = tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=fahrenheit_radio, value=0)
celsius_radio_button.grid(row=1, column=0, columnspan=2)

# Temperature entry
temperature_label = tk.Label(root, text="Enter temperature:")
temperature_label.grid(row=2, column=0)
temperature_entry = tk.Entry(root, textvariable=temperature)
temperature_entry.grid(row=2, column=1)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
