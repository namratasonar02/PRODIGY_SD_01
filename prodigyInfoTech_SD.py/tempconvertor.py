import tkinter as tk
from tkinter import ttk, messagebox

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f + 459.67) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k * 9/5) - 459.67

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = temp_unit.get()
        
        if unit == 'Celsius':
            fahrenheit = celsius_to_fahrenheit(temp)
            kelvin = celsius_to_kelvin(temp)
            result = f"{temp:.2f} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K"
        
        elif unit == 'Fahrenheit':
            celsius = fahrenheit_to_celsius(temp)
            kelvin = fahrenheit_to_kelvin(temp)
            result = f"{temp:.2f} °F = {celsius:.2f} °C = {kelvin:.2f} K"
        
        elif unit == 'Kelvin':
            celsius = kelvin_to_celsius(temp)
            fahrenheit = kelvin_to_fahrenheit(temp)
            result = f"{temp:.2f} K = {celsius:.2f} °C = {fahrenheit:.2f} °F"
        
        label_result.config(text=result)
    
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for temperature.")

# Set up the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")
root.configure(bg='#e3f2fd')

# Create and place widgets
label_temp = tk.Label(root, text="Enter temperature:", bg='#e3f2fd', font=('Helvetica', 14, 'bold'))
label_temp.pack(pady=10)

entry_temp = tk.Entry(root, font=('Helvetica', 14), borderwidth=2, relief="groove")
entry_temp.pack(pady=5)

label_unit = tk.Label(root, text="Select unit:", bg='#e3f2fd', font=('Helvetica', 14, 'bold'))
label_unit.pack(pady=5)

temp_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], font=('Helvetica', 14), state='readonly')
temp_unit.pack(pady=5)
temp_unit.set("Celsius")

button_convert = tk.Button(root, text="Convert", command=convert_temperature, font=('Helvetica', 14, 'bold'), bg='#ff5722', fg='white')
button_convert.pack(pady=20)

label_result = tk.Label(root, text="", bg='#e3f2fd', font=('Helvetica', 16, 'bold'), fg='#00796b')
label_result.pack(pady=10)

# Run the main loop
root.mainloop()
