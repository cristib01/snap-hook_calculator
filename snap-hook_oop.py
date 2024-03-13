import os
import tkinter as tk
from tkinter import ttk, messagebox
import PIL
from PIL import Image, ImageTk
from snap_hooks_data import *
import math

ROOT_WIDTH = 1000
ROOT_HEIGHT = 800


class SnapHookCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Snap-hook calculator \u00A9 PC")
        self.set_window_centered()  # Added the screen centering
        self.root.configure(bg="#84CEEB")
        self.create_widgets()

    def set_window_centered(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = int((screen_width - ROOT_WIDTH) / 2)
        y_position = int((screen_height - ROOT_HEIGHT) / 2)

        self.root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}+{x_position}+{y_position}")

    def create_widgets(self):
        self.create_dropdown()
        self.create_display_button()
        self.create_canvas()
        self.create_display_label()
        self.create_calculate_button()
        self.create_result_label()

    def create_dropdown(self):
        options = ["Select snap-hook type"] + [snap_hook["name"] for snap_hook in snap_hooks]
        self.dropdown_var = tk.StringVar()
        self.dropdown_var.set(options[0])
        self.dropdown = ttk.Combobox(self.root, values=options, textvariable=self.dropdown_var,
                                     font=("Arial", 12), width=int(ROOT_WIDTH / 25))
        self.dropdown.grid(row=0, column=0, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

    def create_display_button(self):
        self.display_button = tk.Button(self.root, text="Display information", command=self.display_information,
                                        font=("Arial", 12), width=int(ROOT_WIDTH / 25))
        self.display_button.grid(row=1, column=0, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

    def create_canvas(self):
        # Create canvas for the first image
        self.canvas = tk.Canvas(self.root, width=158, height=155, bg="#BEB2A7", relief="groove")
        self.canvas.grid(row=2, column=0, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

        # Create canvas for the second image
        self.canvas_section = tk.Canvas(self.root, width=158, height=155, bg="#BEB2A7", relief="groove")
        self.canvas_section.grid(row=2, column=0, padx=(ROOT_WIDTH / 100) + 208, pady=ROOT_HEIGHT / 100, sticky=tk.W)

    def create_display_label(self):
        self.display_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#84CEEB")
        self.display_label.grid(row=4, column=0, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

    def create_calculate_button(self):
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate, font=("Arial", 12),
                                          state=tk.DISABLED)
        self.calculate_button.grid(row=1, column=1, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

    def create_result_label(self):
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#84CEEB", justify=tk.LEFT)
        self.result_label.grid(row=2, column=1, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

    def display_information(self):
        selection = self.dropdown_var.get()
        self.canvas.delete("all")
        self.canvas_section.delete("all")
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) and hasattr(self, 'fields_frame'):
                widget.destroy()

        # Reset the flag before checking each selection
        should_display_button = False

        for snap_hook in snap_hooks:
            if snap_hook["name"] == selection:
                self.canvas.delete("all")
                self.canvas_section.delete("all")
                self.display_image(snap_hook["image_path"])
                self.display_section_image(snap_hook["section_image_path"])
                self.display_label.config(text=f"Enter information about {snap_hook['name']}:")
                self.display_fields(snap_hook["fields"])
                self.result_label.config(text="")
                should_display_button = False
                self.calculate_button.config(state=tk.NORMAL)

                # Define a dictionary for mapping snap-hook names to the desired button text
                button_texts = {
                    "Improved - Rectangular - Type 1": "Q Magnification Factor",
                    "Improved - Rectangular - Type 2": "Q Magnification Factor",
                    "Improved - Rectangular - Type 3": "Q Magnification Factor",
                    "Improved - Rectangular - Type 4": "Q Magnification Factor",
                    "Improved - Rectangular - Type 5": "Q Magnification Factor",
                    "Improved - Rectangular - Type 2T": "Q Magnification Factor",
                    "Improved - Rectangular - Type 5T": "Q Magnification Factor",
                    "Classic - Ring segment - Constant": "K & Z",
                    "Classic - Ring segment - Decrease 1/2 - Y": "K & Z",
                    "Classic - Ring segment - Decrease 1/4 - Z": "K & Z",
                }

                if snap_hook["name"] in button_texts:
                    should_display_button = True
                    self.check_should_display_button(snap_hook)

        if not should_display_button:
            # If there is no need to display the button, destroy the existing button (if it exists)
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget("text") in ["Q Magnification Factor", "K & Z"]:
                    widget.destroy()

    def check_should_display_button(self, snap_hook):

        # Define a dictionary for mapping snap-hook names to the desired button text
        button_texts = {
            "Improved - Rectangular - Type 1": "Q Magnification Factor",
            "Improved - Rectangular - Type 2": "Q Magnification Factor",
            "Improved - Rectangular - Type 3": "Q Magnification Factor",
            "Improved - Rectangular - Type 4": "Q Magnification Factor",
            "Improved - Rectangular - Type 5": "Q Magnification Factor",
            "Improved - Rectangular - Type 2T": "Q Magnification Factor",
            "Improved - Rectangular - Type 5T": "Q Magnification Factor",
            "Classic - Ring segment - Constant": "K & Z",
            "Classic - Ring segment - Decrease 1/2 - Y": "K & Z",
            "Classic - Ring segment - Decrease 1/4 - Z": "K & Z",
        }

        table_button_text = button_texts[snap_hook['name']]
        # Create a button with the specified text
        table_button = tk.Button(self.root, text=f"{table_button_text}",
                                 command=lambda s=snap_hook: self.display_help_tables(s),
                                 font=("Arial", 12), width=int(ROOT_WIDTH / 25))
        # Place the button in the GUI
        table_button.grid(row=6, column=0, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 100, sticky=tk.W)

    def display_help_tables(self, snap_hook):
        table_window = tk.Toplevel(self.root)
        table_window.geometry("800x800")  # Set table window size

        if snap_hook["name"] in ["Classic - Ring segment - Constant",
                                 "Classic - Ring segment - Decrease 1/2 - Y",
                                 "Classic - Ring segment - Decrease 1/4 - Z"]:
            image_path = "media/KZRingCase.png"
        elif snap_hook["name"] in ["Improved - Rectangular - Type 1",
                                   "Improved - Rectangular - Type 2",
                                   "Improved - Rectangular - Type 3",
                                   "Improved - Rectangular - Type 4",
                                   "Improved - Rectangular - Type 5"]:
            image_path = "media/UniformBeamQFactor.jpg"
        elif snap_hook["name"] in ["Improved - Rectangular - Type 2T",
                                   "Improved - Rectangular - Type 5T"]:
            image_path = "media/TaperedBeamQFactor.jpg"

        table_image = Image.open(image_path)
        table_image = table_image.resize((800, 800), PIL.Image.LANCZOS)  # Resize image
        img_tk_table = ImageTk.PhotoImage(table_image)

        label_table = tk.Label(table_window, image=img_tk_table)
        label_table.image = img_tk_table
        label_table.pack()

    def display_image(self, image_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        absolute_image_path = os.path.join(current_dir, image_path)
        image = Image.open(absolute_image_path)
        image = image.resize((158, 155), PIL.Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(image)
        self.canvas.create_image(1, 1, anchor=tk.NW, image=img_tk)
        self.canvas.img_tk = img_tk

    def display_section_image(self, section_image_path):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        absolute_section_image_path = os.path.join(current_dir, section_image_path)
        section_image = Image.open(absolute_section_image_path)
        section_image = section_image.resize((158, 155), PIL.Image.LANCZOS)
        img_tk_section = ImageTk.PhotoImage(section_image)
        self.canvas_section.create_image(1, 1, anchor=tk.NW, image=img_tk_section)
        self.canvas_section.img_tk = img_tk_section

    def display_fields(self, fields):
        fields_frame = tk.Frame(self.root, bg="#BEB2A7", relief="groove", bd=3)
        fields_frame.grid(row=5, column=0, padx=ROOT_WIDTH / 100, pady=ROOT_HEIGHT / 60, sticky=tk.W)
        self.fields_values = []

        for i, field in enumerate(fields):
            label = tk.Label(fields_frame, text=field, bg="#BEB2A7", font=("Arial", 10, "bold"))
            label.grid(row=i, column=0, sticky=tk.W)
            entry = tk.Entry(fields_frame, width=10, font=("Arial", 10))
            entry.grid(row=i, column=1)
            self.fields_values.append((label, entry))

        self.fields_frame = fields_frame

    def convert_to_float(self, value):
        try:
            return float(value)
        except ValueError:
            return float(value.replace(',', '.'))

    def validate_entry_values(self):
        for label, entry in self.fields_values:
            value = entry.get()
            try:
                float(value)
            except ValueError:
                # Display a warning message and reset the value to 0
                tk.messagebox.showwarning("Invalid Input",
                                          f"Invalid input for {label.cget('text')}. "
                                          f"Please enter a numeric value.")
                entry.delete(0, tk.END)
                entry.insert(tk.END, "0.0")

    def extract_data_from_fields(self):
        global data
        data = {}  # A dictionary to store the extracted data
        for label, entry in self.fields_values:
            field_name = label.cget('text')  # Field name based on the associated label
            value = entry.get()  # The value entered for the input field
            data[field_name] = float(value)  # Add to the dictionary (converting to float type)

        return data

    def calculate(self):
        self.validate_entry_values()
        data = self.extract_data_from_fields()

        # Check the snap-hook type and use the corresponding formula
        snap_hook_type = self.dropdown_var.get()
        if snap_hook_type in SNAP_HOOK_FORMULAS:
            formulas = SNAP_HOOK_FORMULAS[snap_hook_type]

            # Ensure there are at least two formulas in the list
            if len(formulas) >= 2:
                formula_for_y = formulas[0]
                formula_for_p = formulas[1]

                y_result = eval(formula_for_y, None, data)
                p_result = eval(formula_for_p, None, data)

                formatted_data = '\n'.join([f"{key}={value}" for key, value in data.items()])
                self.result_label.config(
                    text=f"Y - Allowable snap deflection = {y_result:.3f} mm "
                         f"\nP - Deflection force = {p_result:.3f} N "
                         f"\n\nValues used for calculation:\n{formatted_data}")
            else:
                self.result_label.config(text="Not enough formulas defined for this snap-hook type")
        else:
            self.result_label.config(text="Formula not defined for this snap-hook type")


# Define a mapping of snap-hook types to their formulas
SNAP_HOOK_FORMULAS = {
    'Improved - Rectangular - Type 1': ["0.67 * "
                                        "(data['ε (Strain)'] * "
                                        "data['L (Length of Latch)'] ** 2 ) * "
                                        "data['Q (Deflection Magnification Factor)'] / "
                                        "(data['t/h (Wall Thickness)'])",
                                        "((data['b (Base Width)'] * data['t/h (Wall Thickness)'] ** 2 ) / 6) * "
                                        "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                        "data['L (Length of Latch)'])"],
    'Improved - Rectangular - Type 2': ["0.67 * "
                                        "(data['ε (Strain)'] * "
                                        "data['L (Length of Latch)'] ** 2 ) * "
                                        "data['Q (Deflection Magnification Factor)'] / "
                                        "(data['t/h (Wall Thickness)'])",
                                        "((data['b (Base Width)'] * data['t/h (Wall Thickness)'] ** 2 ) / 6) * "
                                        "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                        "data['L (Length of Latch)'])"],
    'Improved - Rectangular - Type 2T': ["1.09 * "
                                         "(data['ε (Strain)'] * "
                                         "data['L (Length of Latch)'] ** 2 ) * "
                                         "data['Q (Deflection Magnification Factor)'] / "
                                         "(data['t/h (Wall Thickness)'])",
                                         "((data['b (Base Width)'] * data['t/h (Wall Thickness)'] ** 2 ) / 6) * "
                                         "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                         "data['L (Length of Latch)'])"],
    'Improved - Rectangular - Type 3': ["0.67 * "
                                        "(data['ε (Strain)'] * "
                                        "data['L (Length of Latch)'] ** 2 ) * "
                                        "data['Q (Deflection Magnification Factor)'] / "
                                        "(data['t/h (Wall Thickness)'])",
                                        "((data['b (Base Width)'] * data['t/h (Wall Thickness)'] ** 2 ) / 6) * "
                                        "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                        "data['L (Length of Latch)'])"],
    'Improved - Rectangular - Type 4': ["0.67 * "
                                        "(data['ε (Strain)'] * "
                                        "data['L (Length of Latch)'] ** 2 ) * "
                                        "data['Q (Deflection Magnification Factor)'] / "
                                        "(data['t/h (Wall Thickness)'])",
                                        "((data['b (Base Width)'] * data['t/h (Wall Thickness)'] ** 2 ) / 6) * "
                                        "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                        "data['L (Length of Latch)'])"],
    'Improved - Rectangular - Type 5': ["0.67 * "
                                        "(data['ε (Strain)'] * "
                                        "data['L (Length of Latch)'] ** 2 ) * "
                                        "data['Q (Deflection Magnification Factor)'] / "
                                        "(data['t/h (Wall Thickness)'])",
                                        "((data['b (Base Width)'] * data['t/h (Wall Thickness)'] ** 2 ) / 6) * "
                                        "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                        "data['L (Length of Latch)'])"],
    'Improved - Rectangular - Type 5T': ["1.09 * "
                                         "(data['ε (Strain)'] * "
                                         "data['L (Length of Latch)'] ** 2 ) * "
                                         "data['Q (Deflection Magnification Factor)'] / "
                                         "(data['t/h (Wall Thickness)'])",
                                         "((data['b (Base Width)'] * data['t/h (Wall Thickness)'] ** 2 ) / 6) * "
                                         "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                         "data['L (Length of Latch)'])"],
    'L Beam': ["(data['ε (Strain)'] * (12 * data['L2 (Length of support [1])'] * "
               "(data['L1 (Length of slot)'] + data['R (Radius at neutral axis)']) ** 2 + "
               "4 * data['L1 (Length of slot)'] ** 3 + "
               "3 * data['R (Radius at neutral axis)'] * (2 * 3.14159 * data['L1 (Length of slot)'] ** 2 + "
               "3.14159 * data['R (Radius at neutral axis)'] ** 2 + "
               "8 * data['L1 (Length of slot)'] * data['R (Radius at neutral axis)']))) /"
               "(6 * data['t/h (Wall Thickness)'] * (data['L1 (Length of slot)'] + data['R (Radius at neutral axis)']))",
               "(data['ε (Strain)'] * data['E (Flexural Modulus)'] * data['b (Base Width)'] * "
               "data['t/h (Wall Thickness)'] ** 2) /"
               "(6 * (data['L1 (Length of slot)'] + data['R (Radius at neutral axis)']))"],
    'U Beam Case1': ["data['ε (Strain)'] * "
                     "(6 * data['L1 (Length of slot)'] ** 3 + (9 * data['R (Radius at neutral axis)'] * "
                     "(data['L1 (Length of slot)'] * "
                     "(2 * 3.14159 * data['L1 (Length of slot)'] + 8 * data['R (Radius at neutral axis)']) + "
                     "3.14159 * data['R (Radius at neutral axis)'] ** 2)) + "
                     "6 * data['L2 (Length of support [1])'] * (3 * data['L1 (Length of slot)'] ** 2 - "
                     "3 * data['L1 (Length of slot)'] * data['L2 (Length of support [1])'] + "
                     "data['L2 (Length of support [1])'] ** 2)) /"
                     "(9 * data['t/h (Wall Thickness)'] * "
                     "(data['L1 (Length of slot)'] + data['R (Radius at neutral axis)']))",
                     "(data['ε (Strain)'] * data['E (Flexural Modulus)'] * data['b (Base Width)'] * "
                     "data['t/h (Wall Thickness)'] ** 2) /"
                     "(6 * (data['L1 (Length of slot)'] + data['R (Radius at neutral axis)']))"],
    'U Beam Case2': ["(data['ε (Strain)'] / (3 * data['t/h (Wall Thickness)'] * "
                     "(data['L1 (Length of slot)'] + data['R (Radius at neutral axis)']))) * "
                     "(4 * data['L1 (Length of slot)'] ** 3 + 2 * data['L3 (Length of support [2])'] ** 3 + "
                     "3 * data['R (Radius at neutral axis)'] * "
                     "(data['L1 (Length of slot)'] * (2 * 3.14159 * data['L1 (Length of slot)'] +"
                     "8 * data['R (Radius at neutral axis)']) + 3.14159 * data['R (Radius at neutral axis)']** 2))",
                     "(data['ε (Strain)'] * data['E (Flexural Modulus)'] * data['b (Base Width)'] * "
                     "data['t/h (Wall Thickness)'] ** 2) /"
                     "(6 * (data['L1 (Length of slot)'] + data['R (Radius at neutral axis)']))"],
    'Classic - Rectangular - Constant': ["0.67 * (data['ε (Strain)'] * "
                                         "data['L (Length of Latch)'] ** 2) / "
                                         "(data['t/h (Wall Thickness)'])",
                                         "((data['b (Base Width)'] * data['t/h (Wall Thickness)'] ** 2 ) / 6) * "
                                         "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                         "data['L (Length of Latch)'])"],
    'Classic - Rectangular - Decrease 1/2 - Y': ["1.09 * (data['ε (Strain)'] * data['L (Length of "
                                                 "Latch)'] ** 2) / (data['t/h "
                                                 "(Wall Thickness)'])",
                                                 "((data['b (Base Width)'] * data['t/h (Wall Thickness)'] ** 2 ) / "
                                                 "6) * ((data['E (Flexural Modulus)'] * data['ε (Strain)']) / "
                                                 "data['L (Length of Latch)'])"],
    'Classic - Rectangular - Decrease 1/4 - Z': ["0.86 * (data['ε (Strain)'] * data['L (Length of "
                                                 "Latch)'] ** 2) / (data['t/h "
                                                 "(Wall Thickness)'])",
                                                 "((data['b (Base Width)'] * data['t/h (Wall Thickness)'] ** 2 ) / "
                                                 "6) * ((data['E (Flexural Modulus)'] * data['ε (Strain)']) / "
                                                 "data['L (Length of Latch)'])"],
    'Classic - Trapezoid - Constant': ["(data['a (base) (Big base - Trapezoidal)'] + "
                                       "data['b (base) (Small base - Trapezoidal)']) / "
                                       "(2 * data['a (base) (Big base - Trapezoidal)'] + "
                                       "data['b (base) (Small base - Trapezoidal)']) * "
                                       "(data['ε (Strain)'] * data['L (Length of Latch)'] ** 2) / "
                                       "(data['t/h (Wall Thickness)'])",
                                       "(data['t/h (Wall Thickness)'] ** 2 / 12) *"
                                       "(data['a (base) (Big base - Trapezoidal)'] ** 2 +"
                                       "4 * data['a (base) (Big base - Trapezoidal)'] * "
                                       "data['b (base) (Small base - Trapezoidal)'] +  "
                                       "data['b (base) (Small base - Trapezoidal)'] ** 2) / "
                                       "(2 * data['a (base) (Big base - Trapezoidal)'] + "
                                       "data['b (base) (Small base - Trapezoidal)']) * "
                                       "(data['ε (Strain)'] * data['L (Length of Latch)'] ** 2) / "
                                       "(data['t/h (Wall Thickness)'])"],
    'Classic - Trapezoid - Decrease 1/2 - Y': ["1.64 * (data['a (base) (Big base - Trapezoidal)'] + "
                                               "data['b (base) (Small base - Trapezoidal)']) / "
                                               "(2 * data['a (base) (Big base - Trapezoidal)'] + "
                                               "data['b (base) (Small base - Trapezoidal)']) * "
                                               "(data['ε (Strain)'] * data['L (Length of Latch)'] ** 2) / "
                                               "(data['t/h (Wall Thickness)'])",
                                               "(data['t/h (Wall Thickness)'] ** 2 / 12) *"
                                               "(data['a (base) (Big base - Trapezoidal)'] ** 2 +"
                                               "4 * data['a (base) (Big base - Trapezoidal)'] * "
                                               "data['b (base) (Small base - Trapezoidal)'] +  "
                                               "data['b (base) (Small base - Trapezoidal)'] ** 2) / "
                                               "(2 * data['a (base) (Big base - Trapezoidal)'] + "
                                               "data['b (base) (Small base - Trapezoidal)']) * "
                                               "(data['ε (Strain)'] * data['L (Length of Latch)'] ** 2) / "
                                               "(data['t/h (Wall Thickness)'])"],
    'Classic - Trapezoid - Decrease 1/4 - Z': ["1.28 * (data['a (base) (Big base - Trapezoidal)'] + "
                                               "data['b (base) (Small base - Trapezoidal)']) / "
                                               "(2 * data['a (base) (Big base - Trapezoidal)'] + "
                                               "data['b (base) (Small base - Trapezoidal)']) * "
                                               "(data['ε (Strain)'] * data['L (Length of Latch)'] ** 2) / "
                                               "(data['t/h (Wall Thickness)'])",
                                               "(data['t/h (Wall Thickness)'] ** 2 / 12) *"
                                               "(data['a (base) (Big base - Trapezoidal)'] ** 2 +"
                                               "4 * data['a (base) (Big base - Trapezoidal)'] * "
                                               "data['b (base) (Small base - Trapezoidal)'] +  "
                                               "data['b (base) (Small base - Trapezoidal)'] ** 2) / "
                                               "(2 * data['a (base) (Big base - Trapezoidal)'] + "
                                               "data['b (base) (Small base - Trapezoidal)']) * "
                                               "(data['ε (Strain)'] * data['L (Length of Latch)'] ** 2) / "
                                               "(data['t/h (Wall Thickness)'])"],
    'Classic - Ring segment - Constant': ["data['K (Geometric Factor)'] * (data['ε (Strain)'] * "
                                          "data['L (Length of Latch)'] ** 2) / "
                                          "(data['r2 (Outer radius for circular)'])",
                                          "data['Z (Section Modulus)'] * "
                                          "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                          "data['L (Length of Latch)'])"],
    'Classic - Ring segment - Decrease 1/2 - Y': ["1.64 * data['K (Geometric Factor)'] * (data['ε (Strain)'] * "
                                                  "data['L (Length of Latch)'] ** 2) / "
                                                  "(data['r2 (Outer radius for circular)'])",
                                                  "data['Z (Section Modulus)'] * "
                                                  "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                                  "data['L (Length of Latch)'])"],
    'Classic - Ring segment - Decrease 1/4 - Z': ["1.28 * data['K (Geometric Factor)'] * (data['ε (Strain)'] * "
                                                  "data['L (Length of Latch)'] ** 2) / "
                                                  "(data['r2 (Outer radius for circular)'])",
                                                  "data['Z (Section Modulus)'] * "
                                                  "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                                  "data['L (Length of Latch)'])"],
    'Classic - Irregular - Constant': ["1/3 * (data['ε (Strain)'] * "
                                       "data['L (Length of Latch)'] ** 2) / "
                                       "(data['c (Distance outer fiber - neutral axis)'])",
                                       "data['Z (Section Modulus)'] * "
                                       "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                       "data['L (Length of Latch)'])"],
    'Classic - Irregular - Decrease 1/2 - Y': ["0.55 * (data['ε (Strain)'] * "
                                               "data['L (Length of Latch)'] ** 2) / "
                                               "(data['c (Distance outer fiber - neutral axis)'])",
                                               "data['Z (Section Modulus)'] * "
                                               "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                               "data['L (Length of Latch)'])"],
    'Classic - Irregular - Decrease 1/4 - Z': ["0.43 * (data['ε (Strain)'] * "
                                               "data['L (Length of Latch)'] ** 2) / "
                                               "(data['c (Distance outer fiber - neutral axis)'])",
                                               "data['Z (Section Modulus)'] * "
                                               "((data['E (Flexural Modulus)'] * data['ε (Strain)']) /"
                                               "data['L (Length of Latch)'])"]
}

if __name__ == "__main__":
    root = tk.Tk()
app = SnapHookCalculatorApp(root)
root.mainloop()
