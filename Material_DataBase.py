import tkinter as tk
from tkinter import messagebox

# Create an empty dictionary to store the material properties
material_properties = {}


def add_material():
    # Get the values of the material properties from the entry widgets
    material = material_entry.get()
    density = density_entry.get()
    viscosity = viscosity_entry.get()

    # Check if the material is already in the dictionary
    if material in material_properties:
        # Display a warning message if the material is already in the dictionary
        warning_label['text'] = 'This material is already in the database!'
    else:
        # Add the material properties to the dictionary
        material_properties[material] = {'density': density, 'viscosity': viscosity}
        # Clear the entry widgets and reset the warning label
        material_entry.delete(0, 'end')
        density_entry.delete(0, 'end')
        viscosity_entry.delete(0, 'end')
        warning_label['text'] = ''
        # Display a message to indicate that the material has been added to the database
        messagebox.showinfo("Success", "Material added to the database!")
        # Update the material counter label
        material_counter_label['text'] = f'Number of materials in the database: {len(material_properties)}'


def view_library():
    # Clear the listbox
    material_list.delete(0, 'end')

    # Iterate through the materials in the dictionary and add them to the listbox
    for material in material_properties:
        material_list.insert('end', material)


# Create the main window
window = tk.Tk()
window.title("Fluidic Material Properties Database")

# Create the label and entry widgets for the material name
material_label = tk.Label(text="Material:")
material_entry = tk.Entry()

# Create the label and entry widgets for the density
density_label = tk.Label(text="Density (g/cm^3):")
density_entry = tk.Entry()

# Create the label and entry widgets for the viscosity
viscosity_label = tk.Label(text="Viscosity (cP):")
viscosity_entry = tk.Entry()

# Create the button widget to add the material to the library
add_button = tk.Button(text="Add", command=add_material)

# Create the label widget to display warning messages
warning_label = tk.Label(text="")

# Create the listbox widget to display the materials in the library
material_list = tk.Listbox()

# Create the button widget to view the materials in the library
view_library_button = tk.Button(text="View Library", command=view_library)

# Create the label widget to display the number of materials in the database
material_counter_label = tk.Label(text="Number of materials in the database: 0", fg="blue")

# Place the widgets in the window
material_label.grid(row=0, column=0)
material_entry.grid(row=0, column=1)
density_label.grid(row=1, column=0)
density_entry.grid(row=1, column=1)
viscosity_label.grid(row=2, column=0)
viscosity_entry.grid(row=2, column=1)
add_button.grid(row=3, column=0)
warning_label.grid(row=3, column=1)
material_list.grid(row=4, column=0, columnspan=2)
view_library_button.grid(row=5, column=0, columnspan=2)
material_counter_label.grid(row=6, column=0, columnspan=2)

# Run the main loop
window.mainloop()

